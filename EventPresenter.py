from Event import Event, EventFull
from PyQt6.QtCore import QDateTime, QDate
import icalendar


class EventPresenter:
    date_format = 'dd.MM.yyyy'

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
        return self.model.event_to_str(event)

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

    def get_events_via_qdate(self, date: QDate):
        events = self.model.get_all_events_as_list()
        events_to_return = []
        for event in events:
            if ''.join(event.date_start.split('.')[::-1]) <= date.toString("yyyyMMdd") <= ''.join(event.date_end.split('.')[::-1]):
                events_to_return.append(event)
        return events_to_return

    def is_dates_valid(self, date_start: QDate, date_end: QDate, time_start: QDate, time_end: QDate) -> bool:
        print(date_start.toString('yyyyMMdd') + time_start.toString('hhmm'), date_end.toString('yyyyMMdd') + time_end.toString('hhmm'))
        return date_start.toString('yyyyMMdd') + time_start.toString('hhmm') <= date_end.toString('yyyyMMdd') + time_end.toString('hhmm')

    def import_calendar(self, path: str):
        self.model.import_calendar(path)

    def export_calendar(self, path: str):
        self.model.export_calendar(path)

    def add_event_in_calendar_file(self, event: EventFull, cal: icalendar.Calendar):
        self.model.add_event_in_calendar(event, cal)

    def first_note(self, path: str):
        self.model.first_note(path)