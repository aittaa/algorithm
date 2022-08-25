
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

N, L, R = map(int, input().split())
A = [0] + list(map(int, input().split()))


arrL = [0] + ([0] * N)
arrR = [0] + ([0] * N)

for i in range(1, N+1):
     arrL[i-1] 

     arrL[i] = arrL[i-1] + L - A[i]


for i in range(1, N+1):
     arrR[i-1] 

     arrR[i] = arrR[i-1] + R - A[(N+1) - i]

print(arrL)
print(arrR)

maxVal = -INF

for i in range(1, N+1):
    maxVal = max(maxVal, arrL[i] + arrR[N-(i-1)])

print(maxVal)