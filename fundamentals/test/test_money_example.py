



class Dollar:
    def __init__(self,amount):
        self.amount = amount

    def times(self, multipler):
        self.amount *= multipler 

def test_money_times():
    five = Dollar(5)
    result = five.times(2)
    assert five.amount == 10

def main():
    test_money_times()

if __name__ == '__main__':
    main()