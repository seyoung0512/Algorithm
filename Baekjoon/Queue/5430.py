# https://www.acmicpc.net/problem/5430

from collections import deque
import sys

for _ in range(int(input())):
    func = sys.stdin.readline().rstrip()
    n = int(input())
    a = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    rev, flag = 0, 0
    if n == 0:
        a = []
    for i in func:
        if i == 'R':
            rev += 1
        else:
            if len(a) < 1:
                print('error')
                flag = 1
                break
            else:
                if rev % 2 == 0:
                    a.popleft()
                else:
                    a.pop()
    if not flag:
        if rev % 2 == 0:
            print('[' + ','.join(str(i) for i in a) + ']')
        else:
            a.reverse()
            print('[' + ','.join(str(i) for i in a) + ']')
