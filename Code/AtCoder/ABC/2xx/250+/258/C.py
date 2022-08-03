
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
S = input()

current = 0

for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        current += x
        current = current % N
    else :
        print(S[(N - current + x) % N - 1])
