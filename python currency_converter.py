import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to fetch live rates
def fetch_rates(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("result") == "success":
            return data["rates"]
        else:
            messagebox.showerror("Error", f"Failed to fetch rates!\n{data.get('error-type')}")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"API Error: {e}")
        return None

# Convert function
def convert_currency():
    try:
        amount = float(amount_entry.get())
        src = source_currency.get()
        tgt = target_currency.get()

        rates = fetch_rates(src)
        if rates and tgt in rates:
            converted = amount * rates[tgt]
            result_label.config(text=f"{amount} {src} = {converted:.2f} {tgt}")
        else:
            messagebox.showerror("Error", "Target currency not found!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# GUI setup
root = tk.Tk()
root.title("🌍 Currency Converter")
root.geometry("400x300")

title = tk.Label(root, text="💱 Currency Converter", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Currency dropdowns
currency_list = ["USD", "INR", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "NZD"]

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:").grid(row=0, column=0, padx=5)
source_currency = ttk.Combobox(frame, values=currency_list, width=10)
source_currency.set("USD")
source_currency.grid(row=0, column=1)

tk.Label(frame, text="To:").grid(row=0, column=2, padx=5)
target_currency = ttk.Combobox(frame, values=currency_list, width=10)
target_currency.set("INR")
target_currency.grid(row=0, column=3)

# Amount
tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Convert button
convert_btn = tk.Button(root, text="Convert", command=convert_currency, bg="lightblue")
convert_btn.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
