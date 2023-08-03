# https://www.acmicpc.net/problem/1406

s = list(input())
n = int(input())
queue = []

for _ in range(n):
    line = input()
    if line[0] == 'L':
        if s:
            queue.append(s.pop())
    elif line[0] == 'D':
        if queue:
            s.append(queue.pop())
    elif line[0] == 'B':
        if s:
            s.pop()
    else:
        s.append(line.split(' ')[1])
s.extend(reversed(queue))
print(''.join(s))
