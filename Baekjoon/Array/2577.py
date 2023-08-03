# https://www.acmicpc.net/problem/2577

result = [0]*10
a = 1
for _ in range(3):
    a *= int(input())
for i in str(a):
    result[int(i)] += 1
print(' \n'.join(str(s) for s in result))