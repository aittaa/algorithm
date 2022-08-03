
from collections import deque
import math
import heapq
from bisect import bisect_left, bisect_right
import sys
import zipfile

# input = sys.stdin.readline
def input() :
    return sys.stdin.readline().rstrip()
    
dx = (1, 0, -1, 0, 1, -1, -1, 1)
dy = (0, -1, 0, 1, -1, -1, 1, 1)

INF = float('inf')

# sys.setrecursionlimit(10**7)

###

N = int(input())
data = [0] + [int(input()) for _ in range(N)]

DP = [0] * (N+1)

DP[1] = data[1]
DP[2] = data[1] + data[2]
DP[3] = max(data[1] + data[2], data[1] + data[3], data[2] + data[3])

for i in range(4, N+1):
    DP[i] = max(DP[i-2] + data[i], DP[i-3] + data[i-1] + data[i], DP[i-1])


print(DP[N])