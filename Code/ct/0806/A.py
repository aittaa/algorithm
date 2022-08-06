
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

S = input()

col = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]

maxCol = -1


for i in range(len(col)):
    if col[i] in S:
        maxCol = i

if maxCol != -1:
    print(col[maxCol])
else:
    print(maxCol)
