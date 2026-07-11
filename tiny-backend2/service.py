class MessageService:

    def __init__(self, repository):
        self.repository = repository

    def add_message(self, text):
        self.repository.add(text)

    def get_messages(self):
        return self.repository.get_all()