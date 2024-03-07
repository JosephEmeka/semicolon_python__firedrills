from diary_app.diary import diary


class diaries:
    def __init__(self):
        self.diaries = []

    def add_diary(self, username: str, password: str):
        my_diary = diary(username, password)
        self.diaries.append(my_diary)

    def delete_diary(self, username: str, password: str):
        my_diary = diary(username, password)
        diary_found = False
        for item in self.diaries:
            if item.getUserName() == username and my_diary.validatePassword(password):
                self.diaries.remove(item)
                diary_found = True
                break
        if not diary_found:
            raise ValueError("Dairy with user name {} not found".format(username))
