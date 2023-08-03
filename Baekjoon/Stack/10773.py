# https://www.acmicpc.net/problem/10773

import sys

n = int(input())
a = []
for _ in range(n):
    line = int(sys.stdin.readline().rstrip())
    if line == 0:
        a.pop()
    else:
        a.append(line)
print(sum(a))