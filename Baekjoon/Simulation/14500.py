# 제한시간안에 못품 + 테스트 케이스는 다 통과하지만 시간초과 발생해서 다른 코드 살펴보고 해결

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 오, 왼 ,아, 위
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

mode = [
    [[0, 1], [1, 0], [-1, 0]],
    [[1, 0], [-1, 0], [0, -1]],
    [[-1, 0], [0, -1], [0, 1]],
    [[0, -1], [0, 1], [1, 0]]
]

def oh(x, y):
    global max_value
    for i in range(len(mode)):
        cnt = board[x][y]
        for mx, my in mode[i]:
            nx = x + mx
            ny = y + my
            # print(nx, ny)
            if 0 <= nx < n and 0 <= ny < m:
                cnt += board[nx][ny]
                # print("더한 후 cnt", cnt)
        max_value = max(max_value, cnt)


def dfs(depth, dsum, x, y):
    global max_value
    if depth == 3:
        max_value = max(max_value, dsum)
        return

    for i in range(4):
        # print(dir)
        nx = x + dx[i]
        ny = y + dy[i]
        # print("현재 길이: ", depth)
        # print("dir: ", i)
        # print("x, y :", x, y)
        # print("nx, ny : ", nx, ny)
        if 0<= nx < n and 0<= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(depth+1, dsum + board[nx][ny], nx, ny)
            visited[nx][ny] = False


max_value = 0
dfs_cnt = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(0, board[i][j], i, j)
        visited[i][j] = False
        oh(i, j)

print(max_value)
