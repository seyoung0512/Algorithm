# https://www.acmicpc.net/problem/5397
n = int(input())
for _ in range(n):
    queue = []
    answer = []
    ch = list(input())
    for i in ch:
        if i == '<':
            if answer:
                queue.append(answer.pop())
        elif i == '>':
            if queue:
                answer.append(queue.pop())
        elif i == '-':
            if answer:
                answer.pop()
        else:
            answer.append(i)
    answer.extend(reversed(queue))
    print(''.join(answer))
