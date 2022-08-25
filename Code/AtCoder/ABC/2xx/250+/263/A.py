
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

A, B, C, D, E = map(int, input().split())

d = []

d.append(A)
d.append(B)
d.append(C)
d.append(D)
d.append(E)

s = set()
s = set(d)


if len(s) == 2 and (d.count(d[1]) == 2 or d.count(d[1]) == 3):
    print("Yes")
else:
    print("No")
