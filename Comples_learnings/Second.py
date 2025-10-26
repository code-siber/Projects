import tkinter as tk
from tkinter import ttk, messagebox
import csv, os, hashlib
import pygame

root = tk.Tk()
root.title("Library Management System")
root.geometry("550x350")
root.resizable(False, False)

class student:
    def __init__(self, root):
        self.root = root
        self.register_ui()

    def register_ui(self):
        ttk.Label(self.root, text="Book Registration", font=("monocursive", 25, "bold")).grid(row=0, column=1, columnspan=2, pady=20)
        tk.Button(self.root, text="Register the book", command=self.register_book).grid(row=4, column=0, columnspan=2, pady=10)
    
    def register_book(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register Book")
        register_window.geometry("400x300")
        register_window.resizable(False, False)

        ttk.Label(register_window, text="Book Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.book_name_entry = tk.Entry(register_window)

if pygame.event.EventType == pygame.QUIT:
    root.destroy()
root.mainloop()


