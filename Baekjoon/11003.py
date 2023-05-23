# https://www.acmicpc.net/problem/11003

import sys
from collections import deque

n, k = map(int, input().split(' '))
a = list(map(int, sys.stdin.readline().rstrip().split(' ')))
q = deque()
answer = []
for i in range(n):
    while q and q[-1][0] > a[i]:
        q.pop()
    while q and q[0][1] < i-k+1:
        q.popleft()
    q.append((a[i],i))
    answer.append(q[0][0])
print(*answer)