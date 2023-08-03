# https://www.acmicpc.net/problem/18258

import sys
from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    line = sys.stdin.readline().rstrip()
    if line == 'pop':
        if queue:print(queue.popleft())
        else:print(-1)
    elif line == 'size':
        print(len(queue))
    elif line == 'empty':
        if queue: print(0)
        else: print(1)
    elif line == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif line == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    else:
        queue.append(int(line.split(' ')[1]))



