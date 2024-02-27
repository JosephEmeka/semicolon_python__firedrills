from diary_app import *
from diary_app.entry import entry


class diary:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
        self.islocked = False
        self.entry_id = 0
        self.entries = []

    def get_username(self):
        return self.user_name

    def validate_password(self, password: str):
        if self.password == password:
            return True

    def is_diary_locked(self):
        return self.islocked

    def lockDiary(self):
        self.islocked = True

    def createEntry(self, title, body):
        self.entry_id += 1
        freshEntry = entry(self.entry_id, title, body)
        self.entries.append(freshEntry)

    def deleteEntry(self, entry_id: int):
        if self.islocked:
            raise ValueError("You cannot delete! diary locked")
        for item in self.entries:
            if item.getId() == entry_id:
                self.entries.remove(item)
                break
