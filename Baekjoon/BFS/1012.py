from collections import deque

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1

for _ in range(T):
    n, m, k = map(int, input().split())
    graph, visited = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
    queue = deque()
    ans = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j]==0:
                queue.append((i,j))
                visited[i][j] = 1
                bfs()
                ans += 1
    print(ans)
