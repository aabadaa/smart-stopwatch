
# Function to read the time dialog interval from a file
def read_dialog_interval():
    try:
        with open("dialog_interval.txt", "r") as file:
            data = file.read().strip().split()
            if len(data) == 2:
                minutes, seconds = int(data[0]), int(data[1])
                return minutes, seconds
    except (FileNotFoundError, ValueError, IndexError):
        return 3, 0  # Default values if the file doesn't exist or is invalid

# Function to save the time dialog interval to a file
def save_dialog_interval(minutes, seconds):
    with open("dialog_interval.txt", "w") as file:
        file.write(f"{minutes} {seconds}")
