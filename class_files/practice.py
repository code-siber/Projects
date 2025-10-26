import tkinter as tk

root = tk.Tk()
root.title("Rowspan and Columnspan Example")
root.geometry("600x200")

# The label spanning multiple rows and columns
tk.Label(
    root, 
    text="Hello", 
    bg="red", 
    fg="white", 
    font=("Arial", 16, "bold")
).grid(row=0, column=2, columnspan=5, rowspan=2, sticky="nsew", padx=2, pady=2)

# Optional: draw other grid cells to see the effect
for r in range(4):
    for c in range(10):
        if not (r in [0,1] and 4 <= c <= 8):
            tk.Label(root, text=f"{r},{c}", bg="lightgrey", borderwidth=1, relief="solid", width=6, height=2).grid(row=r, column=c, padx=1, pady=1)

root.mainloop()
