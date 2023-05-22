# https://www.acmicpc.net/problem/11003

import sys

n, m = map(int, input().split(' '))
a = map(int, sys.stdin.readline().rstrip().split(' '))
print(a)
answer = ''
for i in range(n):
    print(a[i])
    if i < m:
        answer += str(min(a[:i+1])) + ' '
    else:
        answer += str(min(a[i-m+1:i+1])) + ' '

print(answer)

