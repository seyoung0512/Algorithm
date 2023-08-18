from collections import deque

n = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
graph = [list(map(str, input())) for _ in range(n)]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1


for t in range(2):
    ans = 0
    visited = [[0] * n for _ in range(n)]
    if t==1:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'G':
                    graph[i][j] = 'R'
        # print(' ')
        # for i in graph:
        #     print(i)

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                queue.append((i,j))
                bfs()
                # print(' ')
                # for vi in visited:
                #     print(vi)
                ans += 1
    print(ans, end = ' ')

