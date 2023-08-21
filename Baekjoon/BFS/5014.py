from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0] * (f+1)
dy = [u, d]
queue = deque()

def bfs():
    while queue:
        y = queue.popleft()
        for i in range(2):
            if i == 0:
                ny = y + dy[i]
            else:
                ny = y - dy[i]
            if 1<=ny<=f and visited[ny] == 0:
                visited[ny] = visited[y] + 1
                queue.append((ny))
    if visited[g] == 0:
        return "use the stairs"
    else:
        return visited[g] - 1


if s == g:
    print(0)
else:
    visited[s] = 1
    queue.append((s))
    print(bfs())