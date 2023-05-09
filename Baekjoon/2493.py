# https://www.acmicpc.net/problem/2493

n = int(input())
st = []
answer = []

a = list(map(int, input().split(' ')))
for i in range(n):
    while st:
        if st[-1][1] > a[i]:
            answer.append(st[-1][0] + 1)
            break
        else:
            st.pop()
    if not st:
        answer.append(0)
    st.append([i, a[i]])
print(' '.join(str(i) for i in answer))