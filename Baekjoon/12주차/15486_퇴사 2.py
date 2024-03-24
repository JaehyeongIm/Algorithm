N = int(input())
inputList = []
for i in range(N):
    inputList.append(list(map(int, input().split())))
DP = [[0,0] for _ in range(N)] # DP[i][0] i일의 상담을 했을때의 수익의 최댓값, DP[i][1] i일의 상담을 안했을때의 최댓값
#1일차 초기화
DP[0][0] = 10
DP[0][1] = 0

DP[1][0] = DP[0][1] + inputList[1][0]
DP[1][1]= max(DP[0][0],DP[0][1])

