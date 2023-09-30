n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
stickers = []


def canCoordinate(sticker, board):
    coordinate = []
    xOffset = len(sticker)
    yOffset = len(sticker[0])
    for x in range(n):
        for y in range(m):
            if not board[x][y] or (board[x][y] and not sticker[0][0]):
                if x + xOffset <= n:
                    if y + yOffset <= m:
                        coordinate.append((x, y))
    return coordinate


def put(x, y, sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]:
                board[i+x][j+y] = 1


def canPut(x, y, sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if board[i+x][j+y] and sticker[i][j]:
                return False
    return True


def rotation(sticker):
    sticker = zip(*sticker[::-1])
    return [list(e) for e in sticker]


def logic(sticker):
    for i in range(4):
        coordinate = canCoordinate(sticker, board)
        if coordinate:
            for x, y in coordinate:
                if canPut(x, y, sticker):
                    put(x, y, sticker)
                    return
        sticker = rotation(sticker)


for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)

for sticker in stickers:
    logic(sticker)

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j]:
            cnt += 1

print(cnt)