# https://www.acmicpc.net/problem/3015

import sys

n = int(input())
a = []
st = []
answer = 0

# stack 입력값은 {수, 같은 수가 입력값에 존재하는지에 대한 cnt}
for _ in range(n):
    a.append(int(sys.stdin.readline().rstrip()))

for i in range(n):
    while st and st[-1][0] < a[i]:
        answer += st.pop()[1]
    if not st:
        st.append([a[i], 1])
        continue

    if st[-1][0] == a[i]:
        cnt = st.pop()[1]
        answer += cnt

        if st:
            answer += 1

        st.append([a[i], cnt+1])
    else:
        st.append([a[i], 1])
        answer += 1

    print(st, answer)
