import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.running = False

    def start(self):
        self.start_time = datetime.now()
        self.running = True

    def stop(self):
        self.stop_time = datetime.now()
        self.running = False

    def reset(self):
        self.start_time = None
        self.stop_time = None
        self.running = False

    def elapsed_time(self):
        if self.running:
            current_time = datetime.now()
            elapsed_time = current_time - self.start_time
        else:
            elapsed_time = self.stop_time - self.start_time if self.start_time else timedelta()
        return elapsed_time

class StopwatchUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Stopwatch")
        self.stopwatch = Stopwatch()
        self.create_ui()

    def create_ui(self):
        self.create_labels()
        self.create_buttons()
        self.update_time()

    def create_labels(self):
        self.time_label = tk.Label(self.window, text="00:00:00", font=("Arial", 40))
        self.time_label.pack()
        self.start_time_display = tk.Label(self.window, text="Start Time: ", font=("Arial", 12))
        self.start_time_display.pack()
        self.stop_time_display = tk.Label(self.window, text="Stop Time: ", font=("Arial", 12))
        self.stop_time_display.pack()

    def create_buttons(self):
        start_button = tk.Button(self.window, text="Start", command=self.start_stopwatch)
        stop_button = tk.Button(self.window, text="Stop", command=self.stop_stopwatch)
        restart_button = tk.Button(self.window, text="Restart", command=self.restart_stopwatch)
        start_button.pack()
        stop_button.pack()
        restart_button.pack()

    def start_stopwatch(self):
        self.stopwatch.start()
        self.update_time()

    def stop_stopwatch(self):
        self.stopwatch.stop()
        self.update_time()

    def restart_stopwatch(self):
        if self.stopwatch.running:
            response = messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the stopwatch?")
            if response:
                self.stopwatch.reset()
                self.update_time()

    def update_time(self):
        elapsed_time = self.stopwatch.elapsed_time()
        time_str = self.format_timedelta(elapsed_time)
        self.time_label.config(text=time_str)
        self.start_time_display.config(text=f"Start Time: {self.format_datetime(self.stopwatch.start_time)}")
        self.stop_time_display.config(text=f"Stop Time: {self.format_datetime(self.stopwatch.stop_time)}")
        self.time_label.after(100, self.update_time)

    @staticmethod
    def format_timedelta(td):
        seconds = int(td.total_seconds())
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    @staticmethod
    def format_datetime(dt):
        return dt.strftime('%Y-%m-%d %I:%M:%S') if dt else ""

if __name__ == '__main__':
    window = tk.Tk()
    app = StopwatchUI(window)
    window.mainloop()
