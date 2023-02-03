class Stack():
    class UnderflowException(Exception):
        def __init__(self, message):
            self.message = message
        
        def __str__(self):
            return self.message
    
    def __init__(self):
        self.items = []
        self.isEmpty = True

    def is_empty(self):
        return self.isEmpty

    def push(self, item):
        self.items.append(item)
        self.isEmpty = False

    def pop(self):
        if self.is_empty():
            raise Stack.UnderflowException('Stack is empty')
        else:
            self.items.pop()
            if len(self.items) == 0:
                self.isEmpty = True

    