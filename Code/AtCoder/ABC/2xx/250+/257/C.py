
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

sdata = list(map(int, list(input())))
idata = list(map(int, input().split()))

allOfOne = sdata.count(1)

data = []
for i in range(N):
    data.append((idata[i], sdata[i]))

data.sort()

allOfOne

maxCnt = allOfOne
curCnt = allOfOne



seki_val = 0

for i in range(N):
    next = i+1
    if next < N:
        if data[i][0] == data[next][0]:
            seki_val += 1 if data[i][1] == 0 else -1
            continue

    if seki_val != 0:
        curCnt += seki_val
        seki_val = 0
    

    if data[i][1] == 0:
        curCnt += 1
    else:
        curCnt -= 1
        
    maxCnt = max(curCnt, maxCnt)

print(maxCnt)