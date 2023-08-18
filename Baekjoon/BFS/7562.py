from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if nx == ei and ny == ej:
                    graph[nx][ny] = graph[x][y] + 1
                    return graph[nx][ny]
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    queue = deque()
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    if si == ei and sj == ej:
        print(0)
    else:
        queue.append((si,sj))
        ans = bfs()
        # for i in graph:
        #     print(i)
        print(ans)


