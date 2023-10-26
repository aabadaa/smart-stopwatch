import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox  # Import messagebox from tkinter

window = tk.Tk()
window.title("Stopwatch")

start_time = None
stop_time = None
running = False

start_time_display = tk.Label(window, text="Start Time: ", font=("Arial", 12))
start_time_display.pack()
stop_time_display = tk.Label(window, text="Stop Time: ", font=("Arial", 12))
stop_time_display.pack()

def start_stopwatch():
    global start_time, running
    start_time = datetime.now()
    running = True
    update_time()

def stop_stopwatch():
    global stop_time, running
    if running:
        stop_time = datetime.now()
        running = False
        stop_time_display.config(text=f"Stop Time: {stop_time.strftime('%Y-%m-%d %I:%M:%S')}")

def restart_stopwatch():
    global start_time, stop_time, running
    if running:
        stop_stopwatch()
    confirm_restart = messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the stopwatch?")
    if confirm_restart:
        start_time = None
        stop_time = None
        running = False
        start_time_display.config(text="Start Time: ")
        stop_time_display.config(text="Stop Time: ")
        time_label.config(text="00:00:00")

time_label = tk.Label(window, text="00:00:00", font=("Arial", 40))
time_label.pack()

start_button = tk.Button(window, text="Start", command=start_stopwatch)
stop_button = tk.Button(window, text="Stop", command=stop_stopwatch)
restart_button = tk.Button(window, text="Restart", command=restart_stopwatch)

start_button.pack()
stop_button.pack()
restart_button.pack()

def format_timedelta(td):
    if td is None:
        return "00:00:00"
    seconds = int(td.total_seconds())
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def update_time():
    if running:
        if start_time is not None:
            elapsed_time = datetime.now() - start_time
        else:
            elapsed_time = timedelta()
    else:
        if start_time is not None and stop_time is not None:
            elapsed_time = stop_time - start_time
        else:
            elapsed_time = timedelta()
    time_str = format_timedelta(elapsed_time)
    time_label.config(text=time_str)

    # Update start time continuously to show the running time
    if start_time is not None:
        start_time_display.config(text=f"Start Time: {start_time.strftime('%Y-%m-%d %I:%M:%S')}")
    time_label.after(100, update_time)

window.mainloop()
