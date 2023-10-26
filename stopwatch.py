from datetime import datetime, timedelta

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
