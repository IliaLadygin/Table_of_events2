from Event import EventFull
from EventModel import EventModel
from EventPresenter import EventPresenter
from EventView import EventView, MainWindow
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

# Илья
# GUI

# Вика
# База данных

# Создаем несколько заметок
# Добавить чтение событий из файла
events = []
# Создаем модель заметок
event_model = EventModel(events)
# Создаем Presenter для заметок и связываем его с View и Model
event_presenter = EventPresenter(EventView(EventPresenter), event_model)
# print(event_presenter.model.get_events())
# Импортируем календарь, если он существует
event_presenter.import_calendar('my_calendar.ics')
# Добавляем первую заметку, если не было создано ранее
event_presenter.first_note('my_calendar.ics')
# print(*event_presenter.model.get_events(), sep="\n")
# Удаляем заметку
# event_presenter.delete_event_by_index(0)
# print(event_presenter.model.get_events())
# Выводим все события на экран
# print(event_presenter.model.get_events())
# print(event_presenter.get_beauty_event_date())
print("Starting GUI...")
app = QApplication(sys.argv)
window = MainWindow(event_presenter)
window.show()
app.exec()
event_presenter.export_calendar('my_calendar.ics')
print("GUI was closed successfully.")