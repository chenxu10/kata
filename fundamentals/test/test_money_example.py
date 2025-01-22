



class Dollar:
    def __init__(self,value):
        self.value = value

    def times(self, amount):
        self.value *= amount
        return self.value

def test_money_times():
    five = Dollar(5)
    assert five.times(2) == 10