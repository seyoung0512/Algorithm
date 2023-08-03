# https://www.acmicpc.net/problem/6198
from collections import deque

n = int(input())
a = []
st = []
answer = 0
for i in range(n):
    a.append(int(input()))

print(a)
for i in range(n):
    while st and st[-1] <= a[i]:
        st.pop()
    st.append(a[i])
    answer += len(st)-1
print(answer)