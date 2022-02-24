from pathlib import Path
import os
import shutil
import zipfile
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-a', "--amount",choices=range(1, 50), type=int, default=30, help="number of new puzzles to scrape")
# parser.add_argument('-r', "--amount",choices=range(4, 10), type=int, default=1, help="number of new puzzles to scrape")
args = parser.parse_args()
in_out_folders = ["./input", "./output"]
# if len(sys.argv) > 1 and sys.argv[1] == "reset":
for folder in in_out_folders:
    if os.path.exists(folder):
        shutil.rmtree(folder)

# Path("./input").mkdir(exist_ok=True)
shutil.copytree("./samples/input/", "./input/")
# shutil.copytree("./samples/output/", "./output/")
Path("./output").mkdir(exist_ok=True)
# exit()
cases_folder = "cases.zip"
if os.path.isfile(cases_folder):
    os.remove(cases_folder)

file_name_num = 0
num_made = 0
failed = False
while num_made < args.amount:
    print(num_made)
    input_file = f"input/input{file_name_num}.txt"
    output_file = f"output/output{file_name_num}.txt"
    if not os.path.exists(f"./{input_file}"):
        failed |= os.system(f"echo {num_made} | python input_gen\make_0s_and_1s.py | python input_gen\make_connected_letters_message.py > {input_file}")
    output = subprocess.check_output(f"python solutions/sol.py < {input_file}", shell=True)
    output2 = subprocess.check_output(f"python solutions/sol_non_regex.py < {input_file}", shell=True)
    assert output == output2, f"{output}, {output2}"
    failed |= subprocess.call(f"python solutions/sol.py < {input_file} > {output_file}", shell=True)
    assert not failed
        
    file_name_num += 1
    num_made += 1

# failed |= os.system(f"python ./automation_utils/make_easier.py")
assert not failed
    # shutil.make_archive(cases_folder.removesuffix(".zip"), 'zip', )
with (zipfile.ZipFile(cases_folder, "w")) as zf:
    for folder in in_out_folders:
        for dirname, subdirs, files in os.walk(folder):
            zf.write(dirname)
            for filename in files:
                zf.write(os.path.join(dirname, filename))
zf.close()