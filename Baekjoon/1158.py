# https://www.acmicpc.net/problem/1158

from collections import deque
n, k = map(int, input().split())
a = deque([i+1 for i in range(n)])
answer = []
while a:
    for _ in range(k-1):
        a.append(a.popleft())
    answer.append(a.popleft())
print('<'+', '.join(str(s) for s in answer) + '>')