import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from stopwatch import Stopwatch

class StopwatchUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Stopwatch")
        self.stopwatch = Stopwatch()
        self.last_dialog_time = None
        self.create_ui()
        self.check_resume_timer()

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
        pause_button = tk.Button(self.window, text="Pause", command=self.pause_stopwatch)
        restart_button = tk.Button(self.window, text="Restart", command=self.restart_stopwatch)
        start_button.pack()
        pause_button.pack()
        restart_button.pack()

    def start_stopwatch(self):
        self.stopwatch.start()
        self.update_time()

    def pause_stopwatch(self):
        self.stopwatch.pause()
        self.update_time()
        self.last_dialog_time = datetime.now()

    def restart_stopwatch(self):
        if self.stopwatch.running:
            response = messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the stopwatch?")
            if response:
                self.stopwatch.reset()
                self.update_time()

    def check_resume_timer(self):
        if not self.stopwatch.running and self.stopwatch.paused and (
            not self.last_dialog_time or (datetime.now() - self.last_dialog_time).total_seconds() >= 2
        ):
            response = messagebox.askyesno("Resume Stopwatch", "Do you want to resume the stopwatch?")
            if response:
                self.stopwatch.start()
                self.update_time()
            self.last_dialog_time = datetime.now()

        self.window.after(1000, self.check_resume_timer)  # Start checking after the first pause

    def update_time(self):
        current_time = datetime.now()
        if self.stopwatch.running and self.stopwatch.start_times:
            elapsed_time = current_time - self.stopwatch.start_times[-1]
        else:
            elapsed_time = timedelta(seconds=0)

        total_elapsed = elapsed_time + sum(self.stopwatch.elapsed_times(), timedelta())
        time_str = self.format_timedelta(total_elapsed)

        self.time_label.config(text=time_str)
        self.start_time_display.config(text=f"Start Time: {self.format_datetime(self.stopwatch.start_times)}")
        self.stop_time_display.config(text=f"Stop Time: {self.format_datetime(self.stopwatch.stop_times)}")

        self.time_label.after(1000, self.update_time)

    def format_datetime(self, dt_list):
        if not dt_list:
            return ""
        return "\n".join([dt.strftime('%Y-%m-%d %I:%M:%S') for dt in dt_list])

    def format_timedelta(self, td):
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
