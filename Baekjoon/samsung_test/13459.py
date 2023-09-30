# 9/29 15:05 문제 풀이 시작
# 9/30 11:20 문제 풀이 종료 -- dfs로 풀어서 망함, bfs로 풀어야함

from collections import deque
n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]
visited = [[[[0]*m for _ in range(n)] for _ in range(m)]for _ in range(n)]

queue = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(x, y, dir):
    count = 0
    while board[x + dx[dir]][y+dy[dir]] != '#' and board[x][y] != 'O':
        x += dx[dir]
        y += dy[dir]
        count += 1
    return x, y, count


def bfs():
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for dir in range(4):
            nrx, nry, r_count = move(rx, ry, dir)
            nbx, nby, b_count = move(bx, by, dir)

            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(1)
                return
            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[dir]
                    nry -= dy[dir]
                else:
                    nbx -= dx[dir]
                    nby -= dy[dir]
            if not visited[nrx][nry][nbx][nby]:
                queue.append((nrx,nry,nbx,nby,depth+1))
                visited[nrx][nry][nbx][nby] = True
    print(0)


ri, rj, bi, bj = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            ri, rj = i, j
        if board[i][j] == 'B':
            bi, bj = i, j
queue.append((ri, rj, bi, bj, 1))
visited[ri][rj][bi][bj] = True
bfs()