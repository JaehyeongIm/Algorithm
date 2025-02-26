import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip()))) # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 노드에 대해 상하좌우 검색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #그래프 범위 안에 있고 이웃값이 1일때
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                
                # 거리 업데이트
                graph[nx][ny] = graph[x][y] + 1
    #최단 거리 리턴
    return graph[n-1][m-1]

print(bfs(0,0))