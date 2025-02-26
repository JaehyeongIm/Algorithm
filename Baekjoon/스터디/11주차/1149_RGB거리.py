N = int(input())
cost= []
for i in range(N):
    cost.append(list(map(int,input().split())))

# 0 - 빨강 1 - 녹색 2 - 파랑
# 초기 설정
D = [[0,0,0] for _ in range(N)]
D[0][0] = cost[0][0]
D[0][1] = cost[0][1]
D[0][2] = cost[0][2]

# D[i] = i번째를 특정색깔로 칠했을때 비용의 최솟값 0,1,2 = 빨강,녹색,파랑
for i in range(1, N):
    D[i][0] = min(D[i-1][2]+cost[i][0], D[i-1][1]+cost[i][0])
    D[i][1] = min(D[i-1][0]+cost[i][1], D[i-1][2]+cost[i][1])
    D[i][2] = min(D[i-1][0]+cost[i][2], D[i-1][1]+cost[i][2])
print(min(D[N-1])) # 0 인덱싱이라 1빼서 출력
