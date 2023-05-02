# https://www.acmicpc.net/problem/2493

n = int(input())
st = []
flag = 1
answer = [0]

a = list(map(int, input().split(' ')))
st.append(a[0])
print(a)
print(st)
for i in range(1, n):
    print(i)
    while st:
        if flag:
            k = st.pop()
            print("k", k)
            if a[i] < k:
                answer.append(a.index(a[i]))
                st.append(a[i])

            else:
                answer.append(0)
                st.append(a[i])
    print(flag, a[i], st)