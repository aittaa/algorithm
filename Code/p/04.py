

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

sys.setrecursionlimit(10**5)

###

hist = {}

S = list(input())
q = deque()

a = ord('a')
z = ord('z')
zero = ord('0')
nine = ord('9')

for i in range(a, z+1):
    hist[chr(i)] = 0

temp = 0

for i in range(len(S)):

    if a <= ord(S[i]) <= z:
        q.append(S[i])
    elif zero <= ord(S[i]) <= nine:
        temp += 1
        if zero <= ord(S[i+1]) <= nine:
            continue
        else:
            q.append(int("".join(S[i-(temp-1):i+1])))
            temp = 0
    else:
        q.append(S[i])



def count(queue:deque, value:int):

    while queue:

        cur_val = queue.popleft()

        if isinstance(cur_val, str):
            hist[cur_val] += 1*value
        elif isinstance(cur_val, int) and queue[0].isalpha():
            hist[queue[0]] += cur_val*value
            queue.popleft()
        elif isinstance(cur_val, int) and queue[0] == "(":
            queue.popleft()

            temp_q = deque()
            braket = 0
            while True:
                cur = queue.popleft()

                if cur == "(": braket += 1
                if cur == ")" and braket == 0:
                    count(temp_q, cur_val * value)
                    break
                elif cur == ")":
                    braket -= 1

                temp_q.append(cur)





count(q, 1)


for item in hist.items():
    print(item[0], item[1])


