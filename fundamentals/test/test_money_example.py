



class Dollar:
    def __init__(self,amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

def test_money_times():
    five = Dollar(5)
    dollar = five.times(2)
    assert dollar.amount == 10
    dollar = five.times(3)
    assert dollar.amount==15

def main():
    test_money_times()

if __name__ == '__main__':
    main()