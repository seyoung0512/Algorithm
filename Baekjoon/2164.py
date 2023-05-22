# https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())
a = deque([i+1 for i in range(n)])
while len(a)>1:
    a.popleft()
    a.append(a.popleft())
print(a[0])
