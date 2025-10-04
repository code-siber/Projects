import csv

expenses = []  # List to hold expense dictionaries

# ------------------- Functions -------------------


def load_from_csv():
    
    pass

file = 'file.csv'
def save_to_csv():
    
    """Save expenses to expenses.csv"""
    pass


def add_expense():
    name_of_item = input("enter item name: ")
    price = float(input("enter price: "))
    amount = int(input("amunt of item: "))
    with open("file","a", newline='' ) as file1:
        writer = csv.writer(file1)
        writer.writerow([name_of_item, amount, price])
    
    """Take input and add new expense"""
    pass


def show_expenses():
    with open("file", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))
    input("enter ro exit")
    """Display all expenses"""
    pass


def total_expenses():
    with open("file", "r", newline="") as file:
        total = 0
        reader = csv.reader(file)
        for row in reader:
            if row[1]:
                total += float(row[1])
            print("the total expenses", total)
    """Calculate and display total expenses"""
    pass


def filter_by_category():
    """Filter expenses by category"""
    pass


def show_menu():
    print("""
    1. Add Expense
    2. Show All Expenses
    3. Show Total Expenses
    4. Filter by Category
    5. Save and Exit
    """)


# ------------------- Main Program -------------------

load_from_csv()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        filter_by_category()
    elif choice == "5":
        save_to_csv()
        print("Data saved. Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")