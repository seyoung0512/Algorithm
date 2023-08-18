from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = []
queue = deque()

def bfs():
    cnt = 1
    while queue:
        x, y =queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and graph[nx][ny] == 0:
                    cnt += 1
                    queue.append((nx,ny))
                    graph[nx][ny] = 1

    return cnt

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[j][i] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            queue.append((i,j))
            graph[i][j] = 1
            answer.append(bfs())

print(len(answer))
print(*sorted(answer))