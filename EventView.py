import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QListWidget


class MainWindow(QMainWindow):
    def __init__(self, event_presenter):
        super().__init__()
        self.setFixedSize(QSize(1000, 500)) # Задание стандартных размеров окна
        # self.n_times_clicked = 0
        self.setWindowTitle("Table of events") # Название окна
        self.button_add_event = QPushButton("Добавить событие")
        # self.button_add_event.clicked.connect(self.the_button_was_clicked)
        self.list_events = QListWidget()
        for event in event_presenter.model.events:
            event_dict = event_presenter.model.get_event_as_dict(event)
            # event_str = (event.title() + "\n" +
            #              event_presenter.get_beauty_event_date(event) + "\n" +
            #              event_presenter.get_beauty_event_time(event))
            event_str = ""
            for key, arg in event_dict.items():
                event_str += key + ": " + str(arg) + "\n"
            self.list_events.addItem(event_str)
        self.label_event_view = QLabel()  # показ текста или картинок

        # self.input = QLineEdit()  # Создание строки, в которую можно вводить данные
        # self.input.textChanged.connect(self.label.setText)  # textChanged - сигнал редактирования строки

        # Добавление слоя в которых располагаются виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.list_events)
        layout.addWidget(self.button_add_event)

        # Макет
        container = QWidget()
        container.setLayout(layout)
        # self.setMouseTracking(True) # должна обрабатывать движение мыши без нажатия, но не работает

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

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
