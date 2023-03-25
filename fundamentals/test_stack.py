import pytest
from stack2 import Stack

class TestStack():
    @pytest.mark.parametrize
    def test_create_stack(self):
        stack = Stack()
        return stack