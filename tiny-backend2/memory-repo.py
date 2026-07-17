from repository import Repository

class MemoryRepository(Repository):
    def __init__(self):
        self.messages = []

    def add(self, text):
        self.messages.append(text)

    def get_all(self):
        return self.messages
