from collections import deque

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<R and 0<=ny<C and 0<=nz<L:
                if graph[nz][nx][ny] == '.' and visited[nz][nx][ny] == 0:
                    queue.append((nx,ny,nz))
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                if graph[nz][nx][ny] == 'E':
                    return f"Escaped in {visited[z][x][y]} minute(s)."
    return "Trapped!"



while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    dx = [0, 0, -1, 1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    graph = [[] * R for _ in range(L)]
    visited= [[[0] * C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for _ in range(R):
            graph[i].append(list(map(str, input())))
        input()

    # for i in graph:
    #     for j in i:
    #         print(j)
    #     print('----------------------------')
    #
    # for i in visited:
    #     for j in i:
    #         print(j)
    #     print('----------------------------')

    queue = deque()
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if graph[l][r][c] == 'S':
                    queue.append((r,c,l))
                    visited[l][r][c] = 1
                    print(bfs())

