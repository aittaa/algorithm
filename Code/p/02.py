

from collections import deque
import math
import heapq
from bisect import bisect_left, bisect_right
from re import L
import sys

# input = sys.stdin.readline
def input() :
    return sys.stdin.readline().rstrip()
    
dx = (1, 0, -1, 0, 1, -1, -1, 1)
dy = (0, -1, 0, 1, -1, -1, 1, 1)

INF = float('inf')

# sys.setrecursionlimit(10**7)

###

W, H = map(int, input().split())

data = []

start = 0
end = 0 
for i in range(H):
    s = list(input().split())
    col = []
    for j in range(W):
        col.append(s[j])
        if s[j] == 's':
            start = (i, j)
        elif s[j] == 'g':
            end = (i, j)
    
    data.append(col)




def bfs(y, x):

    q = deque()
    data[y][x] = 0
    
    q.append((y, x))

    while q:

        y, x = q.pop()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not(0 <= new_x < W and 0 <= new_y < H): continue
            if data[new_y][new_x] == 'g':
                print(data[y][x]+1)
                exit(0)
            
            if data[new_y][new_x] != '0': continue


            data[new_y][new_x] = data[y][x]+1
            q.append((new_y, new_x))
        

    else:
        print("Fail")

bfs(start[0], start[1])