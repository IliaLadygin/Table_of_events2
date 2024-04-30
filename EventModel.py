from Event import EventFull


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

    def del_event_from_file(self, event: EventFull):
        print("Deleting event from file (not worked)")

    def update(self, index: int, new_event: EventFull):
        self.events[index] = new_event

    def get_events(self):
        return [str(self.events[i].title) +
                ": Date start = " + str(self.events[i].date_start) +
                " Date end = " + str(self.events[i].date_end) +
                ": Time start = " + str(self.events[i].time_start) +
                " Time end = " + str(self.events[i].time_end)for i in range(len(self.events))]

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

    def save_event_to_file(self, event: EventFull):
        print("Saving event to file... (not worked)")

    def edit_event_to_file(self, event: EventFull):
        print("Editing event to file... (not worked)")