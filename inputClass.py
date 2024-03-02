class inputClass:
    def __init__(self):
        self.consoleString = ""

    def getString(self, consoleString: str):
        self.consoleString = consoleString

    @property
    def printString(self):
        return self.consoleString.upper()
