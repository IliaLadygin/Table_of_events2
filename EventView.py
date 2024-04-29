import sys
# from PyQt6 import Cont
# from PySide6.QtCore import
from Event import EventFull
from PyQt6.QtCore import QTime, QDate, QDateTime
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QVBoxLayout,
                             QWidget,
                             QPushButton,
                             QListWidget,
                             QGridLayout,
                             QCalendarWidget,
                             QHBoxLayout,
                             QMenu,
                             QTextEdit,
                             QListWidgetItem,
                             QDateEdit,
                             QTimeEdit)


class MainWindow(QMainWindow):
    def __init__(self, event_presenter):
        super().__init__()

        # Общие настройки
        self.setBaseSize(QSize(1000, 1000)) # Задание стандартных размеров окна
        # self.n_times_clicked = 0
        self.setWindowTitle("Table of events") # Название окна

        self.event_presenter = event_presenter

        # Виджеты (слева направо, сверху вниз)
        # Первый слой
        # Виджет полного списка событий
        self.list_events = QListWidget()

        for event in event_presenter.model.events:
            event_str = event_presenter.get_event_to_str_via_tool_tip(event.id)
            self.item = QListWidgetItem()
            self.item.setText(event_str.strip())
            self.item.setToolTip(event.id)
            self.list_events.addItem(self.item)
        self.current_event_in_list = self.list_events.currentItem()

        # Создание контекстного меню
        # self.ctx_list_events = QMenu()
        # # Создание действий контекстного меню
        # action_edit = self.ctx_list_events.addAction("Изменить событие")
        # action_delete = self.ctx_list_events.addAction("Удалить событие")
        # # Привязка действий к методам
        # action_edit.triggered.connect(self.action_edit_is_triggered)
        # action_delete.triggered.connect(self.action_delete_is_triggered)

        # Создание контекстного меню 2
        # self.list_events.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.list_events.customContextMenuRequested.connect(self.show_ctx_menu_list_events)

        # Кнопка добавления события
        self.button_add_event = QPushButton("Добавить событие")
        self.button_add_event.clicked.connect(self.the_add_button_was_clicked)

        # Кнопка редактирования события
        self.button_edit_event = QPushButton("Редактировать событие")
        self.button_edit_event.setCheckable(True)
        self.button_edit_is_checked = False
        self.button_edit_event.setChecked(self.button_edit_is_checked)
        self.button_edit_event.toggled.connect(self.the_edit_button_was_toggled)

        # Кнопка удаления события
        self.button_delete_event = QPushButton("Удалить событие")
        self.button_delete_event.clicked.connect(self.the_delete_button_was_clicked)
        # self.button_delete_event.setCheckable(True)
        # self.button_delete_is_checked = False
        # self.button_delete_event.setChecked(self.button_delete_is_checked)

        # Второй слой
        # Реализация календаря
        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(QSize(200, 200))

        # Показ полной информации о событии
        self.container_full_view_right = QVBoxLayout()
        self.container_full_view_left = QVBoxLayout()
        self.list_info = {"Название": QLineEdit,
                          "Дата начала": QDateEdit,
                          "Дата конца": QDateEdit,
                          "Время начала": QTimeEdit,
                          "Время конца": QTimeEdit,
                          "Описание": QLineEdit,
                          "Место": QLineEdit,
                          "Гиперссылка": QLineEdit}

        for name, widget in self.list_info.items():
            # self.container_full_view_right.addWidget(widget())
            self.container_full_view_left.addWidget(QLabel(name))
        # Позор моим навыкам
        self.title_line, self.date_start_line, self.date_end_line, self.time_start_line, self.time_end_line, self.note_line, self.place_line, self.hyperlink_line = tuple([widget()for widget in self.list_info.values()])
        self.title_line.setEnabled(False)
        self.line_widget_tuple = (self.title_line,
                                 self.date_end_line, self.date_start_line,
                                 self.time_start_line, self.time_end_line,
                                 self.note_line, self.place_line, self.hyperlink_line)
        for widget in self.line_widget_tuple:
            widget.setEnabled(False)

        self.container_full_view_right.addWidget(self.title_line)
        self.container_full_view_right.addWidget(self.date_start_line)
        self.container_full_view_right.addWidget(self.date_end_line)
        self.container_full_view_right.addWidget(self.time_start_line)
        self.container_full_view_right.addWidget(self.time_end_line)
        self.container_full_view_right.addWidget(self.note_line)
        self.container_full_view_right.addWidget(self.place_line)
        self.container_full_view_right.addWidget(self.hyperlink_line)
        self.container_full_view = QHBoxLayout()
        self.container_full_view.addLayout(self.container_full_view_left)
        self.container_full_view.addLayout(self.container_full_view_right)

        self.list_events.itemClicked.connect(self.current_item_was_changed)

        # Информатор (пока не знаю, буду ли делать)
        self.info_view = QLabel()

        # self.input = QLineEdit()  # Создание строки, в которую можно вводить данные
        # self.input.textChanged.connect(self.label.setText)  # textChanged - сигнал редактирования строки

        # Добавление слоёв в которых располагаются виджеты
        # Попытка 1
        # layout_add = QGridLayout()
        # layout_add.addWidget(self.list_events, 0, 0, 0, 1, 1, 0, 1, 1)
        # layout_add.addWidget(self.calendar, 2, 0)
        # layout_add.addWidget(self.button_add_event, 0, 3, 1, 3)
        # layout_add.addWidget(self.info_view, 2, 1)
        # layout_add.addWidget(self.info_view, 3, 3)

        # Попытка 2
        layout_main = QHBoxLayout()
        layout0 = QVBoxLayout()
        layout0.addWidget(self.list_events)
        layout0_123 = QHBoxLayout()
        layout0_123.addWidget(self.button_add_event)
        layout0_123.addWidget(self.button_edit_event)
        layout0_123.addWidget(self.button_delete_event)
        layout0.addLayout(layout0_123)
        layout_main.addLayout(layout0)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.calendar)
        layout1.addLayout(self.container_full_view)
        layout1.addWidget(self.info_view)
        layout_main.addLayout(layout1)

        # Макет
        container = QWidget()
        container.setLayout(layout_main)
        # self.setMouseTracking(True) # должна обрабатывать движение мыши без нажатия, но не работает

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    # Сигнал о нажатии Добавить событие
    def the_add_button_was_clicked(self):
        pass

    # Сигнал об изменении текущего элемента в списке событий
    def current_item_was_changed(self):
        # print(self.list_events.currentItem().text())
        # print(self.list_events.currentItem().toolTip())
        # print(self.list_events.item())
        event = self.event_presenter.get_event_via_tool_tip(self.list_events.currentItem().toolTip())
        self.title_line.setText(event.title)
        self.date_start_line.setDate(QDate.fromString(event.date_start, "yyyy.MM.dd"))
        self.date_end_line.setDate(QDate.fromString(event.date_end, "yyyy.MM.dd"))
        self.time_start_line.setTime(QTime.fromString(event.time_start))
        self.time_end_line.setTime(QTime.fromString(event.time_end))
        self.note_line.setText(event.note)
        self.place_line.setText(event.place)
        self.hyperlink_line.setText(event.hyperlink)
        # self.event_full_view.setText(str(self.list_events.currentRow()))
        pass

    # def mousePressEvent(self, a0):
    #     print(self.current_event_in_list)

    # Триггер нажатия кнопки edit
    def the_edit_button_was_toggled(self):
        self.button_edit_is_checked = self.button_edit_event.isChecked()
        if self.button_edit_is_checked:
            # Старый вариант
            # self.list_events.openPersistentEditor(self.list_events.currentItem())
            # self.list_events.editItem(self.list_events.currentItem())
            # Новый вариант
            self.button_edit_event.setText("Сохранить изменения")
            for widget in self.line_widget_tuple:
                widget.setEnabled(True)
        else:
            # Старый вариант
            # self.list_events.closePersistentEditor(self.list_events.currentItem())
            # Новый вариант
            for widget in self.line_widget_tuple:
                widget.setEnabled(False)
            self.button_edit_event.setText("Редактировать событие")
            current_item = self.list_events.currentItem()
            event_to_delete = self.event_presenter.get_event_via_tool_tip(current_item.toolTip())
            # print(self.event_presenter.get_event_to_str(event_to_delete))
            self.event_presenter.delete_event(event_to_delete)
            print(self.date_start_line.textFromDateTime(self.date_start_line.dateTime()))
            print(self.time_end_line.textFromDateTime(self.time_start_line.dateTime()))
            print(self.note_line.text())
            event = EventFull(current_item.toolTip(), self.title_line.text(),
                              self.date_start_line.textFromDateTime(self.date_start_line.dateTime()), self.date_end_line.textFromDateTime(self.date_end_line.dateTime()),
                              self.time_start_line.textFromDateTime(self.time_start_line.dateTime()), self.time_end_line.textFromDateTime(self.time_end_line.dateTime()),
                              note=self.note_line.text(), place=self.place_line.text(), hyperlink=self.hyperlink_line.text())
            self.event_presenter.add_event(event)
            event.print()
            current_item.setText(self.event_presenter.get_event_to_str(event))
            # Сохранение новой информации в файл


    # Сигнал о нажатии Удалить событие
    def the_delete_button_was_clicked(self):
        item_to_delete = self.list_events.takeItem(self.list_events.currentRow())
        # Сохранение изменений в файл

    # Сигнал о нажатии на событие ПКМ
    def show_ctx_menu_list_events(self, event):
        menu = QMenu()
        menu.addAction(QAction("Отредактировать событие", self))
        menu.addAction(QAction("Удалить событие", self))
        menu.exec(event.globalPos())

    # Методы контексного меню
    def action_edit_is_triggered(self):
        pass

    def action_delete_is_triggered(self):
        pass
    # Перехват контексного меню
    # def contextMenuEvent(self, e):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(e.globalPos())

    # Вмешательство с целью добавить новую операцию, но продолжение после
    # Почему-то не работает так как планируется. Просто добавляет операцию
    # def mousePressEvent(self, event):
    #     print("Mouse pressed!")
        # super(self, MainWindow).contextMenuEvent(event)
        # super().contextMenuEvent(event)
        # super().mousePressEvent(event)


class EventView:
    @staticmethod
    def display_program():
        pass

    def __init__(self, presenter):
        self.presenter = presenter

    def add_event_button_click(self, title, t_start, t_end):
        pass

    def delete_event_button_click(self, index):
        pass

    def edit_event_button_click(self, index, new_title, new_t_start, t_end):
        pass

    def update_events(self, events):
        pass
