import copy


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 위 -> 위 -> 위 -> 위 -> 위
def move(board, dir):
    # 동쪽(오른쪽으로 밀기)
    if dir == 0:
        for i in range(n):
            top = n-1
            for j in range(n-2, -1, -1):
                # print("i, j: ", i, j)
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp*2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp
                # for b in board:
                #     print(b)
                # print('-------')

    # 서쪽(왼쪽으로 밀기)
    elif dir == 1:
        for i in range(n):
            top = 0
            for j in range(1, n):
                # print("i, j: ", i, j)
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp*2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp
                # for b in board:
                #     print(b)
                # print('-------')
    # 남쪽(아래쪽으로 밀기)
    elif dir == 2:
        for i in range(0, n):
            top = n - 1
            for j in range(n-2, -1, -1):
                # print("top", top, "j, i: ", j, i)
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[top][i] == 0:
                        board[top][i] = tmp
                    elif board[top][i] == tmp:
                        board[top][i] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][i] = tmp
                # for b in board:
                #     print(b)
                # print('-------')
    # 북쪽(위쪽으로 밀기)
    else:
        for i in range(n):
            top = 0
            for j in range(1, n):
                # print("top", top, "j, i: ", j, i)
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    # print("j, i:", j, i, "top:", top, "top board 값", board[top][i])
                    if board[top][i] == 0:
                        board[top][i] = tmp
                    elif board[top][i] == tmp:
                        # print("here")
                        board[top][i] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][i] = tmp
                # for b in board:
                    # print(b)
                # print('-------')
    return board


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        temp = copy.deepcopy(board)
        temp = move(temp, i)
        dfs(temp, cnt+1)


ans = 0
dfs(board, 0)
print(ans)