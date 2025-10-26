import tkinter as tk
from tkinter import ttk, messagebox
import csv, os, hashlib
import pygame

root = tk.Tk()
root.title("Student Portal")
root.geometry("550x350")
root.resizable(False, False)

class Student:
    def __init__(self, root):
        self.root = root
        self.login_ui()

    # ---------------- HASH FUNCTION -----------------
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # ---------------- LOGIN UI -----------------
    def login_ui(self):
        tk.Label(self.root, text="Student Login", font=("Arial", 25, "bold")).grid(row=0, column=1, columnspan=2, pady=20)
        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Password:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Login", command=self.login_button).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Create New Account", command=self.create_account_window).grid(row=5, column=0, columnspan=2, pady=10)

    # ---------------- REGISTER BUTTON -----------------
    def register_button(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()
        email = self.reg_email_entry.get()
        password = self.reg_password_entry.get()

        if not name or not age or not gender or not email or not password:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        if os.path.exists("users.csv"):
            with open("users.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and len(row) > 3 and row[3] == email:
                        messagebox.showwarning("Warning", "Email already exists!")
                        return

        hashed_pw = self.hash_password(password)

        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, gender, email, hashed_pw])

        messagebox.showinfo("Success", "Account created successfully")
        self.account_window.destroy()

    # ---------------- LOGIN BUTTON -----------------
    def login_button(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        hashed_pw = self.hash_password(password)

        if not os.path.exists("users.csv"):
            messagebox.showerror("Error", "User not found")
            return

        login_success = False
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 1:
                    if row[3] == email and row[4] == hashed_pw:
                        login_success = True
                        break

        if login_success:
            messagebox.showinfo("Success", "Login successful!")
            self.root.withdraw()
            self.info_window(email)
        elif email == "" and password == "":
            messagebox.showwarning("Warning", "Please fill all fields!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # ---------------- INFO WINDOW -----------------
    def info_window(self, email):
        self.information_window = tk.Toplevel(self.root)
        self.information_window.title("Student Portal")
        self.information_window.geometry("400x250")
        self.information_window.resizable(False, False)

        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 3 and row[3] == email:
                    student_name = row[0]
                    tk.Label(
                        self.information_window,
                        text="Welcome " + student_name,
                        font=("Arial", 25, "bold")  
                    ).pack(pady=40)

        tk.Button(self.information_window, text="Exit", command=self.root.destroy).pack(pady=20)

    # ---------------- CREATE ACCOUNT WINDOW -----------------
    def create_account_window(self):
        self.account_window = tk.Toplevel(self.root)
        self.account_window.title("Create New Account")
        self.account_window.geometry("400x400")
        self.account_window.resizable(False, False)

        tk.Label(self.account_window, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.name_entry = tk.Entry(self.account_window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.account_window, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.age_entry = tk.Entry(self.account_window)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.account_window, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.gender_var = tk.StringVar()
        tk.Radiobutton(self.account_window, text="Male", variable=self.gender_var, value="Male").grid(row=2, column=1, sticky='w')
        tk.Radiobutton(self.account_window, text="Female", variable=self.gender_var, value="Female").grid(row=2, column=1, padx=60, sticky='w')

        tk.Label(self.account_window, text="Email:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.reg_email_entry = tk.Entry(self.account_window)
        self.reg_email_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.account_window, text="Password:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.reg_password_entry = tk.Entry(self.account_window, show="*")
        self.reg_password_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.account_window, text="Register", command=self.register_button).grid(row=5, column=0, columnspan=2, pady=15)
        tk.Button(self.account_window, text="Cancel", command=self.account_window.destroy).grid(row=6, column=0, columnspan=2, pady=5)

student = Student(root)

if pygame.event.EventType == pygame.QUIT:
    root.destroy()
root.mainloop()
