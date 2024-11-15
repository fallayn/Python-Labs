import tkinter as tk
from tkinter import messagebox

def solve():
    def say_hello():
        name = entry.get()
        if name:
            messagebox.showinfo("Greetings", "Hello, {}!".format(name))
        else:
            messagebox.showwarning("Warning", "Please enter your name.")

    # Create the main window
    root = tk.Tk()
    root.title("Say Hello!")

    #Set the size of the window
    root.geometry("600x300")

    # Create a label
    label = tk.Label(root, text="Enter your name:")
    label.pack()

    # Create an entry widget for user input
    entry = tk.Entry(root)
    entry.pack()

    # Create a button to trigger the greeting
    button = tk.Button(root, text="Say Hello", command=say_hello)
    button.pack()

    # Run the Tkinter event loop
    root.mainloop()