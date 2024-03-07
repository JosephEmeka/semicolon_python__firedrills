
from diary_app.entry import entry
from diary_app.InvalidPasswordException import InvalidPasswordException


class diary:
    entry_id = 0
    unique_entry_id_count = 1

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
        self.islocked = False
        self.entries = []

    def get_username(self):
        return self.user_name

    def is_diary_locked(self):
        return self.islocked

    def lockDiary(self):
        self.islocked = True

    def createEntry(self, title, body):
        self.entry_id += self.unique_entry_id_count
        freshEntry = entry(self.entry_id, title, body)
        self.entries.append(freshEntry)

    def deleteEntry(self, entry_id):
        if self.islocked:
            raise ValueError("You cannot delete! diary locked")

        entry_found = False
        for item in self.entries:
            if item.getId() == entry_id:
                self.entries.remove(item)
                entry_found = True
                break

        if not entry_found:
            raise ValueError("Entry with ID {} not found".format(entry_id))

    def unlockDiary(self, password):
        self.validatePassword(password)
        self.islocked = False

    def getEntryById(self, entry_id):
        for items in self.entries:
            if items.getId() == entry_id:
                return items
        else:
            raise ValueError("Entry with ID {} not found".format(entry_id))

    def validatePassword(self, password):
        if len(password) < 8:
            raise InvalidPasswordException("Invalid password error")
        if self.password == password:
            return True

    def update_entry(self, entry_id, tittle, body):
        if self.islocked:
            raise ValueError("Unlock to update entry! diary locked")
        self.getEntryById(entry_id).setTitle(tittle)
        self.getEntryById(entry_id).setBody(body)

