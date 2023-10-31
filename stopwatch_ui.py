import tkinter as tk
from tkinter import messagebox

from datetime import datetime, timedelta
from stopwatch import Stopwatch
from fileUtils import *

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
        self.create_textfield()
        self.create_text_list()
        self.update_time()

    def create_labels(self):
        self.time_label = tk.Label(self.window, text="00:00:00:00", font=("Arial", 40))
        self.time_label.pack()

    def create_buttons(self):
        start_button = tk.Button(self.window, text="Start", command=self.start_stopwatch)
        pause_button = tk.Button(self.window, text="Pause", command=self.pause_stopwatch)
        restart_button = tk.Button(self.window, text="Restart", command=self.restart_stopwatch)

        title_label = tk.Label(self.window, text="Title:", font=("Arial", 12))
        self.title_entry = tk.Entry(self.window, font=("Arial", 12))  
        title_label.pack()
        self.title_entry.pack()

        start_button.pack()
        pause_button.pack()
        restart_button.pack()


    def create_textfield(self):
        dialog_interval_label = tk.Label(self.window, text="Dialog Interval:", font=("Arial", 12))
        dialog_interval_label.pack()

        self.dialog_minutes_entry = tk.Entry(self.window, font=("Arial", 12))
        self.dialog_seconds_entry = tk.Entry(self.window, font=("Arial", 12))
        minutes, seconds = read_dialog_interval()
        self.dialog_minutes_entry.insert(0, minutes)
        self.dialog_seconds_entry.insert(0, seconds)

        self.dialog_minutes_entry.pack()
        self.dialog_seconds_entry.pack()

        self.unit_selection = tk.StringVar()
        self.unit_selection.set("minutes")  # Set a default value
        units_label = tk.Label(self.window, text="Units:", font=("Arial", 12))
        units_label.pack()


        self.dialog_minutes_entry.bind("<Return>", self.save_interval)
        self.dialog_seconds_entry.bind("<Return>", self.save_interval)


    def create_text_list(self):
        self.text_list = tk.Listbox(self.window, font=("Arial", 12), width=50, height=10)
        self.text_list.pack()

    def start_stopwatch(self):
        self.stopwatch.start()
        self.update_time()

    def pause_stopwatch(self):
        if  self.stopwatch.running:
            title = self.title_entry.get()
            start_time = self.stopwatch.start_times[-1]
            stop_time = datetime.now()
            self.stopwatch.add_title(title, start_time, stop_time)
            self.display_titles() 
            self.stopwatch.pause()
            self.update_time()
            self.last_dialog_time = datetime.now()

    def restart_stopwatch(self):
        self.pause_stopwatch()
        response = messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the stopwatch?")
        if response:
            self.stopwatch.reset()
            self.update_time()

    def display_titles(self):
        self.text_list.delete(0, tk.END)  # Clear the existing list
        titles = self.stopwatch.get_titles()
        for title, start, stop in titles:
            formatted_text = f"{title}: {self.format_datetime([start])} - {self.format_datetime([stop])}"
            self.text_list.insert(tk.END, formatted_text)

    def check_resume_timer(self):
        interval_minutes, interval_seconds = read_dialog_interval()
        interval_seconds += interval_minutes * 60  # Convert minutes to seconds
        if not self.stopwatch.running and self.stopwatch.paused and (
            not self.last_dialog_time or (datetime.now() - self.last_dialog_time).total_seconds() >= interval_seconds
        ):
            response = messagebox.askyesno("Resume Stopwatch", "Do you want to resume the stopwatch?")
            if response:
                self.stopwatch.start()
                self.update_time()
            self.last_dialog_time = datetime.now()

        self.window.after(1000, self.check_resume_timer)


    def update_time(self):
            total_elapsed = self.stopwatch.calculate_total_elapsed()
            time_str = self.format_timedelta(total_elapsed)
            self.time_label.config(text=time_str)
            self.time_label.after(10, self.update_time)

    def format_datetime(self, dt_list):
        if not dt_list:
            return ""
        return "\n".join([dt.strftime('%I:%M') for dt in dt_list])

    def format_timedelta(self, td):
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int((td.microseconds + seconds * 10 ** 6) / 10 ** 4)
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds//10:02}"


    def save_interval(self, _):
        try:
            minutes = int(self.dialog_minutes_entry.get())
            seconds = int(self.dialog_seconds_entry.get())
            save_dialog_interval(minutes,seconds)
            messagebox.showinfo("Save Successful", "Dialog interval saved successfully!")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for minutes and seconds.")

