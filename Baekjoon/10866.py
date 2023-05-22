# https://www.acmicpc.net/problem/10866

import sys
from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    line = sys.stdin.readline().rstrip()
    if line == 'size':
        print(len(queue))
    elif line == 'empty':
        if queue: print(0)
        else: print(1)
    elif line == 'pop_front':
        if queue: print(queue.popleft())
        else: print(-1)
    elif line == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif line == 'pop_back':
        if queue: print(queue.pop())
        else: print(-1)
    elif line == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    elif 'push_front' in line:
        queue.appendleft(int(line.split(' ')[1]))
    else:
        queue.append(int(line.split(' ')[1]))



