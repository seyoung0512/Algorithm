# https://www.acmicpc.net/problem/10799

a = input()
st = []
ans = 0
for i in range(len(a)):
    if a[i] == '(':
        st.append(i)
    else :
        if a[i-1] == '(':
            st.pop()
            ans += len(st)
        else:
            st.pop()
            ans += 1
print(ans)