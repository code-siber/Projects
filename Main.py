# Expense Tracker (Simplified Version)

import csv
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("""
    ========== Expense Tracker ==========
    1. Add Expense
    2. Show All Expenses
    3. Remove Expense
    4. Filter by Category
    5. Clear All Expenses
    6. Total Price of All Expenses
    7. Total Number of Items Sold
    8. Exit
    """)

# --- Add Expense ---
def add_expense():
    name = input("Enter name: ")
    category = input("Enter category (bag, shoes, clothing, accessories): ").lower()
    amount = int(input("Enter amount: "))
    description = input("Enter description: ")

    company = input("Enter company: ").lower()

    info = "not found"
    # Price rules
    if category == "bag":
        if company == "gucci":
            cost = amount * 100000 
    elif category == "shoes":
        if company == "nike":
            cost = amount * 50000
    elif category == "clothing":
        if company == "adidas":
            cost = amount * 20000
    elif category == "accessories":
        if company == "michael kors":
            cost = amount * 10000
    if company not in ["gucci", "nike", "adidas", "michael kors"]:
        print("Company not found!")
        return
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, category, company, amount, cost, description])

    print("Expense added successfully!")
    time.sleep(1)
    clear()

# --- Show All ---
def show_all():
    print("Name\tCategory\t Company\tAmount\tCost\tDescription")
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row != "":
                print("\t".join(row))
    input("\nPress Enter to return...")
    clear()

# --- Remove Expense ---
def remove_expense():
    target = input("Enter name to remove: ")
    rows = []
    found = False

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() != target.lower():
                rows.append(row)
            else:
                found = True

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Expense removed!" if found else "Expense not found!")
    time.sleep(1)
    clear()

# --- Filter by Category ---
def filter_by_category():
    category = input("Enter category to filter: ").lower()
    found = False
    print(f"\nItems in category '{category}':")
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1].lower() == category:
                print("\t".join(row))
                found = True
    if not found:
        print("No items found in this category.")
    input("\nPress Enter to return...")
    clear()

# --- Total Items ---
def total_items():
    total = 0
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                total += int(row[3])
    print(f"Total number of items sold: {total}")
    input("\nPress Enter to return...")
    clear()

# --- Total Price ---
def total_price():
    total = 0
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                total += float(row[4])
    print(f"Total price of all expenses: {total}")
    input("\nPress Enter to return...")
    clear()

# --- Clear All ---
def clear_file():
    open("expenses.csv", "w").close()
    print("All data cleared!")
    time.sleep(1)
    clear()

# --- Main Loop ---
def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all()
        elif choice == "3":
            remove_expense()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            clear_file()
        elif choice == "6":
            total_price()
        elif choice == "7":
            total_items()
        elif choice == "8":
            print("Exiting... Goodbye!")
            time.sleep(1)
            clear()
            break
        else:
            print("Invalid choice! Try again.")
            time.sleep(1)
            clear()

main()
