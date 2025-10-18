import csv
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import date, datetime
import calendar

CSV_FILE = "expenses.csv"
CSV_HEADERS = ["ID", "Date", "Name", "Amount", "ReceiptPath"]

class SimpleCalendar(tk.Toplevel):
    def __init__(self, parent, sel_date_callback, year=None, month=None):
        super().__init__(parent)
        self.withdraw()
        self.transient(parent)
        self.title("Select Date")
        self.sel_date_callback = sel_date_callback
        self.resizable(False, False)

        today = date.today()
        self.year = year or today.year
        self.month = month or today.month

        self.header = ttk.Frame(self)
        self.header.pack(padx=8, pady=6, anchor="center")
        self.prev_btn = ttk.Button(self.header, text="<", width=3, command=self.prev_month)
        self.prev_btn.grid(row=0, column=0)
        self.title_lbl = ttk.Label(self.header, text="", width=15, anchor="center")
        self.title_lbl.grid(row=0, column=1, padx=6)
        self.next_btn = ttk.Button(self.header, text=">", width=3, command=self.next_month)
        self.next_btn.grid(row=0, column=2)

        self.days_frame = ttk.Frame(self)
        self.days_frame.pack(padx=8, pady=(0,8))

        self.build_calendar()
        self.update_title()
        self.deiconify()

    def build_calendar(self):
        for widget in self.days_frame.winfo_children():
            widget.destroy()
        days = ["Mo","Tu","We","Th","Fr","Sa","Su"]
        for c, d in enumerate(days):
            ttk.Label(self.days_frame, text=d, width=4, anchor="center").grid(row=0, column=c)
        cal = calendar.Calendar(firstweekday=0)
        month_days = list(cal.itermonthdays(self.year, self.month))
        r = 1; c = 0
        for idx, day in enumerate(month_days):
            if day == 0:
                ttk.Label(self.days_frame, text="", width=4).grid(row=r, column=c)
            else:
                btn = ttk.Button(self.days_frame, text=str(day), width=4, command=lambda d=day: self.on_pick(d))
                btn.grid(row=r, column=c, padx=1, pady=1)
            c += 1
            if c >= 7:
                c = 0; r += 1

    def update_title(self):
        self.title_lbl.config(text=f"{calendar.month_name[self.month]} {self.year}")

    def on_pick(self, day):
        selected = date(self.year, self.month, day)
        self.sel_date_callback(selected.strftime("%Y-%m-%d"))
        self.destroy()

    def prev_month(self):
        if self.month == 1:
            self.month = 12; self.year -= 1
        else:
            self.month -= 1
        self.build_calendar()
        self.update_title()

    def next_month(self):
        if self.month == 12:
            self.month = 1; self.year += 1
        else:
            self.month += 1
        self.build_calendar()
        self.update_title()

