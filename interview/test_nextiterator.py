class next_iterator():
    """
    O(1)
    """
    def __init__(self, A):
        self.array = A
        self.cur_index = 0
        self.remaining_times = self.array[self.cur_index + 1]

    def next(self):
        if self.has_next():
            self.remaining_times -= 1
        else:
            self.cur_index += 2
            self.remaining_times = self.array[self.cur_index + 1] - 1
        print("remaing time is {}".format(self.remaining_times))
        cur_number = self.array[self.cur_index]
        return cur_number
    
    def has_next(self):
        return self.remaining_times > 0

def test_nextiterator():
    A = [1,2,3,4]
    B = next_iterator(A)
    print(B.next())
    print(B.next())
    print(B.next())
    print(B.next())
    print(B.next())
    print(B.next())


# blocked at has_next function
# didn't come up with a temp variable to to maintain
# Follow up if next is 0 return pervious one


if __name__ == '__main__':
    test_nextiterator()