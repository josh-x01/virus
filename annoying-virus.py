import tkinter as tk
import random
import threading
import numpy as np
import psutil 

def create_large_array():
    # Define the size of the array (in bytes)
    array_size_bytes = 5 * 1024 * 1024 * 1024  # 5GB

    # Create a NumPy array of zeros (dtype=int32)
    large_array = np.zeros(array_size_bytes // 4, dtype=np.int32)

    # Fill the array with some data (for demonstration purposes)
    for i in range(len(large_array)):
        large_array[i] = i

    # Print memory usage (optional)
    process = psutil.Process(os.getpid())
    print(f"Memory used: {process.memory_info().rss / (1024 * 1024):.2f} MB")


def create_large_array_thread():
    threading.Thread(target=create_large_array).start()

def on_ok_button_click():
    label.config(text="OK Button Clicked!")


def on_exit_button_click():
    create_new_gui()


def create_new_gui():
    new_root = tk.Tk()

    # Generate a random title
    random_title = generate_random_title()
    new_root.title(random_title)

    # Set the initial width and height
    initial_width = 400
    initial_height = 300
    new_root.geometry(f"{initial_width}x{initial_height}")

    # Add a label to the window with padding
    new_label = tk.Label(new_root, text="Hello, GUI!",
                         padx=10, pady=10, bg="white")
    new_label.pack()

    # Add Exit button, make it white, align it to the left with padding
    new_exit_button = tk.Button(
        new_root, text="Exit", command=create_new_gui, bg="white", padx=10, pady=5)
    new_exit_button.pack(side=tk.LEFT, padx=5)

    # Add OK button, make it white, align it to the right with padding
    new_ok_button = tk.Button(new_root, text="OK", command=lambda: new_label.config(
        text="OK Button Clicked!"), bg="white", padx=10, pady=5)
    new_ok_button.pack(side=tk.RIGHT, padx=5)

    # Bind the window close event to on_close function
    new_root.protocol("WM_DELETE_WINDOW", on_close)

    # Start a thread to perform more resource-intensive tasks
    threading.Thread(target=resource_intensive_tasks,
                     args=(new_label,), daemon=True).start()

    # Run the main event loop for the new GUI
    create_large_array_thread()
    new_root.mainloop()


def on_close():
    create_new_gui()


def generate_random_title():
    adjectives = ["Fantastic", "Amazing",
                  "Awesome", "Incredible", "Spectacular"]
    nouns = ["Virus", "App", "Project", "GUI", "Experiment"]

    random_title = f"{random.choice(adjectives)} {random.choice(nouns)}"
    return random_title


def resource_intensive_tasks(label):
    while True:
        # Perform more resource-intensive tasks
        result = 0
        store = []
        for _ in range(100000):
            result += random.random()
            store.append(result)

        # Update the label with the result
        label.config(text=f"Calculating stars: {result}")


# Create the main window
root = tk.Tk()

# Set the window title
root.title("My GUI Application")

# Set the initial width and height
initial_width = 400
initial_height = 300
root.geometry(f"{initial_width}x{initial_height}")

# Add a label to the window with padding
label = tk.Label(root, text="Hello, GUI!", padx=10, pady=10, bg="white")
label.pack()

# Add Exit button, make it white, align it to the left with padding
exit_button = tk.Button(
    root, text="Exit", command=on_exit_button_click, bg="white", padx=10, pady=5)
exit_button.pack(side=tk.LEFT, padx=5)

# Add OK button, make it white, align it to the right with padding
ok_button = tk.Button(
    root, text="OK", command=on_ok_button_click, bg="white", padx=10, pady=5)
ok_button.pack(side=tk.RIGHT, padx=5)

# Bind the window close event to on_close function
root.protocol("WM_DELETE_WINDOW", on_close)

# Run the main event loop
root.mainloop()
