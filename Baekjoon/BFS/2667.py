from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
# for i in graph:
#     print(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
answer = []

def bfs():
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))
            graph[i][j] = 0
            answer.append(bfs())
print(len(answer))
print(*sorted(answer), sep='\n')