n, m, k = map(int, input().split())

stickers = []
board = [[0] * m for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(y)]
    stickers.append(sticker)


def canCoordinate(sticker):
    coordinate = []
    xOffset = len(sticker[0])
    yOffset = len(sticker)
    for y in range(n):
        for x in range(m):
            if board[y][x] == 0 or (board[y][x] and sticker[0][0] == 0):
                if y + yOffset <= n:
                    if x + xOffset <= m:
                        coordinate.append((y,x))
    return coordinate

def put(sticker, y, x):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]:
                board[i+y][j+x] = 1


def canPut(sticker, y, x):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if board[y+i][j+x] and sticker[i][j]:
                return False
    return True

def rotation(sticker):
    sticker = zip(*sticker[::-1])
    return [list(e) for e in sticker]

def logic(sticker):
    for _ in range(4):
        coordinate = canCoordinate(sticker)
        # print('가능한 좌표들', coordinate)
        if coordinate:
            for y, x in coordinate:
                if canPut(sticker, y, x):
                    # print('(', y, x, ') 에다가 넣음')
                    put(sticker, y, x)
                    # print('----------현재 보드 상황------------')
                    # for i in range(n):
                    #     print(board[i])
                    # print('--------------------------------')
                    return
        sticker = rotation(sticker)
        # print('-----------회전시킨거-----------')
        # for xx in range(len(sticker)):
        #     print(sticker[xx])

for sticker in stickers:
    logic(sticker)


cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt += 1

print(cnt)