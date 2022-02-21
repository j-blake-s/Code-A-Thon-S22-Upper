from copy import deepcopy
from collections import defaultdict as dd
# a = AdventInput('input.txt')
# inp = a.data
# start = dd(lambda : {})
n = int(input())
board = dd(lambda : {i for i in range(1, n + 1)})
for y in range(n):
    cur = input()
    for x in range(n):
        if cur[x] != "#":
            number = int(cur[x])
            board[y, x] = {number}
            for row_pos in range(n):
                if row_pos == x:
                    continue
                board[y, row_pos].discard(number)
            for col_pos in range(n):
                if col_pos == y:
                    continue
                board[col_pos, x].discard(number)

greater = dd(list)
less = dd(list)
m = int(input())
for y in range(m):
    y1, x1, y2, x2 = list(map(int,input().split()))
    greater[y1, x1].append((y2, x2))
    board[y1, x1].discard(1)
    less[y2, x2].append((y1, x1))
    board[y2, x2].discard(n)
for y in range(n):
    for x in range(n):
        if len(board[y, x]) != 1:
            continue
        only = list(board[y, x])[0]
        for adjy, adjx in greater[y, x]:
            for k in range(only, n + 1):
                board[adjy, adjx].discard(k)
        for adjy, adjx in less[y, x]:
            for k in range(1, only + 1):
                board[adjy, adjx].discard(k)

times_run = 0
highest = 0
def solve(start, pos):
    # print(pos)
    global highest
    # highest = max(highest, pos)
    if pos > highest:
        highest = pos
        # print(highest)
    global times_run
    if pos == n ** 2:
        # print(start)
        for y in range(n):
            for x in range(n):
                assert len(start[y, x]) == 1
                print(start[y, x].pop(), end='')
            print()
        # exit()
        times_run += 1
        assert times_run == 1
        return start
    y, x = divmod(pos, n)
    for possible in start[y, x]:
        # print(possible)
        stop = False
        state = deepcopy(start)
        state[y, x] = {possible}
        for adjy, adjx in greater[y, x]:
            for k in range(possible, n + 1):
                state[adjy, adjx].discard(k)
        for adjy, adjx in less[y, x]:
            for k in range(1, possible + 1):
                state[adjy, adjx].discard(k)

        for row_pos in range(n):
            if row_pos == x:
                continue
            state[y, row_pos].discard(possible)
            if len(state[y, row_pos]) == 0:
                stop = True
        if stop:
            continue
        for col_pos in range(n):
            if col_pos == y:
                continue
            state[col_pos, x].discard(possible)
            if len(state[col_pos, x]) == 0:
                stop = True
        if stop:
            continue
        works = solve(state, pos + 1)
        if works:
            return True

# print(board)
solve(board, 0)