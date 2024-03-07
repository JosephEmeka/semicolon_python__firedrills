import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from diary_app.diaries import diaries
from diary_app.diary import diary


class diary_app:
    new_diaries = diaries()

    def __init__(self, app_root):
        self.root = app_root
        self.root.title("WELCOME TO SEMICOLON DIARY APP ")

        menu_bar = tk.Menu(app_root)
        menu = tk.Menu(menu_bar)

        menu.add_command(label="Create Diary", command=self.create_diary)
        menu.add_command(label="Lock Diary", command=self.lock_diary)
        menu.add_command(label="Unlock Diary", command=self.unlock_diary)
        menu.add_command(label="Add Entry", command=self.add_entry)
        menu.add_command(label="Delete Entry", command=self.delete_entry)
        menu.add_command(label="Update Entry", command=self.update_entry)
        menu.add_command(label="Find Entry by Id", command=self.find_entry_by_id)
        menu.add_command(label="Exit", command=app_root.quit)
        menu_bar.add_cascade(label="Menu", menu=menu)
        app_root.config(menu=menu_bar)

    def create_diary(self):
        user_name = simpledialog.askstring("Create diary", "Enter username:")
        password = simpledialog.askstring("Create diary", "Enter password:")
        if user_name and password:
            new_diary = diary(user_name, password)
            self.new_diaries.add_diary(new_diary.user_name, new_diary.password)
            messagebox.showinfo("Create Diary", f"Diary {user_name} created successfully")
        else:
            messagebox.showerror("Create Diary", "Username and password are required.")

    def unlock_diary(self):
        user_name = simpledialog.askstring("Unlock Diary", "Enter username:")
        password = simpledialog.askstring("Unlock Diary", "Enter password:")
        if password and user_name:
            for my_diary in self.new_diaries.diaries:
                if my_diary.password == password and my_diary.get_username() == user_name:
                    my_diary.unlockDiary()
                    messagebox.showinfo("Unlock Diary", "Diary unlocked successfully")
                    return
            messagebox.showerror("Unlock Diary", "Incorrect password or diary not found")
        else:
            messagebox.showerror("Unlock Diary", "Username and password are required.")

    def lock_diary(self):
        user_name = simpledialog.askstring("Lock Diary", "Enter username:")
        password = simpledialog.askstring("Lock Diary", "Enter password:")
        if password and user_name:
            for my_diary in self.new_diaries.diaries:
                if my_diary.password == password and my_diary.get_username() == user_name:
                    my_diary.lockDiary()
                    messagebox.showinfo("Lock Diary", "Diary locked successfully")
                    return
            messagebox.showerror("Lock Diary", "Incorrect password or diary not found")
        else:
            messagebox.showerror("Lock Diary", "Username and password are required.")

    def add_entry(self):
        diary_user_name = simpledialog.askstring("Add Entry", "Enter username:")
        diary_password = simpledialog.askstring("Add Entry", "Enter password:")
        title = simpledialog.askstring("Add Entry", "What is your entry title:")
        body = simpledialog.askstring("Add Entry", "Write body:")
        if diary_user_name and diary_password:
            for my_diary in self.new_diaries.diaries:
                if my_diary.get_username() == diary_user_name and my_diary.password == diary_password:
                    my_diary.unlockDiary()
                    my_diary.createEntry(title, body)
                    messagebox.showinfo("Add Entry", "Entry created successfully")
                    return
            messagebox.showerror("Add Entry", "Incorrect username or password")
        else:
            messagebox.showerror("Add Entry", "Username and password are required.")

    def delete_entry(self):
        diary_user_name = simpledialog.askstring("Delete Entry", "Enter username:")
        diary_password = simpledialog.askstring("Delete Entry", "Enter password:")
        if diary_user_name and diary_password:
            for my_diary in self.new_diaries.diaries:
                if my_diary.get_username() == diary_user_name and my_diary.password == diary_password:
                    my_diary.unlockDiary()
                    my_diary.deleteEntry(entry_id=my_diary.entry_id)
                    messagebox.showinfo("Delete Entry", "Entry deleted successfully")
                    return
            messagebox.showerror("Delete Entry", "Incorrect username or password")
        else:
            messagebox.showerror("Delete Entry", "Username and password are required.")

    def update_entry(self):
        diary_user_name = simpledialog.askstring("Update Entry", "Enter username:")
        diary_password = simpledialog.askstring("Update Entry", "Enter password:")
        title = simpledialog.askstring("Update Entry", "What is your entry new title:")
        body = simpledialog.askstring("Update Entry", "Write new body:")
        if diary_user_name and diary_password:
            for my_diary in self.new_diaries.diaries:
                if my_diary.get_username() == diary_user_name and my_diary.password == diary_password:
                    my_diary.unlockDiary()
                    my_diary.updateEntry(entry_id=my_diary.entry_id, title=title, body=body)
                    messagebox.showinfo("Update Entry", "Entry updated successfully")
                    return
            messagebox.showerror("Update Entry", "Incorrect username or password")
        else:
            messagebox.showerror("Update Entry", "Username and password are required.")

    def find_entry_by_id(self):
        diary_user_name = simpledialog.askstring("Find Entry By Id", "Enter username:")
        diary_password = simpledialog.askstring("Find Entry By Id", "Enter password:")
        if diary_user_name and diary_password:
            for my_diary in self.new_diaries.diaries:
                if my_diary.get_username() == diary_user_name and my_diary.password == diary_password:
                    my_diary.unlockDiary()
                    my_diary.getEntryById(entry_id=my_diary.entry_id)
                    messagebox.showinfo("Find Entry By Id", "Entry found")
                    return
            messagebox.showerror("Find Entry By Id", "Incorrect username or password")
        else:
            messagebox.showerror("Find Entry By Id", "Username and password are required.")


if __name__ == "__main__":
    root = tk.Tk()
    app = diary_app(root)
    root.mainloop()
