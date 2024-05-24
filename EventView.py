import sys
# from PyQt6 import Cont
# from PySide6.QtCore import
from pathlib import Path
import os
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
                             QTimeEdit,
                             QFileDialog)


class MainWindow(QMainWindow):
    def __init__(self, event_presenter):
        super().__init__()

        # Общие настройки
        self.setBaseSize(QSize(1000, 1000)) # Задание стандартных размеров окна
        # self.n_times_clicked = 0
        self.setWindowTitle("Table of events") # Название окна

        self.event_presenter = event_presenter
        # Флаг об возможности редакта.
        self.editing_enabled = False
        # Виджеты (слева направо, сверху вниз)
        # Первый слой
        # Виджет полного списка событий
        self.list_events = QListWidget()

        self.list_events.setMouseTracking(False)
        self.list_events.setSortingEnabled(False)

        for event in event_presenter.model.events:
            event_str = event_presenter.get_event_to_str_via_tool_tip(event.id)
            self.item = QListWidgetItem()
            self.item.setText(event_str.strip())
            self.item.setToolTip(event.id)
            self.list_events.addItem(self.item)
        self.current_event_in_list = self.list_events.currentItem()
        self.list_events.setCurrentItem(self.item)
        self.list_events.itemClicked.connect(self.current_item_was_changed)

        # Кнопка добавления события
        self.button_add_event = QPushButton("Добавить событие")
        self.button_add_event.setCheckable(True)
        self.button_add_event.setMinimumWidth(130)
        self.button_add_is_checked = False
        self.button_add_event.setChecked(self.button_add_is_checked)
        self.button_add_event.toggled.connect(self.the_add_button_was_toggled)

        # Кнопка редактирования события
        self.button_edit_event = QPushButton("Редактировать событие")
        self.button_edit_event.setMinimumWidth(145)
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

        # Кнопка показа всех событий
        self.button_all_events = QPushButton("Показать всё")
        self.button_all_events.clicked.connect(self.the_all_events_button_was_clicked)
        self.button_all_events.setCheckable(False)

        # Кнопка импорта событий
        self.button_import = QPushButton("Импорт")
        self.button_import.clicked.connect(self.the_import_button_was_clicked)
        self.button_import.setCheckable(False)

        # Кнопка экспорта событий
        self.button_export = QPushButton("Экспорт")
        self.button_export.clicked.connect(self.the_export_button_was_clicked)
        self.button_export.setCheckable(False)

        # Второй слой
        # Реализация календаря
        self.calendar = QCalendarWidget()
        self.calendar.setMaximumHeight(200)
        self.calendar.setGridVisible(True)
        # print(self.calendar.calendar())
        self.calendar.selectionChanged.connect(self.calendar_day_changed)
        self.calendar.showSelectedDate()

        # Показ полной информации о событии
        self.container_full_view_right = QVBoxLayout()
        self.container_full_view_left = QVBoxLayout()
        self.list_info = {"Название": QLineEdit,
                          "Дата начала": QDateEdit,
                          "Дата конца": QDateEdit,
                          "Время начала": QTimeEdit,
                          "Время конца": QTimeEdit,
                          "Место": QLineEdit,
                          "Гиперссылка": QLineEdit,
                          "Описание": QTextEdit}

        for name, widget in self.list_info.items():
            if name.lower() != 'описание':
                self.container_full_view_left.addWidget(QLabel(name))
        # Позор моим навыкам
        self.title_line, self.date_start_line, self.date_end_line, self.time_start_line, self.time_end_line, self.place_line, self.hyperlink_line, self.note_line = tuple([widget() for widget in self.list_info.values()])
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
        self.container_full_view_right.addWidget(self.place_line)
        self.container_full_view_right.addWidget(self.hyperlink_line)
        self.container_full_view = QHBoxLayout()
        self.container_note_view = QHBoxLayout()
        label_note = QLabel('Описание')
        label_note.setMinimumWidth(77)
        self.container_note_view.addWidget(label_note, alignment=Qt.AlignmentFlag.AlignLeft.AlignTop)
        self.container_note_view.addWidget(self.note_line)
        self.container_full_view.addLayout(self.container_full_view_left)
        self.container_full_view.addLayout(self.container_full_view_right)
        self.container_full_view_final = QVBoxLayout()
        self.container_full_view_final.addLayout(self.container_full_view)
        self.container_full_view_final.addLayout(self.container_note_view)

        # Информатор (пока не знаю, буду ли делать)
        self.info_view = QLabel()

        # Добавление слоёв в которых располагаются виджеты
        layout_main = QHBoxLayout()
        layout0 = QVBoxLayout()
        layout0.addWidget(self.list_events)
        layout11_1 = QVBoxLayout()
        layout11_1.addWidget(self.button_add_event)
        layout11_1.addWidget(self.button_import)
        layout11_2 = QVBoxLayout()
        layout11_2.addWidget(self.button_edit_event)
        layout11_2.addWidget(self.button_export)
        layout11_3 = QVBoxLayout()
        layout11_3.addWidget(self.button_delete_event)
        layout11_3.addWidget(self.button_all_events)
        layout11_123 = QHBoxLayout()
        layout11_123.addLayout(layout11_1)
        layout11_123.addLayout(layout11_2)
        layout11_123.addLayout(layout11_3)
        layout0.addLayout(layout11_123)
        layout_main.addLayout(layout0)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.calendar, alignment=Qt.AlignmentFlag.AlignCenter)
        layout1.addLayout(self.container_full_view_final)
        layout1.addWidget(self.info_view)
        layout_main.addLayout(layout1)

        # Макет
        container = QWidget()
        container.setLayout(layout_main)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    # Удаление информации в строках
    def clear_tuple_lines(self, is_now_editing=False):
        print(is_now_editing)
        if not is_now_editing:
            for widget in self.line_widget_tuple:
                try:
                    widget.setText('')
                except AttributeError:
                    widget.setTime(QTime(0, 0))
                    widget.setDate(QDate.currentDate())
                except:
                    print("Error")

    # Сигнал о нажатии Добавить событие
    def the_add_button_was_toggled(self):
        self.button_add_is_checked = self.button_add_event.isChecked()
        # print(self.button_add_is_checked)
        if self.button_add_is_checked:
            self.calendar.showToday()
            self.calendar.setSelectedDate(QDate.currentDate())
            print(self.title_line.isEnabled())
            self.clear_tuple_lines(is_now_editing=self.title_line.isEnabled())
            self.freeze_left(True)
            self.freeze_right(False)
            # for widget in self.line_widget_tuple:
            #     widget.setEnabled(True)
            # self.list_events.setEnabled(False)
            # self.button_edit_event.setEnabled(False)
            # self.button_delete_event.setEnabled(False)
            # self.info_view.setText('Заполните строки выше.')
            self.button_add_event.setText('Сохранить событие')
        else:
            if not self.title_line.text():
                self.info_view.setText('Событие должно иметь название!')
                self.button_add_event.setChecked(True)
            elif not self.event_presenter.is_dates_valid(self.date_start_line.date(), self.date_end_line.date(),
                                                         self.time_start_line.time(), self.time_end_line.time()):
                self.info_view.setText('Некорректные даты и/или время события.')
                self.button_add_event.setChecked(True)
            else:
                self.freeze_left(False)
                self.freeze_right(True)
                # self.list_events.setEnabled(True)
                # self.button_edit_event.setEnabled(True)
                # self.button_delete_event.setEnabled(True)
                # for widget in self.line_widget_tuple:
                #     widget.setEnabled(False)
                id = self.event_presenter.create_id(self.title_line.text(), self.date_start_line.date(),
                                                    self.time_start_line.time())
                event = EventFull(id, self.title_line.text(),
                                  self.date_start_line.textFromDateTime(self.date_start_line.dateTime()),
                                  self.date_end_line.textFromDateTime(self.date_end_line.dateTime()),
                                  self.time_start_line.textFromDateTime(self.time_start_line.dateTime()),
                                  self.time_end_line.textFromDateTime(self.time_end_line.dateTime()),
                                  note=self.note_line.document().toRawText(), place=self.place_line.text(),
                                  hyperlink=self.hyperlink_line.text())
                self.event_presenter.add_event(event)
                event_str = self.event_presenter.get_event_to_str(event)
                self.item = QListWidgetItem()
                self.item.setText(event_str.strip())
                self.item.setToolTip(event.id)
                self.list_events.addItem(self.item)
                # current_item.setText(self.event_presenter.get_event_to_str(event))
                # Сохранение новой информации в файл
                self.event_presenter.save_new_event_to_file(event)
                self.button_add_event.setText('Добавить событие')
                self.info_view.setText('Событие добавлено.')
        self.editing_enabled = self.title_line.isEnabled()


    # Сигнал об изменении текущего элемента в списке событий
    def current_item_was_changed(self):
        # print(self.list_events.currentItem().text())
        # print(self.list_events.currentItem().toolTip())
        # print(self.list_events.item())
        event = self.event_presenter.get_event_via_tool_tip(self.list_events.currentItem().toolTip())
        self.title_line.setText(event.title)
        self.date_start_line.setDate(QDate.fromString(event.date_start, self.event_presenter.date_format))
        self.date_end_line.setDate(QDate.fromString(event.date_end, self.event_presenter.date_format))
        self.time_start_line.setTime(QTime.fromString(event.time_start))
        self.time_end_line.setTime(QTime.fromString(event.time_end))
        self.note_line.setText(event.note)
        self.place_line.setText(event.place)
        self.hyperlink_line.setText(event.hyperlink)
        self.info_view.setText('')
        # self.event_full_view.setText(str(self.list_events.currentRow()))

    # Триггер нажатия кнопки edit
    def the_edit_button_was_toggled(self):
        self.button_edit_is_checked = self.button_edit_event.isChecked()
        if self.button_edit_is_checked:
            self.button_edit_event.setText("Сохранить изменения")
            self.freeze_left(True)
            self.freeze_right(False)
            # self.list_events.setEnabled(False)
            # self.list_events.setEnabled(False)
            # self.button_add_event.setEnabled(False)
            # self.button_delete_event.setEnabled(False)
            # for widget in self.line_widget_tuple:
            #     widget.setEnabled(True)
        else:
            if not self.title_line.text():
                self.info_view.setText('Событие должно иметь название!')
                self.button_edit_event.setChecked(True)
            elif not self.event_presenter.is_dates_valid(self.date_start_line.date(), self.date_end_line.date(),
                                                         self.time_start_line.time(), self.time_end_line.time()):
                self.info_view.setText('Некорректные даты и/или время события.')
                self.button_edit_event.setChecked(True)
            else:
                self.button_edit_event.setText("Редактировать событие")
                self.freeze_left(False)
                # for widget in self.line_widget_tuple:
                #     widget.setEnabled(False)
                self.freeze_right(True)
                # self.list_events.setEnabled(True)
                # self.button_add_event.setEnabled(True)
                # self.button_delete_event.setEnabled(True)
                current_item = self.list_events.currentItem()
                event_to_delete = self.event_presenter.get_event_via_tool_tip(current_item.toolTip())
                self.event_presenter.delete_event(event_to_delete)
                event = EventFull(current_item.toolTip(), self.title_line.text(),
                                  self.date_start_line.textFromDateTime(self.date_start_line.dateTime()), self.date_end_line.textFromDateTime(self.date_end_line.dateTime()),
                                  self.time_start_line.textFromDateTime(self.time_start_line.dateTime()), self.time_end_line.textFromDateTime(self.time_end_line.dateTime()),
                                  note=self.note_line.document().toRawText(), place=self.place_line.text(), hyperlink=self.hyperlink_line.text())
                self.event_presenter.add_event(event)
                current_item.setText(self.event_presenter.get_event_to_str(event))
                # Сохранение новой информации в файл
                self.event_presenter.save_new_event_to_file(event)
                self.info_view.setText('Изменения сохранены.')
        self.editing_enabled = self.title_line.isEnabled()

    # Сигнал о нажатии Удалить событие
    def the_delete_button_was_clicked(self):
        current_item = self.list_events.currentItem()
        id = current_item.toolTip()
        event = self.event_presenter.get_event_via_tool_tip(id)
        item_to_delete = self.list_events.takeItem(self.list_events.currentRow())
        # Сохранение изменений в файл
        self.event_presenter.delete_event_from_file(event)
        self.event_presenter.delete_event(event)
        self.clear_tuple_lines()
        # print(self.event_presenter.get_events())
        self.info_view.setText('Событие удалено.')

    def calendar_day_changed(self):
        if self.editing_enabled:
            self.date_start_line.setDate(self.calendar.selectedDate())
            self.date_end_line.setDate(self.calendar.selectedDate())
        else:
            events = self.event_presenter.get_events_via_qdate(self.calendar.selectedDate())
            # print(self.calendar.selectedDate())
            # self.calendar.showSelectedDate()
            # print(events)
            self.fill_list_events_with(events)

    def fill_list_events_with(self, events):
        if events:
            self.info_view.setText('Загружены новые события.')
            self.list_events.clear()
            for event in events:
                event_str = self.event_presenter.get_event_to_str_via_tool_tip(event.id)
                self.item = QListWidgetItem()
                self.item.setText(event_str.strip())
                self.item.setToolTip(event.id)
                self.list_events.addItem(self.item)
        else:
            self.info_view.setText('Событий на этот день не найдено.')

    def the_all_events_button_was_clicked(self):
        self.list_events.clear()
        for event in self.event_presenter.model.events:
            event_str = self.event_presenter.get_event_to_str_via_tool_tip(event.id)
            self.item = QListWidgetItem()
            self.item.setText(event_str.strip())
            self.item.setToolTip(event.id)
            self.list_events.addItem(self.item)

    def the_import_button_was_clicked(self):
        print("Import button was clicked.")
        # Тут надо вызов диалогого окна
        dialog_import = QFileDialog(self)
        dialog_import.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog_import.setNameFilter("Календарь (*.ics)")
        if os.path.exists(r"D:\Download\ilia.lad@mail.ru.ical (2)"):
            dialog_import.setDirectory(r"D:\Download\ilia.lad@mail.ru.ical (2)")
        elif os.path.exists(r"C:"):
            dialog_import.setDirectory(r"C:")
        dialog_import.setViewMode(QFileDialog.ViewMode.Detail) # можно поэксперементировать
        if dialog_import.exec():
            file_to_import_path = dialog_import.selectedFiles()
            if file_to_import_path:
                path = Path(file_to_import_path[0])
                os.chdir(os.path.dirname(path))
                with open(os.path.basename(path), 'r', encoding='utf-8') as file_to_import:
                    # print(type(file_to_import))
                    # print(file_to_import)
                    # print(path)
                    self.event_presenter.import_calendar(file_to_import)
                    # file_to_import.close()
        pass

    def the_export_button_was_clicked(self):
        # print("Export button was clicked.")
        # print(self.event_presenter.get_events())
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить календарь", "C:", "Calendar (*.ics);; Text file (*.txt)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as import_file:
                self.event_presenter.export_calendar(import_file)

    def freeze_left(self, freeze=True):
        buttons = [self.button_export, self.button_import,
                   self.button_all_events, self.button_add_event,
                   self.button_delete_event, self.button_edit_event]
        # Возможно можно чутка улучшить
        if freeze:
            self.list_events.setEnabled(False)
            for widget in buttons:
                if not widget.isChecked():
                    widget.setEnabled(False)
        else:
            self.list_events.setEnabled(True)
            for widget in buttons:
                widget.setEnabled(True)

    def freeze_right(self, freeze=True):
        for widget in self.line_widget_tuple:
            widget.setEnabled(not freeze)

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
