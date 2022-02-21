#!/bin/python3
n = int(input())
lines = [input() for _ in range(n)]

total = 0
prev = 0
for y in range(n):
    c_cooldown = 0
    c_start = -1
    h_cooldown = 0
    h_start = -1
    h_stop = -1
    cur_line_count = 0
    for x in range(len(lines[y])):
        if lines[y][x] == 'B':
            total += 1
        elif lines[y][x] == 'A':
            #if against the right wall, don't count a non existant person
            total += 1 + min(len(lines[y])-1 - x, 1)
        elif lines[y][x] == 'L':
            #if against the left wall, don't count up to two non existant people
            total += 1 + min(x, 2)
        elif lines[y][x] == 'C':
            if c_cooldown == 0:
                c_cooldown = 6
                c_start = x
            else:
                total += (x - c_start) + 1
                c_cooldown = 0
        elif lines[y][x] == 'H':
            h_stop = x
            if h_cooldown > 0:
                total += (h_stop - h_start)
            else:
                total += 1

            h_cooldown = 4
            h_start = x
        h_cooldown = max(h_cooldown - 1, 0)
        c_cooldown = max(c_cooldown - 1, 0)
    # print("------")
    cur_line_count = total - prev
    prev = total
    # print(cur_line_count)
                # total += (x - h_start) + 1
            # h_cooldown = 3
            # h_start = x
print(total)