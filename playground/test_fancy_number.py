def count_fancy_number(x):
    div, mod = divmod(x, 4)
    count = 0
    if div == 0:
        if mod == 0:
            count += 1
        else: 
            count += 2
    return count  

def test_count_fancy_number():
    assert count_fancy_number(0) == 1
    assert count_fancy_number(1) == 2
    assert count_fancy_number(2) == 2    
    

if __name__ == "__main__":
    test_count_fancy_number()