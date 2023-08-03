# https://www.acmicpc.net/problem/17298

n = int(input())
a = list(map(int, input().split(' ')))
st = []
answer = [-1]*n


for i in range(n):
    while st and st[-1][1] < a[i]:
        answer[st.pop()[0]] = a[i]
    st.append([i, a[i]])

print(*answer)