class ExpenseManager:
    def __init__(self, filename=CSV_FILE):
        self.filename = filename
        self.records = []
        self._ensure_file()
        self._load()

    def _ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(CSV_HEADERS)

    def _load(self):
        self.records.clear()
        with open(self.filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row or not row["ID"]:
                    continue
                try:
                    amount = float(row["Amount"]) if row["Amount"].strip() else 0.0
                except ValueError:
                    amount = 0.0
                rec = {
                    "ID": int(row["ID"]),
                    "Date": row["Date"],
                    "Name": row["Name"],
                    "Amount": amount,
                    "ReceiptPath": row.get("ReceiptPath", "")
                }
                self.records.append(rec)
        self.records.sort(key=lambda r: r["ID"])

    def _write_all(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
            for r in self.records:
                writer.writerow([
                    r["ID"],
                    r["Date"],
                    r["Name"],
                    f"{r['Amount']:.2f}",
                    r["ReceiptPath"]
                ])

    def add(self, date_s, name, amount, receipt_path):
        next_id = 1 if not self.records else max(r["ID"] for r in self.records) + 1
        rec = {"ID": next_id, "Date": date_s, "Name": name, "Amount": float(amount), "ReceiptPath": receipt_path or ""}
        self.records.append(rec)
        self._write_all()
        return rec

    def update(self, rec_id, date_s, name, amount, receipt_path):
        for r in self.records:
            if r["ID"] == rec_id:
                r["Date"] = date_s
                r["Name"] = name
                r["Amount"] = float(amount)
                r["ReceiptPath"] = receipt_path or ""
                break
        self._write_all()

    def delete(self, rec_id):
        self.records = [r for r in self.records if r["ID"] != rec_id]
        self._write_all()

    def export(self, filepath, filtered_records):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
            for r in filtered_records:
                writer.writerow([r["ID"], r["Date"], f"{r['Amount']:.2f}", r["ReceiptPath"]])

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker - Teacher Edition")
        self.root.geometry("1000x650")
        self.root.minsize(900, 550)

        self.manager = ExpenseManager()
        self.selected_id = None
        self.receipt_path = ""

        self._build_vars()
        self._build_ui()
        self._load_tree()
        self._update_total()
        self._set_status("Ready")

    def _build_vars(self):
        self.date_var = tk.StringVar(value=str(date.today()))
        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.receipt_var = tk.StringVar(value="No file selected")
        self.search_var = tk.StringVar()
        self.mode_dark = False

    def _build_ui(self):
        top_frame = ttk.LabelFrame(self.root, text="Add New Expense")
        top_frame.grid(row=0, column=0, padx=12, pady=10, sticky="ew")
        top_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(top_frame, text="Date:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
        date_frame = ttk.Frame(top_frame)
        date_frame.grid(row=0, column=1, sticky="w", padx=6)
        self.date_entry = ttk.Entry(date_frame, textvariable=self.date_var, width=18)
        self.date_entry.pack(side="left", padx=(0,4))
        ttk.Button(date_frame, text="📅", width=3, command=self.open_calendar).pack(side="left")

        ttk.Label(top_frame, text="Name:").grid(row=1, column=0, sticky="w", padx=6, pady=6)
        ttk.Entry(top_frame, textvariable=self.name_var, width=40).grid(row=1, column=1, sticky="w", padx=6)

        ttk.Label(top_frame, text="Amount ($):").grid(row=2, column=0, sticky="w", padx=6, pady=6)
        ttk.Entry(top_frame, textvariable=self.amount_var, width=20).grid(row=2, column=1, sticky="w", padx=6)

        ttk.Label(top_frame, text="Receipt:").grid(row=3, column=0, sticky="w", padx=6, pady=6)
        receipt_row = ttk.Frame(top_frame)
        receipt_row.grid(row=3, column=1, sticky="w", padx=6)
        self.receipt_label = ttk.Label(receipt_row, textvariable=self.receipt_var, width=40, anchor="w", relief="sunken")
        self.receipt_label.pack(side="left", padx=(0,6))
        ttk.Button(receipt_row, text="Browse", command=self.browse_receipt).pack(side="left")

        actions = ttk.Frame(top_frame)
        actions.grid(row=4, column=0, columnspan=2, pady=8)
        self.add_btn = ttk.Button(actions, text="Add Expense", command=self.add_expense, width=18)
        self.add_btn.pack(side="left", padx=6)
        self.update_btn = ttk.Button(actions, text="Update Selected", command=self.update_expense, width=18, state="disabled")
        self.update_btn.pack(side="left", padx=6)
        self.delete_btn = ttk.Button(actions, text="Delete Selected", command=self.delete_expense, width=18, state="disabled")
        self.delete_btn.pack(side="left", padx=6)

        bottom_frame = ttk.LabelFrame(self.root, text="Expenses")
        bottom_frame.grid(row=1, column=0, padx=12, pady=8, sticky="nsew")
        bottom_frame.grid_rowconfigure(1, weight=1)
        bottom_frame.grid_columnconfigure(0, weight=1)

        search_row = ttk.Frame(bottom_frame)
        search_row.grid(row=0, column=0, sticky="ew", padx=6, pady=(6,0))
        ttk.Label(search_row, text="Search:").pack(side="left")
        search_entry = ttk.Entry(search_row, textvariable=self.search_var, width=40)
        search_entry.pack(side="left", padx=(6,6))
        search_entry.bind("<KeyRelease>", self.on_search)

        ttk.Button(search_row, text="Clear", command=self.clear_search).pack(side="left")
        ttk.Button(search_row, text="Export Filtered", command=self.export_filtered).pack(side="left", padx=6)
        ttk.Button(search_row, text="Toggle Dark", command=self.toggle_theme).pack(side="left")

        columns = ("ID", "Date", "Name", "Amount", "Receipt")
        self.tree = ttk.Treeview(bottom_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Receipt", text="Receipt")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Date", width=110, anchor="center")
        self.tree.column("Name", width=300)
        self.tree.column("Amount", width=110, anchor="e")
        self.tree.column("Receipt", width=80, anchor="center")
        self.tree.grid(row=1, column=0, sticky="nsew", padx=6, pady=6)

        vsb = ttk.Scrollbar(bottom_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        vsb.grid(row=1, column=1, sticky="ns", pady=6)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        footer = ttk.Frame(self.root)
        footer.grid(row=2, column=0, sticky="ew", padx=12, pady=(0,6))
        footer.grid_columnconfigure(0, weight=1)

        self.total_lbl = ttk.Label(footer, text="Total: $0.00")
        self.total_lbl.pack(side="left")
        self.status_lbl = ttk.Label(footer, text="", anchor="e")
        self.status_lbl.pack(side="right")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def open_calendar(self):
        SimpleCalendar(self.root, self._set_date)

    def _set_date(self, date_str):
        self.date_var.set(date_str)

    def browse_receipt(self):
        p = filedialog.askopenfilename(title="Select Receipt", filetypes=[("Images & PDFs", "*.jpg *.jpeg *.png *.pdf"), ("All files","*.*")])
        if p:
            self.receipt_path = p
            self.receipt_var.set(os.path.basename(p))
            self._set_status("Receipt selected")
        else:
            self.receipt_path = ""
            self.receipt_var.set("No file selected")
            self._set_status("Receipt cleared")

    def _load_tree(self, records=None):
        for r in self.tree.get_children():
            self.tree.delete(r)
        to_show = records if records is not None else self.manager.records
        for r in to_show:
            self.tree.insert("", tk.END, values=(r["ID"], r["Date"], r["Name"], f"${r['Amount']:.2f}", "Yes" if r["ReceiptPath"] else "No"))
        self._update_total(to_show)

    def _get_selected_record(self):
        sel = self.tree.selection()
        if not sel:
            return None
        vals = self.tree.item(sel[0], "values")
        rec_id = int(vals[0])
        for r in self.manager.records:
            if r["ID"] == rec_id:
                return r
        return None

    def on_select(self, event):
        rec = self._get_selected_record()
        if rec:
            self.selected_id = rec["ID"]
            self.date_var.set(rec["Date"])
            self.name_var.set(rec["Name"])
            self.amount_var.set(f"{rec['Amount']:.2f}")
            self.receipt_path = rec["ReceiptPath"]
            self.receipt_var.set(os.path.basename(rec["ReceiptPath"]) if rec["ReceiptPath"] else "No file selected")
            self.update_btn.config(state="normal")
            self.delete_btn.config(state="normal")
            self.add_btn.config(state="disabled")
            self._set_status(f"Selected ID {rec['ID']}")
        else:
            self.clear_form()

    def clear_form(self):
        self.selected_id = None
        self.date_var.set(str(date.today()))
        self.name_var.set("")
        self.amount_var.set("")
        self.receipt_path = ""
        self.receipt_var.set("No file selected")
        self.update_btn.config(state="disabled")
        self.delete_btn.config(state="disabled")
        self.add_btn.config(state="normal")
        self.tree.selection_remove(self.tree.selection())

    def add_expense(self):
        name = self.name_var.get().strip()
        amount = self.amount_var.get().strip()
        date_s = self.date_var.get().strip()

        if not name or not amount:
            messagebox.showerror("Error", "Name and Amount required")
            return
        try:
            amt = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")
            return

        newr = self.manager.add(date_s, name, amt, self.receipt_path)
        self._load_tree()
        self.clear_form()
        self._set_status(f"Added ID {newr['ID']}")

    def update_expense(self):
        if not self.selected_id:
            return
        name = self.name_var.get().strip()
        amount = self.amount_var.get().strip()
        date_s = self.date_var.get().strip()
        if not name or not amount:
            messagebox.showerror("Error", "Name and Amount required")
            return
        try:
            amt = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")
            return
        self.manager.update(self.selected_id, date_s, name, amt, self.receipt_path)
        self._load_tree()
        self.clear_form()
        self._set_status(f"Updated ID {self.selected_id}")

    def delete_expense(self):
        rec = self._get_selected_record()
        if not rec:
            return
        if messagebox.askyesno("Confirm", f"Delete ID {rec['ID']}?"):
            self.manager.delete(rec["ID"])
            self._load_tree()
            self.clear_form()
            self._set_status(f"Deleted ID {rec['ID']}")

    def on_search(self, event=None):
        q = self.search_var.get().strip().lower()
        if not q:
            self._load_tree()
            return
        filtered = []
        for r in self.manager.records:
            if (q in str(r["ID"]).lower() or q in r["Date"].lower() or q in r["Name"].lower()
                or q in f"{r['Amount']:.2f}".lower() or q in (r["ReceiptPath"] or "").lower()):
                filtered.append(r)
        self._load_tree(filtered)

    def clear_search(self):
        self.search_var.set("")
        self._load_tree()
        self._set_status("Search cleared")

    def export_filtered(self):
        q = self.search_var.get().strip().lower()
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv"),("All files","*.*")])
        if not filepath:
            return
        if q:
            filtered = []
            for r in self.manager.records:
                if (q in str(r["ID"]).lower() or q in r["Date"].lower() or q in r["Name"].lower()
                    or q in f"{r['Amount']:.2f}".lower() or q in (r["ReceiptPath"] or "").lower()):
                    filtered.append(r)
            self.manager.export(filepath, filtered)
        else:
            self.manager.export(filepath, self.manager.records)
        self._set_status(f"Exported to {os.path.basename(filepath)}")

    def _update_total(self, records=None):
        recs = records if records is not None else self.manager.records
        total = sum(r["Amount"] for r in recs)
        self.total_lbl.config(text=f"Total: ${total:.2f}")

    def _set_status(self, msg):
        self.status_lbl.config(text=msg)

    def toggle_theme(self):
        if not self.mode_dark:
            style = ttk.Style()
            try:
                style.theme_use("clam")
            except:
                pass
            style.configure(".", background="#2e2e2e", foreground="#f0f0f0", fieldbackground="#3a3a3a")
            style.configure("Treeview", background="#252525", foreground="#f0f0f0", fieldbackground="#252525")
            self.root.configure(bg="#2e2e2e")
            self.mode_dark = True
            self._set_status("Dark mode on")
        else:
            style = ttk.Style()
            try:
                style.theme_use("default")
            except:
                pass
            style.configure(".", background=None, foreground=None, fieldbackground=None)
            self.root.configure(bg=None)
            self.mode_dark = False
            self._set_status("Dark mode off")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()
