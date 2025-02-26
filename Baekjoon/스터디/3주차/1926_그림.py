from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프의 범위 안 벗어나게 하기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 방문 노드에 1이 표시 되었을 떄
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                #인접한 노드 추가
                queue.append((nx, ny))
                count += 1
    return count

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))

if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))