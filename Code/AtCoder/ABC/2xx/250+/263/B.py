
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
P = [1, 1] + list(map(int, input().split()))

if N == 2:
    print(1)
    exit(0)

cnt = 1
current = P[N]
target = 1

if P[N] == 1:
    print(1)
    exit(0)
    
while P[current] != target:
    cnt += 1
    current = P[current]


print(cnt+1)