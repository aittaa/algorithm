
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

N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

for i in range(N):

    if K < 1: break

    if A[i] // X != 0:
        if X*K > A[i]:
            K -= A[i]//X
            A[i] = A[i]%X
        else:
            A[i] -= X*K
            K = 0

A.sort(reverse=True)

for i in range(N):

    if K < 1: break
    A[i] = 0
    K -= 1

print(sum(A))

    
    
