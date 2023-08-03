# https://www.acmicpc.net/problem/2504

a = input()
ans = 0
st = []
tmp = 1
for i in range(len(a)):
    if a[i] == '(':
        st.append(a[i])
        tmp *= 2
    elif a[i] == '[':
        st.append(a[i])
        tmp *= 3
    elif a[i] == ')':
        if not st:
            ans = 0
            break
        elif a[i-1] == '(':
            ans += tmp
            st.pop()
        elif st[-1] == '(':
            st.pop()
        tmp //= 2
    elif a[i] == ']':
        if not st:
            ans = 0
            break
        elif a[i-1] == '[':
            ans += tmp
            st.pop()
        elif st[-1] == '[':
            st.pop()
        tmp //= 3
    # print(st, 'tmp:', tmp, ans)
if len(st) > 0:
    print(0)
else:
    print(ans)