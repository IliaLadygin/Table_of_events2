from Event import Event, EventFull

class EventPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
    def add_event(self, event):
        self.model.add(event)
    def delete_event_by_index(self, index):
        self.model.delete(index)
    def update_event_by_index(self, index, new_title, new_t_start, new_t_end):
        self.model.update(index, Event(new_title, new_t_start, new_t_end))
