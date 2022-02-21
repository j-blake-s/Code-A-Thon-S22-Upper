from itertools import permutations
from collections import defaultdict as dd, Counter
from copy import deepcopy
'''
this naive solution ignores the alligators and 
just finds a permutation that works for each
line

INCOMPLETE
'''


n = int(input())
dummy = "#"
board = [[int(x) if x.isdigit() else x for x in input() ] for _ in range(n)]
sign_count = int(input())
this_greater_than_that = dd(set)
this_less_than_that = dd(set)
for i in range(sign_count):
    y1, x1, y2, x2 = map(int, input().split())
    this_greater_than_that[y1, x1].add((y2, x2))
    this_less_than_that[y2, x2].add((y1, x1))
all_nums = set(range(1, n+1))
#print(this_less_than_that)
# exit()

def has_compare_contradiction(line_num, temp):
    ## print(line_num)
    for x in range(n):
        for other_y, other_x in this_greater_than_that[line_num, x]:
            if temp[other_y][other_x] == dummy:
                continue
            if temp[line_num][x] < temp[other_y][other_x]:
                #print("greater contradiction")
                return True
        
        for other_y, other_x in this_less_than_that[line_num, x]:
            if temp[other_y][other_x] == dummy:
                continue
            if temp[line_num][x] > temp[other_y][other_x]:
                #print(temp[line_num][x], temp[other_y][other_x])
                #print(f"{line_num}, {x} less contradiction {other_y} {other_x}")
                return True
    return False

def has_col_contradiction(temp_board):
    for x in range(n):
        counts = Counter([temp_board[y][x] for y in range(n)])
        counts[dummy] = 0
        #print(counts)
        if any(value >= 2 for value in counts.values()):
            #print("had col contradiction")
            return True
    return False


#TODO check for line contradiction

answers = [] 
def get_perm(line_num, temp_board):
    if line_num == n:
        return temp_board
    remaining = all_nums - set(board[line_num])
    #print(remaining)
    for perm in permutations(remaining):
        pos = 0
        cur_board = deepcopy(temp_board)
        for x in range(n):
            if cur_board[line_num][x] == dummy:
                cur_board[line_num][x] = perm[pos]
                pos += 1
        # for line in cur_board:
            #print(line)
        #print("------")
        if has_compare_contradiction(line_num, cur_board) or\
            has_col_contradiction(cur_board):
            continue
        attempt = get_perm(line_num + 1, cur_board)
        if attempt is not None:
            answers.append(attempt)

run = get_perm(0, board)
# print(answers)
for line in (answers[0]):
    print(*line, sep='')