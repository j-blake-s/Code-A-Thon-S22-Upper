#!/bin/python3
import re
n = int(input())
lines = [input() for _ in range(n)]
# print(lines)
full = "\n".join(lines)
pat = r"B|C.{0,4}?C|(?:H.{0,2})+H|A.|..L"
found = (re.findall(pat, full))
# print(found)
# print(len(found))
new = ["".join(x) for x in found]
# print(new)
    # print()
print(sum(len("".join(x)) for x in found))
