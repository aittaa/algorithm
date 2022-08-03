
from collections import deque
from curses import A_STANDOUT
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
A = list(map(int, input().split()))

data = [ [] for _ in range(K)]

A_sorted = sorted(A[:])

if K == 1:
    print("Yes")
    exit(0)


for i in range(N):
    data[i%K].append(A[i])

for i in range(K):
    data[i].sort()

result = [0] * N
for i in range(N):
    result[i] = data[i%K][i//K]


if result == A_sorted:
    print("Yes")
else:
    print("No")


