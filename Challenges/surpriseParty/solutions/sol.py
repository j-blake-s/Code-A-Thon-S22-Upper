#!/bin/python3
import re
n = int(input())
lines = [input() for _ in range(n)]
full = "\n".join(lines)
pat = r"B|C.{0,4}?C|(?:H.{0,2})+H|A.|..L"
found = (re.findall(pat, full))
new = ["".join(x) for x in found]
print(sum(len("".join(x)) for x in found))
