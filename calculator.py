import tkinter as tk
from tkinter import messagebox

# Function to update the display when a button is pressed
def press_button(value):
    current = display.get()
    display.set(current + str(value))

# Function to evaluate the expression on the display
def calculate():
    try:
        result = eval(display.get())
        display.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to clear the display
def clear_display():
    display.set("")

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x550")
root.config(bg="lightblue")

# Create a StringVar to hold the value of the display
display = tk.StringVar()

# Create the display area (entry widget)
display_area = tk.Entry(root, textvariable=display, font=("Arial", 24), bd=10, relief="sunken", justify="right", bg="lightgreen", fg="black")
display_area.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Create button values and their respective actions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Loop through button definitions and create them
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="orange", fg="white", command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="red", fg="white", command=clear_display)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), bg="lightblue", fg="black", command=lambda value=text: press_button(value))
    
    button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

# Make the grid rows and columns resize dynamically
for i in range(6):
    root.grid_rowconfigure(i, weight=1, minsize=80)  # Set minimum size for each row
for i in range(4):
    root.grid_columnconfigure(i, weight=1, minsize=80)  # Set minimum size for each column

# Start the main event loop
root.mainloop()
