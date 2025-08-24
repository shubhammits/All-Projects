import tkinter as tk
from tkinter import messagebox

# Initial balance
balance = 1000

# Functions
def check_balance():
    messagebox.showinfo("Balance", f"Your balance is: ₹{balance}")

def withdraw_money():
    global balance
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            messagebox.showwarning("Invalid", "Please enter a valid amount")
        elif amount > balance:
            messagebox.showwarning("Error", "Insufficient Balance")
        else:
            balance -= amount
            messagebox.showinfo("Success", f"₹{amount} Withdrawn Successfully!\nNew Balance: ₹{balance}")
            entry_amount.delete(0, tk.END)
    except:
        messagebox.showwarning("Error", "Enter a valid number")

def deposit_money():
    global balance
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            messagebox.showwarning("Invalid", "Please enter a valid amount")
        else:
            balance += amount
            messagebox.showinfo("Success", f"₹{amount} Deposited Successfully!\nNew Balance: ₹{balance}")
            entry_amount.delete(0, tk.END)
    except:
        messagebox.showwarning("Error", "Enter a valid number")

def exit_app():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("ATM Machine")
root.geometry("400x350")
root.config(bg="#2C3E50")

title = tk.Label(root, text="💳 ATM Machine", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50")
title.pack(pady=10)

frame = tk.Frame(root, bg="#34495E")
frame.pack(pady=20, padx=20, fill="both")

lbl = tk.Label(frame, text="Enter Amount:", font=("Arial", 12), bg="#34495E", fg="white")
lbl.pack(pady=5)

entry_amount = tk.Entry(frame, font=("Arial", 14))
entry_amount.pack(pady=5)

btn_balance = tk.Button(frame, text="Check Balance", font=("Arial", 12, "bold"), bg="#1ABC9C", fg="white", command=check_balance)
btn_balance.pack(pady=5, fill="x")

btn_withdraw = tk.Button(frame, text="Withdraw", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", command=withdraw_money)
btn_withdraw.pack(pady=5, fill="x")

btn_deposit = tk.Button(frame, text="Deposit", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", command=deposit_money)
btn_deposit.pack(pady=5, fill="x")

btn_exit = tk.Button(frame, text="Exit", font=("Arial", 12, "bold"), bg="#F39C12", fg="white", command=exit_app)
btn_exit.pack(pady=5, fill="x")

root.mainloop()
