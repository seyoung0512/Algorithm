import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cctv = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for i in range(n):
    for j in range(m):
        if board[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([board[i][j], i, j])

def fill(board, dir, x, y):
    for i in dir:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, arr):
    global min_value
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += arr[i].count(0)
        min_value = min(min_value, cnt)
        return
    temp = copy.deepcopy(arr)
    cctv_nums, x, y = cctv[depth]
    for i in mode[cctv_nums]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, board)
print(min_value)
