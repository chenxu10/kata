def count_fancy_numbers(n):
    if n == 0:
        return 1
    
    count = 0
    for i in range(n + 1):
        div, mod = divmod(i, 4)
        
        if div == 1 and mod == 1:
            count += 1

        if div == 1 and mod == 0:
            count += 1

        if div == 0 and mod == 1:
            count += 1

        if div == 0 and mod == 0:
            count += 1
    
    return count


if __name__ == '__main__':
    assert count_fancy_numbers(0) == 1
    assert count_fancy_numbers(1) == 2