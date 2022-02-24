#!/bin/python3
import re
n = int(input())
lines = [input() for _ in range(n)]
# print(lines)
full = "\n".join(lines)
def sub_out(x):
    return "#"*len(x.group())
def swap(x):
    # print(x.group())
    
    if x.group() == "#":
        return full[x.span()[0]:x.span()[1]]
    else:
        return " " * len(x.group())
        
pat = r"B|C.{0,4}?C|(?:H.{0,2})+H|A.|..L"
found = (re.sub(pat, sub_out, full))
print(found)
swap = (re.sub(r".", swap, found))
# print(found)
print(swap)
# print(found)
# print(len(found))
# new = ["".join(x) for x in found]
# print(new)
    # print()
# print(sum(len("".join(x)) for x in found))
