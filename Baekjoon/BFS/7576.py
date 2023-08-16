# https://www.acmicpc.net/problem/7576

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
ans = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque([])
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans-1)

