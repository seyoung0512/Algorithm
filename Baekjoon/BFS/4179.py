#https://www.acmicpc.net/problem/4179

import sys
from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

j_queue, f_queue = deque([]), deque([])
j_visited, f_visited = [[-1] * m for _ in range(n)], [[-1] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            j_visited[i][j] = 0
            j_queue.append((i,j))
        elif graph[i][j] == 'F':
            f_visited[i][j] = 0
            f_queue.append((i,j))

def bfs():
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<n and 0 <=ny<m:
                if f_visited[nx][ny] == -1 and graph[nx][ny] != "#":
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx,ny))

    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if j_visited[nx][ny] == -1 and graph[nx][ny] != "#":
                    if f_visited[nx][ny] == -1 or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))
            else:
                return j_visited[x][y] + 1
    return "IMPOSSIBLE"

print(bfs())