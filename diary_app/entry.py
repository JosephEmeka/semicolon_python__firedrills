from datetime import datetime


class entry:

    def __init__(self, entry_id: int, title: str, body: str):
        self.entry_id = entry_id
        self.title = title
        self.body = body
        self.date = datetime.now()

    def getId(self):
        return self.entry_id

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body

    def setTitle(self, title):
        self.title = title

    def setBody(self, body):
        self.body = body
