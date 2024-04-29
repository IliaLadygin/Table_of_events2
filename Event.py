class Event:
    def __init__(self, id, title, date_start, date_end, time_start, time_end):
        self.id = id
        self.title = title
        self.date_start = date_start
        self.date_end = date_end
        self.time_start = time_start
        self.time_end = time_end


class EventFull(Event):
    def __init__(self, id, title, date_start, date_end, time_start, time_end, note='', place='', hyperlink=''):
        super().__init__(id, title, date_start, date_end, time_start, time_end)
        self.note = note
        self.place = place
        self.hyperlink = hyperlink
        # Додумать доп штуки

    @staticmethod
    def print_event(event):
        print(event.id, event.title, event.date_start, event.date_end, event.time_start, event.time_end, event.note, event.place, event.hyperlink, sep="\n")

    def print(self):
        print(self.id, self.title, self.date_start, self.date_end, self.time_start, self.time_end, self.note, self.place, self.hyperlink, sep="\n")