import tkinter as tk
import csv
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x400")

# Variables
item_var = tk.StringVar()
item_price_var = tk.StringVar()
category_var = tk.StringVar()

def adding_expense():
    item = item_var.get()
    item_price = item_price_var.get()
    category = category_var.get()

    if item == "" or item_price == "" or category == "":
        messagebox.showerror("Error", "Please fill all fields!")
        return

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, item_price, category])

    # Clear entries
    item_var.set("")
    item_price_var.set("")
    category_var.set("")

    messagebox.showinfo("Success", "Expense added successfully!")

# Heading
tk.Label(root, text="Expense Tracker", font=("Arial", 25, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

# Item
tk.Label(root, text="Item", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=item_var).grid(row=1, column=1, padx=10, pady=10)

# Item Price
tk.Label(root, text="Item Price", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=item_price_var).grid(row=2, column=1, padx=10, pady=10)

# Category
tk.Label(root, text="Category", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=category_var).grid(row=3, column=1, padx=10, pady=10)

# Button
tk.Button(root, text="Add Expense", command=adding_expense, bg="blue", fg="white", width=15).grid(row=4, column=1, pady=20)

root.mainloop()