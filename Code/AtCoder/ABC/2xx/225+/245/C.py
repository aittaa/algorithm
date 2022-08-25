
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
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dx = (0, 0, 1, 1)
dy = (0, 1, 0, 1)

for i in range(N-1):
    
    passFlag = False

    for j in range(4):
        curI = A[i] if dx[j] else B[i]
        curIp = A[i+1] if dy[j] else B[i+1]
        
        if abs(curI - curIp) <= K:
            passFlag = True
            break     
    
    if passFlag:
        continue
    else:
        break    

else:
    print("Yes")
    exit(0)

print("No")

