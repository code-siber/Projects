import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

# Main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("350x300")

root.resizable(width=False, height = False)
# Function to save data
def save_data():
    name = name_entry.get()
    gender = gender_var.get()
    course = course_combo.get()

    age_str = age_entry.get()
    if not name.isalpha():
        messagebox.showwarning("Invalid Name", "Please enter a valid name!")
        return
    if not age_str.isdigit():
        messagebox.showwarning("Invalid Age", "Please enter a number!")
        return
    age = int(age_str)
    if age < 1 or age > 50:
        messagebox.showwarning("Invalid Age", "Please enter a valid age between 1 and 50!")
        return
    
    if name and gender and course != "Select Course": 
        with open('students.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, gender, course])
        # Clear fields after saving
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_var.set("")
        course_combo.set("Select Course")
        messagebox.showinfo("Success", "Data saved successfully!")
    else:
        messagebox.showwarning("Error", "Please fill all fields!")

# Full Name
header = tk.Label(root, text="Student Registration Form", font=("Arial", 25, "bold"))
header.grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Age
tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Gender
tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, padx=60, sticky='w')

# Course
tk.Label(root, text="Course:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
course_combo = ttk.Combobox(root, values=["BCA", "BBA", "BSc", "BIT"], state="readonly", width=20)
course_combo.grid(row=4, column=1, padx=10, pady=5)
course_combo.set("Select Course")

# Register button
tk.Button(root, text="Register", command=save_data, bg="green", fg="white", width=15).grid(row=5, column=1, pady=20)

root.mainloop()

# Full Name
tk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Age
tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Gender
tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, padx=60, sticky='w')

# Course
tk.Label(root, text="Course:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
course_combo = ttk.Combobox(root, values=["BCA", "BBA", "BSc", "BIT"], state="readonly", width=20)
course_combo.grid(row=4, column=1, padx=10, pady=5)
course_combo.set("Select Course")

# Register button
tk.Button(root, text="Register", command=save_data, bg="green", fg="white", width=15).grid(row=5, column=1, pady=20)

if tk.Button(root, text= "Exit", command=root.destroy, bg="red", fg="white", width=10).grid(row=9, column=7, pady=20):
    messagebox.showwarning("Exiting the application", "Goodbye!")


root.mainloop()
