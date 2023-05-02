# https://www.acmicpc.net/problem/1874

import sys

n = int(sys.stdin.readline())
st = []
flag = 0
answer = []
pos = 1
for _ in range(n):
    k = int(sys.stdin.readline())
    while pos <= k:
        st.append(pos)
        answer.append('+')
        pos += 1
    if st[-1] == k:
        st.pop()
        answer.append('-')
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    print(*answer, sep = '\n')










