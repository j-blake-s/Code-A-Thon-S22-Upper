from copy import deepcopy
from collections import defaultdict as dd, deque
# a = AdventInput('input.txt')
# inp = a.data
# start = dd(lambda : {})

def prune_row_and_col(y, x, number, cur_board):
    come_back = []
    for row_pos in range(n):
        if row_pos == x:
            continue
        before = len(cur_board[y, row_pos])
        cur_board[y, row_pos].discard(number)
        if len(cur_board[y, row_pos]) == 0:
            return False
        after = len(cur_board[y, row_pos])
        if before != after and after == 1:
            come_back.append((y, row_pos))
    for col_pos in range(n):
        if col_pos == y:
            continue
        before = len(cur_board[col_pos, x])
        cur_board[col_pos, x].discard(number)
        if len(cur_board[col_pos, x]) == 0:
            return False
        after = len(cur_board[col_pos, x])
        if before != after and after == 1:
            come_back.append((col_pos, x))
    for new_y, new_x in come_back:
        works = prune_row_and_col(new_y, new_x, list(cur_board[new_y, new_x])[0], cur_board)
        if not works:
            return False
        # if len(cur_board[col_pos, x]) == 1:
    return True

n = int(input())
board = dd(lambda : {i for i in range(1, n + 1)})
for y in range(n):
    cur = input()
    for x in range(n):
        if cur[x] != "#":
            number = int(cur[x])
            board[y, x] = {number}
            good = prune_row_and_col(y, x, number, board)
            assert good == True

greater = dd(list)
less = dd(list)
m = int(input())
for j in range(m):
    y1, x1, y2, x2 = list(map(int,input().split()))
    greater[y1, x1].append((y2, x2))
    board[y1, x1].discard(1)
    less[y2, x2].append((y1, x1))
    board[y2, x2].discard(n)

fringe = deque()
for y in range(n):
    for x in range(n):
        fringe.extend(greater[y, x])
        fringe.extend(less[y, x])

        if len(board[y, x]) != 1:
            continue
        only = list(board[y, x])[0]
        for adjy, adjx in greater[y, x]:
            for k in range(only, n + 1):
                board[adjy, adjx].discard(k)
        for adjy, adjx in less[y, x]:
            for k in range(1, only + 1):
                board[adjy, adjx].discard(k)

# print(fringe)
# print(less)
# for k, v in sorted(board.items()):
#     print(k, v)
while fringe:
    y, x = fringe.popleft()
    for y2, x2 in greater[y, x]:
        before = len(board[y2, x2])
        # print(board[y, x])
        for i in range(max(board[y, x]), n + 1):
            board[y2, x2].discard(i)
        after = len(board[y2, x2])
        if before != after:
            fringe.append((y2, x2))
    for y2, x2 in less[y, x]:
        before = len(board[y2, x2])
        # print(board[y, x])
        for i in range(1, min(board[y, x]) + 1):
            board[y2, x2].discard(i)
        after = len(board[y2, x2])
        if before != after:
            fringe.append((y2, x2))
    # print("cur")
    # print(board[])
for y in range(n):
    for x in range(n):
        if len(board[y, x]) == 1:
            prune_row_and_col(y, x, list(board[y, x])[0], board)
# print("after")
# for k, v in sorted(board.items()):
#     print(k, v)
# exit()
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
        good = True
        state = deepcopy(start)
        state[y, x] = {possible}
        for adjy, adjx in greater[y, x]:
            for k in range(possible, n + 1):
                state[adjy, adjx].discard(k)
        for adjy, adjx in less[y, x]:
            for k in range(1, possible + 1):
                state[adjy, adjx].discard(k)

        good = prune_row_and_col(y, x, possible, state)
        if not good:
            continue
        
        works = solve(state, pos + 1)
        if works:
            return True

# print(board)
solve(board, 0)