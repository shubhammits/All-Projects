import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        tasks.remove(task)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete")

def clear_tasks():
    global tasks
    tasks = []
    update_listbox()

# GUI setup
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x400")
root.config(bg="#2C3E50")

# Title
title = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
title.pack(pady=10)

# Entry box
entry_task = tk.Entry(root, font=("Arial", 14))
entry_task.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#2C3E50")
btn_frame.pack(pady=5)

btn_add = tk.Button(btn_frame, text="Add Task", width=10, bg="#27AE60", fg="white", command=add_task)
btn_add.grid(row=0, column=0, padx=5)

btn_delete = tk.Button(btn_frame, text="Delete Task", width=10, bg="#E74C3C", fg="white", command=delete_task)
btn_delete.grid(row=0, column=1, padx=5)

btn_clear = tk.Button(btn_frame, text="Clear All", width=10, bg="#F39C12", fg="white", command=clear_tasks)
btn_clear.grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

root.mainloop()
