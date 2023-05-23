# https://www.acmicpc.net/problem/4949

import re

flag = True
while flag:
    line = input()
    if line[0] == '.':
        flag = False
        break
    a = re.findall('[^a-zA-Z]', line.replace(' ', ''))
    st = []
    # print(a)
    for i in range(len(a)-1):
        if a[i] == '[' or a[i] == '(':
            st.append(a[i])
        elif a[i] == ')' or a[i] == ']':
            if not st:
                answer = 'no'
                break
            else:
                while st and (st[-1] == '(' and a[i] == ')') or (st[-1] == '[' and a[i] == ']'):
                    st.pop()
                    break
        else:
            answer = 'yes'
            break
        if i == len(a)-2:
            if len(st) == 0:
                answer = 'yes'
            else:
                answer = 'no'
    print(answer)