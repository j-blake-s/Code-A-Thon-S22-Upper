#!/usr/local/bin/python3
import random
case_num = int(input())
random.seed(case_num + 42)
# 0 and 1 are the sample cases
if case_num < 2:
    n = random.randint(3, 9)
    g = random.randint(2, 9)
elif case_num <= 15:
    n = random.randint(1, 500)
    g = random.randint(1, 1000)


else:
    # output what should be read in as input by
    # contestant code
    n = random.randint(90000, 100000)
    g = random.randint(90000, 100000)

print(n, g)
nums = [random.randint(case_num, 95) for _ in range(n)]
gifts = [random.choices([random.choice(nums), random.randint(96, 100)], k=1)[0] for _ in range(g)]
print(*nums)
print(*gifts)
# for gift in gifts:
    # print(gift)