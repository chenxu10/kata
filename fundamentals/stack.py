class Stack():
    def __init__(self):
        self.items = []
        self.isEmpty = True

    def is_empty(self):
        return self.isEmpty

    def push(self, item):
        self.items.append(item)
        self.isEmpty = False