import sys
# from PyQt6 import Cont
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
                             QMenu)


class MainWindow(QMainWindow):
    def __init__(self, event_presenter):
        super().__init__()

        # Общие настройки
        self.setBaseSize(QSize(1000, 1000)) # Задание стандартных размеров окна
        # self.n_times_clicked = 0
        self.setWindowTitle("Table of events") # Название окна

        # Виджеты (слева направо, сверху вниз)
        # Первый слой
        self.list_events = QListWidget()
        for event in event_presenter.model.events:
            event_dict = event_presenter.model.get_event_as_dict(event)
            # event_str = (event.title() + "\n" +
            #              event_presenter.get_beauty_event_date(event) + "\n" +
            #              event_presenter.get_beauty_event_time(event))
            event_str = ""
            for key, arg in event_dict.items():
                event_str += key + ": " + str(arg) + "\n"
                if key.lower() == "время конца":
                    break
            self.list_events.addItem(event_str.strip())

        # Создание контекстного меню
        # self.ctx_list_events = QMenu()
        # # Создание действий контекстного меню
        # action_edit = self.ctx_list_events.addAction("Изменить событие")
        # action_delete = self.ctx_list_events.addAction("Удалить событие")
        # # Привязка действий к методам
        # action_edit.triggered.connect(self.action_edit_is_triggered)
        # action_delete.triggered.connect(self.action_delete_is_triggered)

        # Создание контекстного меню 2
        self.list_events.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_events.customContextMenuRequested.connect(self.show_ctx_menu_list_events)

        # Кнопка добавления события
        self.button_add_event = QPushButton("Добавить событие")
        self.button_add_event.clicked.connect(self.the_event_button_was_clicked)

        # Второй слой
        # Реализация календаря
        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(QSize(200, 200))

        # Показ полной информации о событии
        self.event_full_view = QLabel()

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
        layout = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout1.addWidget(self.list_events)
        layout1.addWidget(self.button_add_event)
        layout.addLayout(layout1)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.calendar)
        layout2.addWidget(self.event_full_view)
        layout2.addWidget(self.info_view)
        layout.addLayout(layout2)

        # Макет
        container = QWidget()
        container.setLayout(layout)
        # self.setMouseTracking(True) # должна обрабатывать движение мыши без нажатия, но не работает

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    # Сигнал о нажатии Добавить событие
    def the_event_button_was_clicked(self):
        pass

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
