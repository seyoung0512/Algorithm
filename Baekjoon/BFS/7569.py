from collections import deque

n, m, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

queue = deque()
ans = 0

# for i in graph:
#     for j in i:
#         print(j)

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # print(nx, ny, nz)
            if 0<=nx<h and 0<=ny<m and 0<=nz<n:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append((nx,ny,nz))

bfs()
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
            else:
                ans = max(ans, k)

print(ans-1)