
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
data = [0] + list(map(int, input().split()))


sum = 0
type_a = 0
type_b = 0

for i in range(1, N+1):
    if data[i] == i:
        type_a += 1
        
    elif data[i] < i and data[data[i]] == i :
        type_b += 1

sum = (type_a) * (type_a-1) / 2
print(int(sum) + type_b)

