class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def to_dict(self):
        return {
            "Title": self.title,
            "Description": self.description
        }