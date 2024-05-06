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
events = [EventFull("123","Event 1", "04.05.2024", "04.05.2024", "13:00", "14:00", note="This is just a note"),
          EventFull("124", "Event 2", "05.05.2024", "07.05.2024", "12:00", "14:00", note="This is", place="Wth")]
# Создаем модель заметок
event_model = EventModel(events)
# Создаем Presenter для заметок и связываем его с View и Model
event_presenter = EventPresenter(EventView(EventPresenter), event_model)
# print(event_presenter.model.get_events())
# Добавляем новую заметку
event_presenter.add_event(EventFull("125", "Event 3", "04.05.2024", "06.05.2024", "11:00", "16:00", hyperlink="www.google.com"))
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
print("GUI was closed successfully.")