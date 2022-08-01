

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
DP = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    DP[0][i] = 1

for i in range(1, N):
    for j in range(10):
        up = j + 1
        down = j - 1
    
        DP[i][j] += DP[i-1][up] if up < 10 else 0
        DP[i][j] += DP[i-1][down] if down >= 0 else 0

print(sum(DP[N-1]) % 1000000000)
