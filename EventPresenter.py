from Event import Event, EventFull
from PyQt6.QtCore import QDateTime


class EventPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_event(self, event: EventFull):
        print(self.model.add_new_event(event))

    def get_event_via_tool_tip(self, tool_tip: str):
        return self.model.get_event_via_tool_tip(tool_tip)

    def get_event_to_str_via_tool_tip(self, tool_tip: str):
        return self.model.get_event_to_str_via_tool_tip(tool_tip)

    def get_event_to_str(self, event: EventFull):
        # print('.')
        return self.model.event_to_str(event)

    def save_new_event_to_file(self, event: EventFull):
        return self.model.save_event_to_file(event)

    def delete_event_from_file(self, event: EventFull):
        return self.model.del_event_from_file(event)

    def edit_event_in_file(self, event: EventFull):
        return self.model.edit_event_to_file(event)

    def delete_event_by_index(self, index):
        self.model.delete(index)

    def delete_event(self, event: EventFull):
        self.model.del_event(event)

    def update_event_by_index(self, index, new_title, new_t_start, new_t_end):
        self.model.update(index, Event(new_title, new_t_start, new_t_end))

    def get_beauty_event_date(self, event: EventFull):
        self.model.get_beauty_date(self, event)

    def create_id(self, title: str, date: QDateTime, time: QDateTime):
        return title + date.toString('yyyyMMdd') + time.toString('hhmmss')

    def get_beauty_event_time(self, event: EventFull):
        self.model.get_beauty_time(self, event)

    def get_events(self):
        return self.model.get_events()

    def get_event_as_dict(self, event: EventFull):
        return self.model.get_event_as_dict(event)
