def count_fancy_numbers(n):
    q, r = divmod(n, 3)
    cnt_r = 1 if r % 3 == 0 else 0 if r % 3 == 1 else 1
    cnt_q = q // 3
    return cnt_r + cnt_q * 3

   
if __name__ == "__main__":
    print(count_fancy_numbers(1))
    print(count_fancy_numbers(13))