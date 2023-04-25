# https://www.acmicpc.net/problem/1919

x = input()
y = input()
lx= [0] * 26
ly =[0] * 26
answer = 0
for i in x:
    lx[ord(i)-97] += 1
for i in y:
    ly[ord(i)-97] += 1
for i in range(26):
    if lx[i] > ly[i] or lx[i] < ly[i]:
        answer += abs(lx[i]-ly[i])
print(answer)


