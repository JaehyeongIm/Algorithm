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


#인덱스로 접근할때는 h , n ,m 순서 : 왜냐하면  m을 먼저넣었기 때문에
# 동시에 토마토가 익게하려면 익은 토마토를 처음에 다 넣어야함
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
            
            # 토마토 배열에 1을 더해주면서 익은 날짜를 표기
            three_dimensional_array[nh][nn][nm] = three_dimensional_array[h][n][m] + 1

# 모든 토마토가 익었는지 확인 및 결과 계산
result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if three_dimensional_array[h][n][m] == 0:
                print(-1)
                exit()
                
                # 토마토 셀 중 최댓값을 찾음
            result = max(result, three_dimensional_array[h][n][m])
 # 시작할 때를 하루걸린다고 했기 때문에 -1
print(result - 1)
