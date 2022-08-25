
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

N, M, T = map(int, input().split())
A = list(map(int, input().split()))

for i in range(M):
    X, Y = map(int, input().split())
    A[X-1] -= Y


if N == 2:
    print("Yes")
    exit(0)

for i in range(0, N-1):

    T -= A[i]

    if T <= 0:
        print("No")
        exit(0)


print("Yes")