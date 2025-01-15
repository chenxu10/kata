# TODO:five.times(2)
# TODO: 5 dollor * 10 chf = 20 dollars if rate is 2:1

class Dollar:
    def __init__(self, amount) -> None:
        self.amount = amount 
    
    def times(self, multipler):
        self.amount = self.amount * multipler

def test_multiply():
    five = Dollar(5)
    assert 10 == five.times(2).amount