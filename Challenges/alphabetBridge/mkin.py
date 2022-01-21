#!/usr/local/bin/python3
from random import randint, seed
case_num = int(input())
seed(117 + case_num)
# 0 and 1 are the sample cases
if case_num == 0:
    print(4)
    print(3, 1, 2)
    print(5, 2, 4)
    print(6, 2, 5)
    print(7, 3, 6)
elif case_num == 1:
    print(1)
    print(7, 3, 7)
elif case_num <= 10:
    case_count = randint(3, 5)
    print(case_count)
    for j in range(case_count):
        # while True:
        n = (randint(2, 5) * 2 + 1) if j % 2== 0 else randint(5, 8)
        g = randint(1, n-2)
        if n % 2== 0 and g % 2 == 0:
            n += 1
            g += 1
        l = randint(3, 8)
        print(n, g, l)
else:
    # output what should be read in as input by
    # contestant code
    case_count = randint(3, 8) if case_num < 25 else randint(10, 14)
    print(case_count)
    for _ in range(case_count):
        while True:
            n = min(20, randint(3, case_num//3 + 7))
            for _ in range(3):
                if n % 2 == 0:
                    n += randint(0,1)
                else:
                    break
            g = 1 + randint(0, (n-2)//2) * 2
            # if (n -1) % 4 == 0:


            # g += (randint(0, 2))
            options = [max(4, case_num//3), 26]
            lo, hi = min(options), max(options)
            l = randint(lo, hi)
            if case_num >= 49:
                if n + l in range(38, 48):
                    break
                continue
            if (n + l) in range(max(3, case_num //2), 37) and g < n:
                break
        print(n, g, l)
