import tkinter as tk
from stopwatch_ui import StopwatchUI

if __name__ == '__main__':
    window = tk.Tk()
    app = StopwatchUI(window)
    window.mainloop()
