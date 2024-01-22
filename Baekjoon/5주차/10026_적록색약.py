from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * N for _ in range(N)]


def bfs(a, b,blindness):
    queue = deque()
    queue.append([a,b,graph[a][b]])
    if blindness:
        while queue:
            x, y, color = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y + dy[i]
                if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and visited[nx][ny] == False and graph[x][y]==graph[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return True




for i in range(N):
    for j in range(N):
        bfs(i,j,False)
        bfs(i,j,True)

