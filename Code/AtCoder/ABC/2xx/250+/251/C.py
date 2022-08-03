
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

for i in range(N):
    s, t = input().split()
    t = int(t)
    
    if not s in data:
        data[s] = (t, i+1)
    

result = sorted(list(data.values()), key=lambda x: (x[0], -x[1]))

print(result[-1][1])
