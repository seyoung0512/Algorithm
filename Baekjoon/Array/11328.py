# https://www.acmicpc.net/problem/11328

n = int(input())
for _ in range(n):
    fir, sec = input().split(' ')
    if sorted(fir) == sorted(sec):
        print("Possible")
    else:
        print("Impossible")

