# https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >=n or ny <0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        bfs(graph, i, j)

print(graph[n-1][m-1])