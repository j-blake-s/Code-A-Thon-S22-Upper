#!/bin/python3
from collections import defaultdict as dd
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
assert all(len(line) == m for line in board)

seen = dd(lambda : (0,0))
trues = 0
falses = 0
concrete = {"T", "F"}
all_block = "L"
none_block = "N"
any_block = "Y"
same_block = "S"
answer = 0

for y in range(n-1, -1, -1):
    for x in range(m):
        before = board[y][x]
        if board[y][x] in concrete:
            seen[y, x] = board[y][x] == "T"
        elif board[y][x] == all_block:
            seen[y, x] = falses == 0
        elif board[y][x] == none_block:
            seen[y, x] = trues == 0
        elif board[y][x] == any_block:
            seen[y, x] = trues >= 1
        elif board[y][x] == same_block:
            seen[y, x] = trues == falses
        else:
            assert False
        board[y][x] = "T" if seen[y, x] == True else "F"
        answer += board[y][x] == "T" and board[y][x] != before

    trues += sum(x == "T" for x in board[y])
    falses += sum(x == "F" for x in board[y])
for y in range(n):
    print("".join(board[y]))
print(answer)