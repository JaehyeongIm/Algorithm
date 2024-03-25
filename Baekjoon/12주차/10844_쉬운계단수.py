N = int(input())

# DP[i][j] , i자리 숫자에서 숫자 j로 끝나는 계단수 개수
DP = [[0]*10 for _ in range(N+1)]
for i in range(1,10): #초기값 설정
    DP[1][i]=1
if N>=2:
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                DP[i][j] = DP[i-1][j+1]
            elif j == 9:
                DP[i][j] = DP[i-1][j-1]
            else:
                DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]

result =0
for i in range(10):
    result += DP[N][i]
print(result % 1000000000)
