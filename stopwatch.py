from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self):
        self.running = False
        self.paused = False
        self.start_times = []
        self.stop_times = []
        self.titles = []  # List to store titles and their respective start and end times

    def start(self):
        if not self.running:
            self.start_times.append(datetime.now())
            self.running = True

    def pause(self):
        if self.running:
            self.stop_times.append(datetime.now())
            self.running = False
            self.paused = True

    def reset(self):
        self.running = False
        self.paused = False
        self.start_times = []
        self.stop_times = []
        self.titles = []  # Clear the titles when resetting

    def elapsed_times(self):
        elapsed = []
        for start, stop in zip(self.start_times, self.stop_times):
            elapsed.append(stop - start)
        return elapsed

    def add_title(self, title, start_time, stop_time):
        self.titles.append((title, start_time, stop_time))

    def get_titles(self):
        return self.titles