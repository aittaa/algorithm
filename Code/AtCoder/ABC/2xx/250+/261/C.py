
from collections import deque
import math
import heapq
from bisect import bisect_left, bisect_right
import sys

# input = sys.stdin.readline
def input() :
    return sys.stdin.readline().rstrip()
    
dx = (1, 0, -1, 0, 1, -1, -1, 1)
dy = (0, -1, 0, 1, -1, -1, 1, 1)

INF = float('inf')

# sys.setrecursionlimit(10**7)

###


N = int(input())
data = {}


for _ in range(N):

    s = input()
    
    if s in data:
        data[s] += 1
        print(f"{s}({data[s]})")
    else:
        data[s] = 0
        print(s)