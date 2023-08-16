from collections import deque

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
queue = deque()

def bfs():
    while queue:
        x, y, k = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == k and visited[nx][ny] != k:
                    queue.append((nx,ny))
                    visited[nx][ny] = k
for i in range(2):
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = graph[i][j]
                queue.append((i,j))
                bfs()



