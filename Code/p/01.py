

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

H, W = map(int, input().split())

data = []
for i in range(H):
    data.append(list(input()))

visit = [[False] * W for _ in range(H)]


r = 0; g = 0; b = 0


def dfs(y, x):

    visit[y][x] = True

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < W and 0 <= new_y < H:
            if not visit[new_y][new_x] and data[y][x] == data[new_y][new_x]:
                dfs(new_y, new_x)

    return data[y][x]

for y in range(H):
    for x in range(W):
        if not visit[y][x]:
            val = dfs(y, x)
            if val == 'R':
                r += 1
            elif val == 'G':
                g += 1
            else:
                b += 1


print(r, g, b)