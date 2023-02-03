from stack import Stack 
import pytest

class TestStack():
    @pytest.fixture
    def stack(self):
        stack = Stack()
        return stack
        
    def test_create_stack(self, stack):
        assert stack.is_empty() == True

    def test_afteronepush_isstillempty(self, stack):
        stack.push(1)
        assert stack.is_empty() == False

    def test_willthrowunderflow_whenemptystackispopped(self, stack):
        with pytest.raises(stack.UnderflowException):
            stack.pop()

    