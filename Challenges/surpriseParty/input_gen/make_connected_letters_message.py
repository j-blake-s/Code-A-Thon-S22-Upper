#!/bin/python3
import re
import random
import string
import sys
'''
solved with:
(B|C.{,4}?C|(H.{,2})+H|A.|..L)
((B)|(C.{,4}?C)|((H.{,2})+H)|(A.)|(..L))

Find all:
B
C's that are within a horizontal distance of 5 of another C (count those between them as well) (they are only in partners, found according to top to bottom, left to right order)
H's that are within a group (horizontal distance of 3 of another H)
A clues in the person immediately to their right
L clues in the two people immediately to the left
'''

random.seed(6)
all_letters = ('ABC')
after_letter = 'A'
single_letter = 'B'
space_between_letter = 'C'
chain_letter = 'H'
before_letter = 'L'
used = [after_letter,
single_letter,
space_between_letter,
chain_letter,
before_letter]
dummy_letters = set(string.ascii_uppercase) - set(used)
dummy_letters = list(dummy_letters)
max_dist = 3
# with open("../image_text/from_main_as_data.txt") as f:
#     data = f.read()
# stream = input()
# data = sys.stdin.read()
line_count = int(input())
data = [input() for _ in range(line_count)]
data = "\n".join(data)
# print(data)

def needed_replacement(s):
    if isinstance(s, re.Match):
        s = s.group(0)
    if not s:
        return ''
    if len(s) == 1:
        return single_letter
    options = [
        single_letter *len(s), 
        space_between_letter + "".join(random.choices(dummy_letters, k=len(s)-2)) + space_between_letter
        ]

    if len(s) % 2 == 0:
        options.append(
            (after_letter + random.choice(dummy_letters))*
            (len(s)//2))
    if len(s) >= 3:
        options.append("".join(random.choices(dummy_letters, k=2)) + before_letter)
    # else:
        # options.append()
    chosen =random.choice(options)
    return chosen + needed_replacement(s[len(chosen):])

def chained_replace(s):
    s = s.group(0)
    if random.randint(0, 2):
        return s
    ret = ''
    while s:
        if len(s) >= 4:
            ret += chain_letter + "".join(random.choices(dummy_letters,k=2)) + chain_letter
            s = s[4:]
        elif len(s) >= 3:
            ret += chain_letter + random.choice(dummy_letters) + chain_letter
            s = s[3:]
        else:
            ret += chain_letter * len(s)
            s = ''
    return ret
    # return "".join(key_letter if i % max_dist == 0 else random.choice(list(all_letters)) for i, x in enumerate(s))[:-1] + key_letter

# data = data.replace("1", " ")
pat = r"(?<!0..|.0.|..0)0{2,5}"
first_sub = re.sub(pat, chained_replace, data)
first_sub = re.sub(r"0{2,6}", needed_replacement, first_sub)
first_sub = first_sub.replace("0", single_letter)
# print(first_sub)
# dummy_letters = list(dummy_letters)
final = re.sub("1", lambda x: random.choice(dummy_letters), first_sub)
# final = re.sub("1", " ", first_sub)
# print(pat)
print(len(data.strip().split("\n")))
print(final)
# print(new)