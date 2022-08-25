
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

# U D L R
G = [(-1, 0), (1, 0), (0, -1), (0, 1)]

H, W = map(int, input().split())
data = []

for i in range(H):
    row = list(map(str, input()))
    new_row = []

    for e in row:
        if e == 'U':
            new_row.append(0)
        elif e == 'D':
            new_row.append(1)
        elif e == 'L':
            new_row.append(2)
        else:
            new_row.append(3)
    data.append(new_row)



cur_x = 0
cur_y = 0
step = 0

fin = 0

while 0 <= cur_x < W and 0 <= cur_y < H:

    step += 1
    if step > (H*W*3):
        print(-1)
        break

    cur_g_val = data[cur_y][cur_x]
    cur_x += G[cur_g_val][1]
    cur_y += G[cur_g_val][0]

else:
    cur_x -= G[cur_g_val][1]
    cur_y -= G[cur_g_val][0]
    print(cur_y+1, cur_x+1)