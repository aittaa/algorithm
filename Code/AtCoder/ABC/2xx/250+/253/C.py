
from collections import OrderedDict, deque
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

Q = int(input())

data = dict()
minHeap = []
maxHeap = []

for i in range(Q):
    
    inputData = list(map(int, input().split()))

    if inputData[0] == 1:

        x = inputData[1]

        if x in data:
            data[x] += 1
        else:
            data[x] = 1
            heapq.heappush(minHeap, x)
            heapq.heappush(maxHeap, -x)


    elif inputData[0] == 2:
        x, c = inputData[1], inputData[2]

        if x in data:
            if data[x] <= c:
                del data[x]
            else:
                data[x] -= c

    else:
        
        maxKey = 0
        minKey = 0

        while True:
            minKey = minHeap[0]
            if minKey in data:
                break
            else:
                heapq.heappop(minHeap)
        while True:
            maxKey = maxHeap[0]
            maxKey = -maxKey
            if maxKey in data:
                break
            else:
                heapq.heappop(maxHeap)
                
        print(maxKey - minKey)


