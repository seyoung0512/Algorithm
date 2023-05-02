# https://www.acmicpc.net/problem/10828

import sys

n = int(input())
a = []
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    if line[1] == 'u':
        a.append(int(line.split(' ')[1]))
    elif line == 'pop':
        if a:
            print(a.pop())
        else:
            print(-1)
    elif line[0] == 's':
        print(len(a))
    elif line[0] == 'e':
        if a:
            print(0)
        else:
            print(1)
    else:
        if a:
            print(a[-1])
        else:
            print(-1)

