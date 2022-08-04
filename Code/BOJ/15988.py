

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

DP = [0] * (1000000+1)

DP[1] = 1
DP[2] = 2
DP[3] = 4
DP[4] = 7

for i in range(5, 1000000+1):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    DP[i] = DP[i] % 1000000009

for i in range(N):
    idx = int(input())
    print(DP[idx])
