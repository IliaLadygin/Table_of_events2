from Event import EventFull
from EventModel import EventModel
from EventPresenter import EventPresenter
from EventView import EventView

# Создаем несколько заметок
# Добавить чтение событий из файла
events = [EventFull("Event 1", "20230404", "20230604", note="This is just a note"), EventFull("Event 2", "20230405", "20230407")]
# Создаем модель заметок
event_model = EventModel(events)
# Создаем Presenter для заметок и связываем его с View и Model
event_presenter = EventPresenter(EventView(EventPresenter), event_model)
print(event_presenter.model.get_events())
# Добавляем новую заметку
event_presenter.add_event(EventFull("Event 3", "20230204", "20230604"))
print(*event_presenter.model.get_events(), sep="\n")
# Удаляем заметку
event_presenter.delete_event_by_index(0)
print(event_presenter.model.get_events())
# Выводим все события на экран
print(event_presenter.model.get_events())
print(5)
print("FixBrainDeads")
print("FixBrainDeads2")
print("FixBrainDeads3")
