import time
import tkinter as tk
from threading import Thread, Event
import datetime


class App(tk.Tk):

    n_round = 1
    is_stopped = True
    elapsed_total = 0

    def __init__(self, *args, **kwargs):
        self.root = tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")
        self.title('TestApp')

        self.time_started = time.time()

        self.label = tk.Label(self.root, text="0", font=("MSゴシック", "60", "bold"))
        self.label.pack()

        self.start_button = tk.Button(self.root, text="start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="stop", command=self.stop)
        self.stop_button.pack()

        self.restart_button = tk.Button(self.root, text="reset", command=self.reset)
        self.restart_button.pack()

        self.event = Event()
        self.thread = Thread(target=self.update_label)

    def start(self):
        self.time_started = time.time()
        # self.label["text"] = 0.0
        self.start_update_label()
        self.is_stopped = False

    def stop(self):
        if self.is_stopped:
            return
        cur = time.time()
        elapsed = cur - self.time_started
        self.label["text"] = round(cur - self.time_started + self.elapsed_total, self.n_round)
        self.elapsed_total += elapsed
        self.stop_update_label()
        self.event.clear()
        self.is_stopped = True

    def start_update_label(self):
        self.thread = Thread(target=self.update_label)
        self.thread.start()

    def update_label(self):
        while not self.event.wait(0.1):
            cur = time.time()
            self.label["text"] = round(cur - self.time_started + self.elapsed_total, self.n_round)

    def reset(self):
        if not self.is_stopped:
            return
        tk.Label(self.root, text="record: {},  {}".format(self.label["text"], datetime.datetime.now())).pack()
        self.elapsed_total = 0
        self.label["text"] = 0

    def stop_update_label(self):
        self.event.set()


app = App()
app.mainloop()
