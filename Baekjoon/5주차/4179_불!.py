from collections import deque

R, C = map(int, input().split())

visitedFire = [[0] * C for _ in range(R)]
visitedJihoon = [[0] * C for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 지도 세팅
graph = []
for i in range(R):
    graph.append(list(input()))
queueFire = deque()
queueJihoon = deque()

# 초기 세팅
for i in range(R):
    for j in range(C):
        if graph[i][j] == "J":
            visitedJihoon[i][j] = 1
            queueJihoon.append((i, j))
        if graph[i][j] == "F":
            visitedFire[i][j] = 1
            queueFire.append((i, j))


def bfs():
    while queueFire:
        x, y = queueFire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != "#" and not visitedFire[nx][ny]:
                    queueFire.append((nx, ny))
                    # 전 방문에 걸린 시간에 +1 하여 기록
                    visitedFire[nx][ny] = visitedFire[x][y] + 1

    while queueJihoon:
        x, y = queueJihoon.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                # visitedFire[x][y]+1이 nx,ny의 도착시간인데 Fire보다 작아야함.
                if graph[nx][ny] != "#" and not visitedJihoon[nx][ny]:
                    # 불이 안온 경우나 지훈이 빨리온 경우
                    if not visitedFire[nx][ny] or visitedJihoon[x][y] + 1 < visitedFire[nx][ny]:
                        queueJihoon.append((nx, ny))
                        # 전 방문에 걸린 시간에 +1 하여 기록
                        visitedJihoon[nx][ny] = visitedJihoon[x][y] + 1

            else:
                return visitedJihoon[x][y]
    return "IMPOSSIBLE"


result = bfs()
print(result)
