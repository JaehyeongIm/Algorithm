from collections import deque

M, N, H = map(int, input().split())

# 3차원 배열 생성 및 입력 받기
three_dimensional_array = []
for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
    three_dimensional_array.append(layer)

# 방문 배열 초기화
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

# 이동 방향 설정 (상하좌우위아래)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# BFS 큐 초기화
queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if three_dimensional_array[h][n][m] == 1:
                queue.append((h, n, m))
                visited[h][n][m] = True

# BFS 실행
while queue:
    h, n, m = queue.popleft()
    for i in range(6):
        nh = h + dz[i]
        nn = n + dy[i]
        nm = m + dx[i]
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and not visited[nh][nn][nm] and three_dimensional_array[nh][nn][nm] == 0:
            queue.append((nh, nn, nm))
            visited[nh][nn][nm] = True
            three_dimensional_array[nh][nn][nm] = three_dimensional_array[h][n][m] + 1

# 모든 토마토가 익었는지 확인 및 결과 계산
result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if three_dimensional_array[h][n][m] == 0:
                print(-1)
                exit()
            result = max(result, three_dimensional_array[h][n][m])

print(result - 1)
