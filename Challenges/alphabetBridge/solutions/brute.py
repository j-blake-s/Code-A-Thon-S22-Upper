from itertools import combinations_with_replacement, permutations, product
# from more_itertools import distinct_permutations
import string
import re
import math

cases = int(input())
for _ in range(cases):
    n, gap, num_letters_allowed = map(int, input().split())
    ret = 0
    if n % 2 != gap % 2 or gap % 2 == 0:
        print(0)
        continue
    allowed_letters = set(string.ascii_uppercase[:num_letters_allowed])

    letters = string.ascii_uppercase[:num_letters_allowed]
    seen = set()
    for x in (product(letters, repeat=n)): 
        if x in seen:
            continue
        seen.add(x)
        bin_form = "".join(str(ord(letter)%2) for letter in x)
        if x == x[::-1] and all(x[j] != x[j+1] for j in range(len(x)-1)) and re.fullmatch(rf"1+0{{{gap}}}1+", bin_form):
            ret += 1
            # print("".join(x))
            # print(bin_form)

    print(ret)


