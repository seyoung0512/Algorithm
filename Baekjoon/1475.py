# https://www.acmicpc.net/problem/1475
minimum = 0
a = list(input())
sixnine = int(abs(a.count('6') + a.count('9'))/2) + int(abs(a.count('6') + a.count('9'))%2)
for i in range(10):
    if i == 6 or i == 9:
        continue
    if minimum < a.count(str(i)):
        minimum = a.count(str(i))
print(max(minimum, sixnine))