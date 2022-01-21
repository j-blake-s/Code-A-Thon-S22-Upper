import math
cases = int(input())
for _ in range(cases):
    n, gap, letters_allowed = map(int, input().split())
    if n % 2 != gap % 2 or gap % 2 == 0:
        print(0)
        continue
    even_letter_count = letters_allowed // 2
    odd_letter_count = math.ceil(letters_allowed / 2)
    first_len = (n - gap) //2
    to_mid = math.ceil(gap / 2) 
    ret = odd_letter_count * ((odd_letter_count - 1) ** (first_len -1))
    ret *= even_letter_count * ((even_letter_count - 1) ** (to_mid-1))
    
    print(ret)
