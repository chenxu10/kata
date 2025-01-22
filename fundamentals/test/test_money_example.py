



class Dollar:
    def __init__(self,value):
        self.value = value

    def times(self, amount):
        self.value *= amount
        return self.value        

def test_money_times():
    five = Dollar(5)
    result = five.times(2)
    assert result == 10

def main():
    test_money_times()

if __name__ == '__main__':
    main()