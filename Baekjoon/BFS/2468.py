from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
s, m = 100, 1
for i in graph:
    s = min(s, min(i))
    m = max(s, max(i))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs():
    # cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if tmp_graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    # cnt += 1
    # return cnt

answer = []
for h in range(s, m):
    tmp_graph, visited = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
    queue = deque()
    ans = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:
                tmp_graph[i][j] = 1
    # print("height: ", h, "---------------------")
    # for tmp in tmp_graph:
    #     print(tmp)
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == 0 and visited[i][j] == 0:
                queue.append((i,j))
                visited[i][j] = 1
                ans += 1
                bfs()
                #
                # print("넓이: ", bfs(), "---------------------")
    answer.append(ans)
if len(answer) > 0:
    print(max(answer))
else:
    print(1)