import tkinter as tk

def solve():

    def button_click():
        button.config(text = "Button clicked")

    #Create the mani window
    root = tk.Tk()
    root.title("Hello world!")

    #Set the size of the window
    root.geometry("600x600")

    # Add a button
    button = tk.Button(root, text="Click me", command=button_click)
    button.pack()

    # Run the Tkinter event loop
    root.mainloop()