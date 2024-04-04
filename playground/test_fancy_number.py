def count_fancy_numbers(n):
    q, r = divmod(n, 4)
    cnt_r = 1 if r % 4 == 0 else 0 if r % 4 == 1 else 1
    cnt_q = q // 4
    return cnt_r + cnt_q * 4

   
if __name__ == "__main__":
    print(count_fancy_numbers(1))
    print(count_fancy_numbers(2))