# from tkinter import Tk
# import tkinter

# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH,expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame,text="Exit",command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()

class EventView:
    @staticmethod
    def display_program():
        pass

    def __init__(self, presenter):
        self.presenter = presenter

    def add_event_button_click(self, title, t_start, t_end):
        pass

    def delete_event_button_click(self, index):
        pass

    def edit_event_button_click(self, index, new_title, new_t_start, t_end):
        pass

    def update_events(self, events):
        pass
