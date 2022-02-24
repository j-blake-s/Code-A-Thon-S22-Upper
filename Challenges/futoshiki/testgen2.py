from pathlib import Path
import os
import shutil
import zipfile
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', "--amount",choices=range(1, 10), type=int, default=1, help="number of new puzzles to scrape")
# parser.add_argument('-r', "--amount",choices=range(4, 10), type=int, default=1, help="number of new puzzles to scrape")
args = parser.parse_args()
# parser.add_argument('-d', "--diff", choices=range(4), default=1, type=int, help="difficulty of the puzzle scraped", required=False)
# Path("/my/directory").mkdir(parents=True, exist_ok=True)
in_out_folders = ["input", "output"]
if len(sys.argv) > 1 and sys.argv[1] == "reset":
    for folder in in_out_folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
#     # os.mkdir(folder)
#     command =f"cp -r samples{os.sep}{folder} ."
#     print(command)
#     os.system(command)
    # shutil.copy(os.path.join("samples", folder, "/"), "./")
Path("./input").mkdir(exist_ok=True)
Path("./output").mkdir(exist_ok=True)
cases_folder = "cases.zip"
if os.path.isfile(cases_folder):
    os.remove(cases_folder)


# exit()
# for i in range(3):
difficulty = 2
file_name_num = 0
size = 8
num_made = 0
failed = False
while num_made < args.amount:
    print(num_made)
    input_file = f"input/input{file_name_num}.txt"
    while os.path.isfile(input_file):
        # print(input_file, "already exists")
        file_name_num += 1
        input_file = f"input/input{file_name_num}.txt"
        continue
    
    failed |= os.system(f"python ./automation_utils/scraper/scrape_boards.py scrape -s {size} -d {difficulty}")
    failed |= os.system(f"python ./automation_utils/scraper/scrape_boards.py input > input/input{file_name_num}.txt")
    failed |= os.system(f"python ./automation_utils/scraper/scrape_boards.py output > output/output{file_name_num}.txt")
    # failed |= os.system(f"python ./automation_utils/make_easier.py")
    assert not failed
        
    file_name_num += 1
    num_made += 1

failed |= os.system(f"python ./automation_utils/make_easier.py")
assert not failed
    # shutil.make_archive(cases_folder.removesuffix(".zip"), 'zip', )
with (zipfile.ZipFile(cases_folder, "w")) as zf:
    for folder in in_out_folders:
        for dirname, subdirs, files in os.walk(folder):
            zf.write(dirname)
            for filename in files:
                zf.write(os.path.join(dirname, filename))
zf.close()