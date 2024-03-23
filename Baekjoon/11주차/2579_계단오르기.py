N = int(input())
stair = []
# D[i] 정의 : i칸을 밟았을때 그때까지의 최댓값, 세번 연속 x
for _ in range(N):
    stair.append(int(input()))
DP = [0] * N

if N >= 1:
    DP[0] = stair[0]
if N >= 2:
    DP[1] = stair[0] + stair[1]
if N >= 3:
    DP[2] = max(stair[0] + stair[2], stair[1] + stair[2])


for i in range(3, N):
    DP[i] = max(DP[i - 3] + stair[i - 1] + stair[i], DP[i - 2] + stair[i]) # 두가지 경우로 나눔. i-3과 i-2 계단 밟을때
print(DP[N - 1])
