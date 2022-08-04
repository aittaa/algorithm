
from itertools import combinations #조합

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

N, K = map(int, input().split())
S = [input() for _ in range(N)]

maxVal = 0

for subset in range(1 << N):

    s = [0]*26
    
    for i in range(N):
        if subset >> i & 1:
            for c in S[i]:
                idx = ord(c) - ord('a')
                s[idx] += 1

    maxVal = max(maxVal, s.count(K))

print(maxVal)
