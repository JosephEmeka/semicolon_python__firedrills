import tkinter as tk
from tkinter import messagebox, simpledialog
from bank_app.bank import bank


class bank_app:
    access_bank = bank("Access")

    def __init__(self, root):
        self.root = root
        self.root.title("WELCOME TO SEMICOLON BANK WHERE WIMPS LIKE YOU PAY THEIR LOAN ")

        menu_bar = tk.Menu(root)
        menu = tk.Menu(menu_bar)

        menu.add_command(label = "Create Account", command = self.create_account)
        menu.add_command(label = "Deposit", command = self.deposit)
        menu.add_command(label = "Withdraw", command = self.withdraw)
        menu.add_command(label = "Transfer", command = self.transfer)
        menu.add_command(label = "Check Balance", command = self.check_balance)
        menu.add_command(label = "Remove Account", command = self.remove_account)
        menu.add_command(label = "Find Account", command = self.find_account)
        menu.add_command(label = "Exit", command = root.quit)
        menu_bar.add_cascade(label = "Menu", menu = menu)
        root.config(menu = menu_bar)

    def create_account(self):
        first_name = simpledialog.askstring("Customer first name", "Enter first name:")
        last_name = simpledialog.askstring("Customer last name", "Enter last name:")
        pin = simpledialog.askstring("customer pin number", "Enter pin number:")
        if first_name and last_name and pin:
            self.access_bank.register_customer(first_name, last_name, pin)
            account_number = self.access_bank.get_account_number(first_name, last_name)
            messagebox.showinfo("Create Account",
                f"Account {first_name} {last_name} with account number {account_number} created successfully")
        else:
            messagebox.showerror("Create Account", "first name and last name are required.")

    def deposit(self):
        account_number = simpledialog.askinteger("Deposit", "Enter Account Number:")
        amount = simpledialog.askinteger("Deposit", "Enter Amount:")
        if account_number and amount:
            self.access_bank.deposit(account_number, amount)
            messagebox.showinfo("Deposit", f"You Deposited #{amount} successfully in {account_number}")
        else:
            messagebox.showerror("Deposit", "Account number and Amount required.")

    def withdraw(self):
        account_number = simpledialog.askinteger("Withdraw", "Enter Account Number:")
        amount = simpledialog.askinteger("Withdraw", "Enter Amount:")
        pin = simpledialog.askstring("Withdraw", "Enter Pin")
        if account_number and amount and pin:
            self.access_bank.withdraw(account_number, amount, pin)
            messagebox.showinfo("Withdraw",
                f"You withdrew #{amount} successfully from your account with account number {account_number}")
        else:
            messagebox.showerror("Withdraw", "Account number and Amount are required.")

    def transfer(self):
        source_account_number = simpledialog.askinteger("Transfer", "Enter Source Account Number:")
        destination_account_number = simpledialog.askinteger("Transfer", "Enter Destination Account Number:")
        amount = simpledialog.askinteger("Transfer", "Enter Amount:")
        pin = simpledialog.askstring("Transfer", "Enter Pin")
        if source_account_number and destination_account_number and amount and pin:
            self.access_bank.transfer(source_account_number, destination_account_number, amount, pin)
            messagebox.showinfo("Transfer", "Transfer Successful")
        else:
            messagebox.showerror("Transfer", "Source Account, Destination Account, Amount and Pin are required.")

    def check_balance(self):
        account_number = simpledialog.askinteger("Check Balance", "Enter Account Number:")
        pin = simpledialog.askstring("Check Balance", "Enter Pin")
        if account_number and pin:
            balance = self.access_bank.check_balance(account_number, pin)
            messagebox.showinfo("Check Balance", f"Account Balance for {account_number} is #{balance}")
        else:
            messagebox.showerror("Check Balance", "first name and last name are required.")

    def remove_account(self):
        account_number = simpledialog.askinteger("Remove Account", "Enter Account Number:")
        if account_number:
            self.access_bank.remove_account(account_number)
            messagebox.showinfo("Remove Account", f"Account {account_number} successfully removed")
        else:
            messagebox.showerror("Remove Account", "Account Number required.")

    def find_account(self):
        account_number = simpledialog.askinteger("Find Account", "Enter Account Number:")
        if account_number:
            account = self.access_bank.find_account(account_number)
            if account:
                messagebox.showinfo("Find Account", f"Account {account_number} found\n{account}")
            else:
                messagebox.showinfo("Find Account", f"Account {account_number} not found")
        else:
            messagebox.showerror("find Account number", "Account Number required.")


if __name__ == "__main__":
    root = tk.Tk()
    app = bank_app(root)
    root.mainloop()
