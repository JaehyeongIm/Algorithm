# 0으로 시작하지 않음
# 1이 두번 연속으로 나타나지 않음
N= int(input())
#DP[i][j] = i자리까지의 이친수 개수 (j는 끝나는 자리의 수)
DP = [[0,0] for _ in range(N+1)]
DP[1][0] = 0
DP[1][1] = 1

if N>=2:
    for i in range(2,N+1):
        DP[i][0] = DP[i-1][1] + DP[i-1][0] #0으로 끝나는수
        DP[i][1] = DP[i-1][0] # 1으로 끝나는 수
print(DP[N][0]+DP[N][1])

