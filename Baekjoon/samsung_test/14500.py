n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

mode = [
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3],
]


def oh(x, y):
    global max_value
    for dirs in mode:
        cnt = board[x][y]
        for dir in dirs:
            nx = x+dx[dir]
            ny = y+dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                cnt += board[nx][ny]
        max_value = max(max_value, cnt)


def dfs(x, y, dsum, depth):
    global max_value
    if depth == 4:
        max_value = max(max_value, dsum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum+board[nx][ny], depth+1)
            visited[nx][ny] = False



max_value = 0
for i in range(n):
    for j in range(m):
        oh(i, j)
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
print(max_value)