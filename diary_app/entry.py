class entry:
    def __init__(self, entry_id: int, title: str, body: str):
        self.entry_id = entry_id
        self.title = title
        self.body = body

    def getId(self):
        return self.entry_id

