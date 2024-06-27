import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.expenses = []
        self.spending_limit = tk.DoubleVar()
        self.spending_limit.set(1000)  # Set default spending limit

        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = tk.Label(self.master, text="Expense Tracker", font=("Helvetica", 16))
        self.lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.lbl_amount = tk.Label(self.master, text="Amount:")
        self.lbl_amount.grid(row=1, column=0, sticky=tk.E)

        self.ent_amount = tk.Entry(self.master)
        self.ent_amount.grid(row=1, column=1)

        self.lbl_description = tk.Label(self.master, text="Description:")
        self.lbl_description.grid(row=2, column=0, sticky=tk.E)

        self.ent_description = tk.Entry(self.master)
        self.ent_description.grid(row=2, column=1)

        self.lbl_limit = tk.Label(self.master, text="Spending Limit: Rs")
        self.lbl_limit.grid(row=3, column=0, sticky=tk.E)

        self.ent_limit = tk.Entry(self.master, textvariable=self.spending_limit)
        self.ent_limit.grid(row=3, column=1)

        self.btn_add = tk.Button(self.master, text="Add Expense", command=self.add_expense)
        self.btn_add.grid(row=4, column=0, columnspan=2, pady=10)

        self.lst_expenses = tk.Listbox(self.master, height=10, width=50)
        self.lst_expenses.grid(row=5, column=0, columnspan=2, padx=10)

        self.btn_clear = tk.Button(self.master, text="Clear All", command=self.clear_expenses)
        self.btn_clear.grid(row=6, column=0, columnspan=2, pady=10)

    def add_expense(self):
        amount = self.ent_amount.get()
        description = self.ent_description.get()

        if amount and description:
            amount = float(amount)
            if amount <= self.spending_limit.get():
                self.expenses.append((description, amount))
                self.update_expense_list()
                self.ent_amount.delete(0, tk.END)
                self.ent_description.delete(0, tk.END)
                self.update_spending_limit()
            else:
                messagebox.showwarning("Exceeded Spending Limit", f"The expense of ${amount} exceeds the spending limit of ${self.spending_limit.get()}.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter both amount and description.")

    def update_expense_list(self):
        self.lst_expenses.delete(0, tk.END)
        for description, amount in self.expenses:
            self.lst_expenses.insert(tk.END, f"{description}: Rs{amount}")

    def update_spending_limit(self):
        total_expenses = sum(amount for _, amount in self.expenses)
        remaining_limit = self.spending_limit.get() - total_expenses
        if remaining_limit < 0:
            messagebox.showinfo("Warning", "Spending limit exceeded!")
        self.lbl_limit.config(text=f"Spending Limit: {remaining_limit:.2f}")

    def clear_expenses(self):
        self.expenses = []
        self.update_expense_list()
        self.update_spending_limit()

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


