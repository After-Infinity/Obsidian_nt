import tkinter as tk
import random

def generate_random_number():
    random_number = random.randint(100000, 999999)
    result_label.config(text=f"{random_number}")

# Create the main window
window = tk.Tk()
window.title("Random Number Generator")

# Create a label to display the random number
result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

# Create a button to generate a new random number
generate_button = tk.Button(window, text="Generate ", command=generate_random_number)
generate_button.pack()

# Set the window to always appear on top
window.wm_attributes("-topmost", 1)

# Run the Tkinter event loop
window.mainloop()
