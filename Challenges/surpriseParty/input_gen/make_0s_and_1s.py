#!/bin/python3
import random

case_num = int(input())
random.seed(case_num)
# y = int(input())
# x = int(input())
if case_num <= 15:
    x = random.randint(10, 20)
    y = random.randint(10, 20)
else:
    x = random.randint(10, 12) * 5
    y = random.randint(10, 22) * 10


# print(x, y)

options = ["0", "1"]
print(y)
for _ in range(y):
    cur_line = ''
    while len(cur_line) < x:
        chosen =random.choice(options)
        amount = min(x-len(cur_line), random.randint(1,5))
        cur_line += chosen * amount
    print(cur_line)

