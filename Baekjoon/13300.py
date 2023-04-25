# https://www.acmicpc.net/problem/13300

n, k = map(int, input().split(' '))
girl, boy = [0]*6, [0]*6

cnt, cntt= 0, 0
for _ in range(int(n)):
    s, y = map(int, input().split(' '))
    if s == 0:
        girl[y-1] += 1
        if girl[y-1] % k == 0:
            girl[y-1] = 0
            cntt += 1
    else:
        boy[y-1] += 1
        if boy[y-1] % k == 0:
            boy[y-1] = 0
            cnt += 1
print(cntt + cnt + 12 - boy.count(0) - girl.count(0))

