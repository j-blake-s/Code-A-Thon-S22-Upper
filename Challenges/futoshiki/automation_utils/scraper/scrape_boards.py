from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
import math
import sys
import argparse
import os
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
script_dir = os.path.dirname(os.path.realpath(__file__))

OG_BOARD_FILE = "temp.html"

def get_nums(file):
    with open(os.path.join(script_dir, file)) as f:
        html_to_read = f.read()
        nums = [x or "#" for x in re.findall(r"32px\">\s+(\d?)\s+</td>", html_to_read)]
    n = int(math.sqrt(len(nums)))
    # print(n)
    nums = "".join(nums)
    return "\n".join(re.findall(rf".{{{n}}}", nums))
    # for g in groups:
        # print(g)

def show_signs():
    with open(os.path.join(script_dir, OG_BOARD_FILE)) as f:
        html = f.read()
    arrows = re.findall(r"(\d)-(\d)(.).*(.)0\.gif", html)
    greater = []
    less_to_other = {
        "l" : lambda a, b : (a, b + 1, a, b),
        "r" : lambda a, b : (a, b, a, b + 1),
        "d" : lambda a, b : (a, b, a + 1, b),
        "u" : lambda a, b : (a + 1, b, a, b),
    }
    for gy, gx, _, less_side in arrows:
        # dy, dx = less_to_other[less_side]
        gy = int(gy)
        gx = int(gx)
        greater.append(less_to_other[less_side](gy, gx))
    print(len(greater))
    for g in greater:
        print(*g)

def scrape(size=4, difficulty=1):
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.futoshiki.org/")
    elem = driver.find_element_by_id("ssize")
    elem.send_keys(Keys.RETURN)
    for _ in range(size - 4):
        elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_id("sdif")
    elem.send_keys(Keys.RETURN)
    if difficulty == 0:
        elem.send_keys(Keys.UP)
    elif difficulty >= 2:
        for _ in range(difficulty - 2):
            elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    elem = driver.find_element_by_id("board")
    html = elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, "lxml")
    pretty = soup.prettify()
    with open(os.path.join(script_dir, OG_BOARD_FILE), 'w') as f:
        f.write(pretty)

    elem = driver.find_element_by_id("info")
    elem = elem.find_element_by_class_name("button")
    elem.send_keys(Keys.ENTER)

    time.sleep(1)
    elem = driver.find_element_by_id("board")
    html = elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, "lxml")
    pretty = soup.prettify()
    with open(os.path.join(script_dir, "temp_sol.html"), 'w') as f:
        f.write(pretty)
    # driver.quit()
    # driver.close()
    # driver.quit()

# print(pretty)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["input", "output", "scrape", "all"], help="indicates what action to take",nargs="?",const=1, default="all")
    parser.add_argument('-s', "--size",choices=range(4, 10), type=int, default=4, help="size of the puzzle scraped")
    parser.add_argument('-d', "--diff", choices=range(4), default=1, type=int, help="difficulty of the puzzle scraped", required=False)
    # parser.add_argument("-output",help='outputs to STDOUT the solution to a scraped puzzle', action='store_true')
    # parser.add_argument("-input", help='outputs to STDOUT the input for a scraped puzzle',action='store_true')
    # parser.add_argument("-scrape",help='scrapes a puzzle', action='store_true')
    args = parser.parse_args()
    # print(os.path.realpath(__file__))

    if args.mode == 'input':
        start = get_nums(OG_BOARD_FILE)
        print(len(start.splitlines()))
        print(start)
        show_signs()
    elif args.mode == "output":
        solution = get_nums("temp_sol.html")
        print(solution)
    elif args.mode == "scrape":
        scrape(args.size, args.diff)
    else:
        scrape(args.size, args.diff)
        start = get_nums(OG_BOARD_FILE)
        print(len(start.splitlines()))
        print(start)
        show_signs()
        print()
        solution = get_nums("temp_sol.html")
        print(solution)

    # driver.quit()
    # exit()
