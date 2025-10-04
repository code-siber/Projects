
# Expense Tracker

import os
import csv
import time

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def options():
    menu = """
    1. Add Expense
    2. Show All Expenses
    3. remove Expenses
    4. Filter by Category
    5. clear file
    6. total price of all expenses
    7. total number of expenses sold 
    8. Exit
    """
    return menu

def add_expense():
    try:
        name = str(input("Enter name: "))
        category = str(input("Enter category: "))
        amount = int(input("Enter amount: "))
        Cost = float(input("Enter cost: "))
        description = input("Enter description: ")
    except ValueError:
        print("""  
              
              Invalid input. Amount must be an integer and Cost must be a number.
              
                Redirecting to main menu...
              """)
        time.sleep(3)
        return


    with open("expenses.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, category, amount, Cost, description])

    print("Expense added successfully!")
    print("Redirecting to main menu...")
    time.sleep(2)
    screen_clear() 

def show_all_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        print("Name\tCategory\tAmount\tDescription")
        for row in reader:
            print("\t \t".join(row))
    input("Press Enter to return to the menu")
    print("Redirecting to main menu...")
    time.sleep(2)
    screen_clear()  # Wait for user to press Enter

def remove_expense():
            expence_to_remove = input("Name of the buyer you want to remove the expense to remove: ")
            rows = []
            try:
                if expence_to_remove == "":
                    raise ValueError("Expense name cannot be empty.")
            except:
                print("Invalid input. Please enter a valid expense name.")
                return
                    
            with open("expenses.csv", "r", newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] != expence_to_remove:
                        rows.append(row)
            with open("expenses.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            if expence_to_remove not in rows:
                print("""Expense not found. 
                ============try again===============""")
            else:
                print("Expense removed successfully!")
            input("Press Enter to return to the menu")
            print("Redirecting to main menu...")
            time.sleep(2)
            screen_clear()

def total_amount():
    tot = 0
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                tot += int(row[2])
    print(f"""
          ================Total number of expenses===============
          Total number of the sold expenses till date {time.timezone}: {tot}""")
    input("Press Enter to return to the menu ")
    print("Redirecting to main menu...")
    time.sleep(1)

def total_expenses():
    total = 0
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                total += float(row[3])
    print(f"""
          ================Total price of all expenses===============
          Total price of the sold expenses: {total}""")
    input("Press Enter to return to the menu ")
    print("Redirecting to main menu...")
    time.sleep(1)

def close():
    print("Exiting the program...")
    time.sleep(2)
    screen_clear()
    exit()

def choices(): 
    while True:
        print(options())
        choice = input("Enter your choice: ")
        screen_clear()
        if choice == "8":
            close()
        elif choice == "1":
            print("""
                  ================Add Item===============""")
            add_expense()

        elif choice == "2":
            show_all_expenses()

        elif choice == "3":
            print("""
                  ================Remove Item===============""")
            remove_expense()

        elif choice == "4":
            print("Filter by Category feature is not implemented yet.")

        elif choice == "5":
            open("expenses.csv", "w").close()
            print("All expenses cleared.")
            time.sleep(2)
            screen_clear()
        
        elif choice == "6":
            total_expenses()

        elif choice == "7":
            total_amount() 

        if not choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid choice. Please try again.")
        screen_clear()     
choices()
