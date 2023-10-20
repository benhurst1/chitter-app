class Post:
    def __init__(self, id, text, user_id, time=None, date=None, username=None):
        self.id = id
        self.text = text
        self.user_id = user_id
        self.time = time
        self.date = date
        self.username = username
