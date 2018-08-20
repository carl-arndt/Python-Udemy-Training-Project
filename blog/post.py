class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        print(self.title)
        print(self.content)

    def json(self):
        # returns a dictionary representing the post
        return {
            'title': self.title,
            'content': self.content, # trailing comma is optional
        }

