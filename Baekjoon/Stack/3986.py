# https://www.acmicpc.net/problem/3986

n = int(input())
answer = 0
for i in range(n):
    a = input()
    st = []
    for i in a:
        if i == 'A':
            if st and st[-1] == 'A':
                st.pop()
            else:
                st.append(i)
        elif i == 'B':
            if st and st[-1] == 'B':
                st.pop()
            else:
                st.append(i)
    if len(st) == 0:
        answer += 1
print(answer)