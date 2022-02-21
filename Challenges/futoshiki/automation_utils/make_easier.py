import re
import random
import os
folders = ["input", "output"]
file_dir = os.path.dirname(__file__)
for i in range(20, 50):
    input_file_loc = f'{file_dir}/../input/input{i}.txt'
    output_file_loc = f'{file_dir}/../output/output{i}.txt'
    try:
        with open(input_file_loc) as inp, open(output_file_loc) as out:
            all_in_data = inp.read()
            inp_lines = all_in_data.splitlines()
            n = int(inp_lines[0])
            board = [list(line) for line in inp_lines[1:n +1]]
            rest = inp_lines[n+1:]
            mouths = set(rest[1:])
            out_lines = out.read().strip().splitlines()
        # print(rest)
        look_ahead = 4
        cooldown = 0
        for y in range(len(out_lines)):
            for x in range(len(out_lines[y]) - 1):
                pot = f"{y} {x} {y} {x+1}"
                if pot not in mouths and out_lines[y][x] > out_lines[y][x+1]:
                    rest.append(pot)
                    rest[0] = str(int(rest[0]) + 1)
                if not cooldown and re.fullmatch("#"*look_ahead, inp_lines[y+1][x:x+look_ahead]):
                    x = random.randint(x, x + look_ahead - 1)
                    board[y][x] = out_lines[y][x]
                    cooldown += 1
                    continue
                cooldown = max(cooldown - 1, 0)
                # print(cooldown)
        for y in range(len(out_lines)-1):
            for x in range(len(out_lines[y])):
                pot = f"{y} {x} {y+1} {x}"
                if pot not in mouths and out_lines[y][x] > out_lines[y+1][x]:
                    rest.append(pot)
                    rest[0] = str(int(rest[0]) + 1)

        with open(input_file_loc, 'w') as f:
            print(n, file=f)
            print("\n".join("".join(line) for line in board), file=f)
            print("\n".join(rest), file=f)
    except FileNotFoundError:
        print("done")
        break