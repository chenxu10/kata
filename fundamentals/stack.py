class Stack():
    class UnderflowException(Exception):
        def __init__(self, message):
            self.message = message
        
        def __str__(self):
            return self.message
    
    def __init__(self):
        self.isEmpty = True
        self.size = 0
        self.elements = []

    def is_empty(self):
        return self.isEmpty

    def push(self, item):
        self.elements.append(item)
        self.size += 1
        self.isEmpty = False

    def pop(self):
        if self.is_empty():
            raise Stack.UnderflowException('Stack is empty')
        else:
            value = self.elements.pop()
            if len(self.elements) == 0:
                self.isEmpty = True
            self.size -= 1
            return value
    