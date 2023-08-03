# https://www.acmicpc.net/problem/4949

while True:
    a = input()
    if a[0] == '.':
        break
    st = []
    for i in a:
        if i == '(' or i == '[':
            st.append(i)
        elif i == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                st.append(i)
                break
        elif i == ']':
            if st and st[-1] == '[':
                st.pop()
            else:
                st.append(i)
                break
    if len(st) != 0:
        print("no")
    else:
        print("yes")