# Function to read the time dialog interval from a file
def read_dialog_interval():
    try:
        with open("dialog_interval.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 3  # Default value if the file doesn't exist or is invalid

# Function to save the time dialog interval to a file
def save_dialog_interval(interval):
    with open("dialog_interval.txt", "w") as file:
        file.write(str(interval))
    messagebox.showinfo("Save Successful", "Dialog interval saved successfully!")