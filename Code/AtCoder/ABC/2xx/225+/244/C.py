
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

arr = [False] * (2*N+1+1)

print(1)
arr[0] = True
arr[1] = True

val = int(input())
while val != 0:
    arr[val] = True
    curIdx = arr.index(False)
    print(curIdx)
    arr[curIdx] = True
    sys.stdout.flush()
    val = int(input())