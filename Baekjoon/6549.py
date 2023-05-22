# https://www.acmicpc.net/problem/6549
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    st = []
    answer = 0
    for i, height in enumerate(a):
        if i==0:
            continue
        if st and st[-1][1] > height:
            while st:
                st_i, st_height = st.pop()
                width_start = 1
                if st:
                    width_start = st[-1][0]+1
                result = (i-width_start) * st_height
                answer = max(result, answer)
                if not st or st[-1][1] <= height:
                    break
        if not st or st[-1][1] <= height:
            st.append((i, height))
    while st:
        width_start = 1
        st_i, st_height = st.pop()
        if st:
            width_start = st[-1][0]+1
        result = (a[0]+1-width_start) * st_height
        answer = max(answer, result)
    print(answer)
