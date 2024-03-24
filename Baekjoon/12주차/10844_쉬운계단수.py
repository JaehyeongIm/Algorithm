N = int(input())

# 모두 + 일때는 어디에 쳐도 상관 없음
# 하나가 -일경우 - 뒤에서 쳐야함
#
# DP[i] , i번째 자리수까지의 계단수 개수
DP = [0] * (N+1)
DP[1] = 9
if N>=2:
    for i in range(2,N+1):
        DP[i] = DP[i-1]*2 -1 # 9인경우 떄문에 1뺴줘야함
print(DP[N] % 1000000000)
