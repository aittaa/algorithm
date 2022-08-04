

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

N, Q = map(int, input().split())

data = [i for i in range(1, N+1)]
Query = [ int(input()) for _ in range(Q) ]

pos = { i:i-1 for i in range(1, N+1)}

for q in Query:
    
    idx = pos[q]

    if idx < N-1:
        data[idx], data[idx+1] = data[idx+1], data[idx]
        pos[q] += 1
        pos[data[idx]] -= 1
        
    else:
        data[idx], data[idx-1] = data[idx-1], data[idx]
        pos[q] -= 1
        pos[data[idx]] += 1


print(" ".join(map(str, data)))