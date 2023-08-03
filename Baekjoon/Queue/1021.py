# https://www.acmicpc.net/problem/1021
from collections import deque

n, m = map(int, input().split(' '))
a = deque([_+1 for _ in range(n)])
key = list(map(int, input().split(' ')))
answer = 0
for i in key:
    while a[0] != i:
        if a.index(i) <= len(a)/2:
            a.append(a.popleft())
            answer += 1
        else:
            a.appendleft(a.pop())
            answer += 1
    a.popleft()
print(answer)






