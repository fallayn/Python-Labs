import tkinter as tk

def solve():
    def button_click(button_text):
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text + button_text)

    def clear_display():
        display.delete(0, tk.END)

    def calculate():
        expression = display.get()
        try:
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    # Create the main window
    root = tk.Tk()
    root.title("Simple Calculator")

    root.geometry("400x300")

    # Create the display widget
    display = tk.Entry(root, width=30, font=("Arial", 14))
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Define button labels
    button_labels = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+",
        "C"  # Clear button
    ]

    # Create buttons
    row = 1
    col = 0
    for label in button_labels:
        if label == "=":
            tk.Button(root, text=label, width=10, command=calculate).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
        elif label == "C":
            tk.Button(root, text=label, width=5, command=clear_display).grid(row=row, column=col, padx=5, pady=5)
        else:
            tk.Button(root, text=label, width=5, command=lambda l=label: button_click(l)).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Run the Tkinter event loop
    root.mainloop()