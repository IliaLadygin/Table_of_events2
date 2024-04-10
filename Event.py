class Event:
    def __init__(self, title, date_start, date_end, time_start, time_end):
        self.title = title
        self.date_start = date_start
        self.date_end = date_end
        self.time_start = time_start
        self.time_end = time_end


class EventFull(Event):
    def __init__(self, title, date_start, date_end, time_start, time_end, note=None, place=None, hyperlink=None):
        super().__init__(title, date_start, date_end, time_start, time_end)
        self.note = note
        self.place = place
        self.hyperlink = hyperlink
        # Додумать доп штуки
