# https://www.acmicpc.net/problem/3273

# 9
# 5 12 7 10 9 1 2 3 11
# 13
#
#
# (1, 12)
# (3, 10)
# (2, 11)

n = int(input())
tmp = [0] * 55
result = 0
a = sorted(list(map(int, input().split(' '))))
for i in a:
    tmp[i] += 1
k = int(input())
print(tmp)
print(a)
for i in range(n//2+1):
    if tmp[k-a[i]] > 0:
        result += 1
        tmp[k-a[i]] -= 1
        tmp[a[i]] -= 1
    # tmp[a[i]] -= 1
    print(tmp, i)
print(result)

# 9
# 1 8 2 7 3 6 9 9 9
# 15
