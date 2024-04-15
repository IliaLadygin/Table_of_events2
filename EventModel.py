class EventModel:
    def __init__(self, events):
        self.events = events

    def add(self, event):
        self.events.append(event)

    def delete(self, index):
        del self.events[index]

    def update(self, index, new_event):
        self.events[index] = new_event

    def get_events(self):
        return [str(self.events[i].title) +
                ": Date start = " + str(self.events[i].date_start) +
                " Date end = " + str(self.events[i].date_end) +
                ": Time start = " + str(self.events[i].time_start) +
                " Time end = " + str(self.events[i].time_end)for i in range(len(self.events))]

    @staticmethod
    def get_beauty_date(event):
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
        beauty_date = ""
        if event.date_start == event.date_end:
            beauty_date += str(int(event.date_start[7:])) + " " + months[event.date_start[5:7]]
        else:
            beauty_date += (str(int(event.date_start[7:])) + " " + months[event.date_start[5:7]] +
                            " - " + str(int(event.date_end[7:])) + " " + months[event.date_end[5:7]])
        return beauty_date

    @staticmethod
    def get_beauty_time(event):
        return event.time_start[0:2] + ":" + event.time_start[2:] + "-" + event.time_end[0:2] + ":" + event.time_end[2:]

    @staticmethod
    def get_event_as_dict(event):
        event_dict = {}
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
