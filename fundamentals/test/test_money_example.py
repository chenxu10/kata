# TODO:five.times(2)
# TODO: 5 dollor * 10 chf = 20 dollars if rate is 2:1

class Dollar:
    def __init__(self, amount) -> None:
        self.amount = amount

    def times(self, value):
        self.amount = self.amount * value
        return self.amount

def test_multipy():
    five = Dollar(5)
    amount = five.times(2)
    print(five.amount)
    assert amount == 10

def main():
    test_multipy()
    
if __name__ == '__main__':
    main()