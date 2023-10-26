from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self):
        self.start_times = []
        self.stop_times = []
        self.running = False
        self.paused = False  # Add a 'paused' attribute

    def start(self):
        if not self.running:
            self.start_times.append(datetime.now())
            self.running = True
            self.paused = False  # Reset 'paused' when starting

    def pause(self):
        if self.running:
            self.stop_times.append(datetime.now())
            self.running = False
            self.paused = True  # Set 'paused' to True when pausing

    def reset(self):
        self.start_times = []
        self.stop_times = []
        self.running = False
        self.paused = False  # Reset 'paused' when resetting

    def elapsed_times(self):
        elapsed_times = []
        for start_time, stop_time in zip(self.start_times, self.stop_times):
            elapsed_times.append(stop_time - start_time)
        return elapsed_times
