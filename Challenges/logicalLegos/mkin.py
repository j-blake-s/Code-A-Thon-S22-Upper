#!/bin/python3
import random
case_num = int(input())
random.seed(case_num)
# 0 and 1 are the sample cases
if case_num == 0:
    print(3, 4)
    print('''
FLNY
FLYF
TTTT'''.lstrip())
elif case_num == 1:
    print(5, 4)
    print('''
NTFT
YTSS
FTTT
TLNT
FFFF'''.lstrip())
elif case_num == 2:
    print(2, 4)
    print('''
NYLS
LYNS'''.lstrip())
elif case_num <= 15:
    y = random.randint(10, 20)
    x = random.randint(3, 6)
    print(y, x)
    options = ["T","F","L","N","Y","S"]
    weights = [.3, .3, .1,.1,.1,.1]
    for _ in range(y):
        print("".join(random.choices(options, weights=weights,k=x)))
else:
    y = random.randint(25000, 32000) // 2 * 2
    x = random.randint(3, 6) * 2
    print(y, x)
    options = ["T","F","L","N","Y","S"]
    weights = [.4, .4, .05,.05,.05,.05]
    bottom_size = 1000
    bottom_options = [
            "T"*x,
            "F"*x,
            "FL"*(x//2),
            "FY"*(x//2),
            "TL"*(x//2),
            "TF"*(x//2),
            "SF"*(x//2)
        ]
    # if x % 4 == 0:
    bottom = random.choice(bottom_options)
    # start = random.randint()
    for _ in range(y-bottom_size):
        print("".join(random.choices(options, weights=weights,k=x)))
    for _ in range(bottom_size):
        print(bottom)
    
    # output what should be read in as input by
    # contestant code
    # n = randint(3, 100000)
    # j = randint(3, 2 ** 25)
    # print(n, j)
