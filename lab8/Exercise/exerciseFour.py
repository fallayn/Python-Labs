import tkinter as tk

def solve():
    exchange_rates = {
        "USD": {"EUR": 0.85, "GBP": 0.73},
        "EUR": {"USD": 1.18, "GBP": 0.86},
        "GBP": {"USD": 1.38, "EUR": 1.17}
    }

    # Function to perform currency conversion
    def convert_currency():
        try:
            source_currency = source_currency_var.get()
            target_currency = target_currency_var.get()
            amount = float(amount_entry.get())

            # Perform conversion
            result = amount * exchange_rates[source_currency][target_currency]

            # Update result label
            result_label.config(text="{:.2f} {}".format(result, target_currency))
        except ValueError:
            result_label.config(text="Invalid input")
        except KeyError:
            result_label.config(text="Exchange rate not found")

    # Create the main window
    root = tk.Tk()
    root.title("Currency Converter")

    # Source currency selection
    tk.Label(root, text="Source Currency:").grid(row=0, column=0)
    source_currency_var = tk.StringVar(root)
    source_currency_var.set("USD")  # Default value
    source_currency_option = tk.OptionMenu(root, source_currency_var, *exchange_rates.keys())
    source_currency_option.grid(row=0, column=1)

    # Amount entry
    tk.Label(root, text="Amount:").grid(row=1, column=0)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=1, column=1)

    # Target currency selection
    tk.Label(root, text="Target Currency:").grid(row=2, column=0)
    target_currency_var = tk.StringVar(root)
    target_currency_var.set("EUR")  # Default value
    target_currency_option = tk.OptionMenu(root, target_currency_var, *exchange_rates.keys())
    target_currency_option.grid(row=2, column=1)

    # Convert button
    convert_button = tk.Button(root, text="Convert", command=convert_currency)
    convert_button.grid(row=3, columnspan=2)

    # Result label
    result_label = tk.Label(root, text="")
    result_label.grid(row=4, columnspan=2)

    # Run the Tkinter event loop
    root.mainloop()