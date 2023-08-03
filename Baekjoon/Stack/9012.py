# https://www.acmicpc.net/problem/9012

i = int(input())
for i in range(i):
    a = input()
    st = []
    for i in a:
        if i == '(':
            st.append(i)
        elif i == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                st.append(i)
                break
    if len(st) == 0:
        print("YES")
    else:
        print("NO")