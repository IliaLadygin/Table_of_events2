from Event import EventFull
import icalendar
import os
from datetime import datetime


class EventModel:
    def __init__(self, events):
        self.events = events

    def add_new_event(self, event: EventFull):
        self.events.append(event)
        return "Event has been saved"

    def delete(self, index):
        del self.events[index]

    def del_event(self, event: EventFull):
        self.events.remove(event)

    # def del_event_from_file(self, event: EventFull):
        # print("Deleting event from file (not worked)")

    def update(self, index: int, new_event: EventFull):
        self.events[index] = new_event

    def get_events(self):
        return [str(self.events[i].title) +
                ": Date start = " + str(self.events[i].date_start) +
                " Date end = " + str(self.events[i].date_end) +
                ": Time start = " + str(self.events[i].time_start) +
                " Time end = " + str(self.events[i].time_end)for i in range(len(self.events))]

    def get_all_events_as_list(self):
        # print(list(self.events))
        return self.events

    @staticmethod
    def get_beauty_date(event: EventFull):
        months = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"}
        ddMMyyyy_start = tuple(event.date_start.split('.'))
        ddMMyyyy_end = tuple(event.date_end.split('.'))
        if ddMMyyyy_start == ddMMyyyy_end:
            beauty_date = str(int(ddMMyyyy_start[0])) + ' ' + months[ddMMyyyy_start[1]]
        else:
            beauty_date = str(int(ddMMyyyy_start[0])) + ' ' + months[ddMMyyyy_start[1]] + ' - ' + str(int(ddMMyyyy_end[0])) + ' ' + months[ddMMyyyy_end[1]]
        return beauty_date

    @staticmethod
    def get_beauty_time(event: EventFull):
        return event.time_start + " - " + event.time_end

    @staticmethod
    def get_event_as_dict(event: EventFull):
        event_dict = {}
        event_dict["ID"] = event.id
        event_dict["Название"] = event.title
        event_dict["Дата начала"] = event.date_start
        event_dict["Дата конца"] = event.date_end
        event_dict["Время начала"] = event.time_start
        event_dict["Время конца"] = event.time_end
        if event.note:
            event_dict["Пометка"] = event.note
        if event.place:
            event_dict["Место"] = event.place
        if event.hyperlink:
            event_dict["Гиперссылка"] = event.hyperlink
        return event_dict

    def get_event_via_tool_tip(self, tool_tip: str):
        for event in self.events:
            if event.id.lower() == tool_tip.lower():
                # print(tool_tip)
                # print(event.title)
                return event

    def event_to_str(self, event: EventFull):
        return event.title + "\n" + self.get_beauty_date(event) + "\n" + self.get_beauty_time(event) + ('', "\n" + event.place)[event.place != '']

    def get_event_to_str_via_tool_tip(self, tool_tip: str):
        for event in self.events:
            if event.id.lower() == tool_tip.lower():
                # print(tool_tip)
                # print(event.title)
                return event.title + "\n" + self.get_beauty_date(event) + "\n" + self.get_beauty_time(event) + ('', "\n" + event.place)[event.place != '']
        print("Error in get_event_via_tool_tip")
        raise Exception("Error in get_event_via_tool_tip")

    # def save_event_to_file(self, event: EventFull):
        # print("Saving event to file... (not worked)")

    # def edit_event_to_file(self, event: EventFull):
        # print("Editing event to file... (not worked)")
        
    def import_calendar(self, path):
        if os.path.exists(path) and path.endswith('.ics'):
            g = open(path,'rb')
            try:
                gcal = icalendar.Calendar.from_ical(g.read())
                for component in gcal.walk():
                    if component.name == "VEVENT":
                        dstart = component.get('dtstart').dt
                        dend = component.get('dtend').dt
                        event = EventFull(id=str(component.get('uid')), title=component.get('summary'), date_start=dstart.strftime('%d.%m.%Y'), 
                                      date_end=dend.strftime('%d.%m.%Y'), time_start=dstart.strftime('%H:%M'), 
                                      time_end=dend.strftime('%H:%M'), note=component.get('description') or '',
                                      place=component.get('location') or '', hyperlink=str(component.get('url')) or '')
                        self.add_new_event(event)
            except ValueError:
                print('Uncorrect file!')
            finally:
                g.close()
        
    def add_event_in_calendar(self, event: EventFull, cal: icalendar.Calendar):
        cal_event = icalendar.Event()
        cal_event.add('uid', event.id)
        cal_event.add('summary', event.title)
        cal_event.add('dtstart', datetime.strptime(event.date_start + event.time_start, '%d.%m.%Y%H:%M'))
        cal_event.add('dtend', datetime.strptime(event.date_end + event.time_start, '%d.%m.%Y%H:%M'))
        cal_event.add('location', event.place)
        cal_event.add('description', event.note)
        cal_event.add('url', event.hyperlink)
        
        cal.add_component(cal_event)
        
    def export_calendar(self, path: str):
        cal = icalendar.Calendar()
        cal.add('prodid', '-//Windows Calendar//')
        cal.add('version', '2.0')
        
        for event in self.events:
            self.add_event_in_calendar(event, cal)

        f = open(path, 'wb')
        f.write(cal.to_ical())
        f.close()
        
    def first_note(self, path: str):
        if len(self.events) == 0:
            event = EventFull("id", "Title", "01.01.2000", "01.01.2000", "00:00", "00:00",
                              note="Hello! Here you can write a description of your event. You can delete this note.",
                              place="You're in Calendar App", hyperlink="Here's hyperlink")
            self.add_new_event(event)