import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
graph = []

q_j = deque()
q_f = deque()

visited_j = [[0] * c for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 초기 설정 (J면 방문처리+q에 넣기 , f면 방문처리+q에 넣기)
for i in range(r):
    temp = list(input())

    for j in range(len(temp)):
        if temp[j] == "J":
            q_j.append((i, j))
            visited_j[i][j] = 1

        elif temp[j] == "F":
            q_f.append((i, j))
            visited_f[i][j] = 1

    graph.append(temp)


def bfs():
    while q_f:
        x, y = q_f.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if not visited_f[nx][ny] and graph[nx][ny] != "#":
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_f.append((nx, ny))

    while q_j:
        x, y = q_j.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != "#" and not visited_j[nx][ny]:
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_j.append((nx, ny))

            else:
                return visited_j[x][y]

    return "IMPOSSIBLE"


print(bfs())
