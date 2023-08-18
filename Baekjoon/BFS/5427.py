from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(str, input().strip())) for _ in range(m)]

    # for i in graph:
    #     print(i)

    j_visited, f_visited = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
    j_queue, f_queue = deque(), deque()

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def bfs():
        while f_queue:
            x, y = f_queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[nx][ny] != '#' and f_visited[nx][ny] == 0:
                        f_queue.append((nx,ny))
                        f_visited[nx][ny] = f_visited[x][y] + 1
        # for i in f_visited:
        #     print(i)

        while j_queue:
            x, y = j_queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if graph[nx][ny] != '#' and j_visited[nx][ny] == 0:
                        if f_visited[nx][ny] == 0 or f_visited[nx][ny] > j_visited[x][y]+1:
                            j_queue.append((nx,ny))
                            j_visited[nx][ny] = j_visited[x][y] + 1
                else:
                    # for k in j_visited:
                    #     print(k)
                    return j_visited[x][y]


        return 'IMPOSSIBLE'

    for i in range(m):
        for j in range(n):
            if graph[i][j] == '@':
                j_queue.append((i,j))
                j_visited[i][j] = 1
            elif graph[i][j] == '*':
                f_queue.append((i,j))
                f_visited[i][j] = 1

    print(bfs())