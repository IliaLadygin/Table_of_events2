class Event:
    def __init__(self, title, t_start, t_end):
        self.title = title
        self.t_start = t_start
        self.t_end = t_end

class EventFull(Event):
    def __init__(self, title, t_start, t_end, note=None, place=None, hyperlink=None):
        super().__init__(title, t_start, t_end)
        self.note = note
        self.place = place
        self.hyperlink = hyperlink
