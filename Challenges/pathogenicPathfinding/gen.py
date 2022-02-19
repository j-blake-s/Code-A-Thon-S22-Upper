import sys
import os
from random import seed
import random
from networkx.generators.random_graphs import erdos_renyi_graph

 
def sample_case(num):
  if num == 0:
    print("5 5 2")
    print("A B 1\nB C 1\nB D 7\nC E 1\nD E 6\nA E\nA D")
  if num == 1:
    print("10 18 4")
    print("A B 5\nA C 7\nA D 3\nB C 10\nC D 10\nB F 3\nC F 2\nC G 4\nC H 5")
    print("D H 1\nD I 8\nB E 5\nF E 3\nF G 5\nH G 2\nH I 2\nE G 1\nG I 7")
    print("A A\nA G\nA E\nA F")

def gen(n,q,p=0.1):
  g = erdos_renyi_graph(n, p)
  print(n,len(g.edges),q)

  for f,t in g.edges:
    print(hex(f),hex(t),random.randint(1,1000))

  for _ in range(q):
    fi = random.randint(0,n-1)
    ti = random.randint(0,n-1)
    print(hex(fi),hex(ti))

def main():
  case_num = int(input())
  seed(case_num)

  # Easy
  if case_num <= 1:
    sample_case(case_num)
  elif case_num < 7:
    gen(10,5,0.5)
  elif case_num < 17:
    gen(50,200,0.3)
  elif case_num < 27:
    gen(150,5000,0.2)
  elif case_num <= 32:
    gen(255,5000,0.1)


if __name__ == "__main__":
  main()