from stack import Stack 

class TestStack():
    def test_create_stack(self):
        stack = Stack()
        assert stack.is_empty() == True

    def test_push(self):
        stack = Stack()
        stack.push(1)
        assert stack.is_empty() == False

    