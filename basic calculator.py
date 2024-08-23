import tkinter as tk
from tkinter import messagebox

# Function to process the mathematical expression
def process_expression(expression):
    try:
        # Evaluate the expression and update the display
        result = str(eval(expression))
        display_var.set(result)
    except Exception as error:
        # Show an error message if the input is invalid
        messagebox.showerror("Error", f"Input Error: {error}")
        display_var.set("")

# Function to add characters to the expression
def add_to_expression(character):
    current_expression = display_var.get()
    updated_expression = current_expression + character
    display_var.set(updated_expression)

# Function to clear the current display
def clear_expression():
    display_var.set("")

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# StringVar to store the text displayed on the calculator screen
display_var = tk.StringVar()

# Entry widget to display the expression/result
display_field = tk.Entry(app, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
display_field.grid(row=0, column=0, columnspan=4)

# Button layout for the calculator
button_data = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('Clear', 5, 0)
]

# Create and position the buttons dynamically
for (label, row, col) in button_data:
    if label == '=':
        button = tk.Button(app, text=label, padx=30, pady=20, font=("Arial", 18),
                           command=lambda: process_expression(display_var.get()))
    elif label == 'Clear':
        button = tk.Button(app, text=label, padx=30, pady=20, font=("Arial", 18),
                           command=clear_expression)
    else:
        button = tk.Button(app, text=label, padx=30, pady=20, font=("Arial", 18),
                           command=lambda label=label: add_to_expression(label))
    button.grid(row=row, column=col)

# Run the main application loop
app.mainloop()
