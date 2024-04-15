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
