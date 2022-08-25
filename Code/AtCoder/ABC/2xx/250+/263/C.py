from itertools import permutations #순열
from cmath import pi
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

N, M = map(int, input().split())

li = [i for i in range(1, M+1)]

ans = list(permutations(li, N))

result = []
for e in ans:
    for i in range(N-1):
        if not e[i] < e[i+1]:
            break
    else:
        result.append(e[:])


for e in result:
    for i in range(N):
        print(e[i], end=" ")
    print()
