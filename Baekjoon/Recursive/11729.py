
def hanoi(n, start, end, sub):
    if n==1:
        answer.append((start, end))
        return
    else:
        hanoi(n-1, start, sub, end)
        answer.append((start, end))
        hanoi(n-1, sub, end, start)
n = int(input())
answer = []
hanoi(n, 1, 3, 2)
print(len(answer))
for s, e in answer:
    print(s, e)