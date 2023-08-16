# https://www.acmicpc.net/problem/1697

from collections import deque

n, m = map(int, input().split())
visited = [0] * 100001

queue = deque()
queue.append((n))
visited[n] = 1

dx = [-1, 1, 2]

def bfs():
    while visited[m] == 0:
        x = queue.popleft()
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
                if 0 <= nx < len(visited):
                    if visited[nx] == 0:
                        visited[nx] = visited[x] + 1
                        queue.append((nx))
            else:
                nx = x + dx[i]
                if 0 <= nx < len(visited):
                    if visited[nx] == 0:
                        visited[nx] = visited[x] + 1
                        queue.append((nx))
    return visited[m]

print(bfs()-1)