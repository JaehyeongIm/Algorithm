# 블로그 참고
import sys
input = sys.stdin.readline

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n + 1)]

#dp[i] i일까지의 최대수익
for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])  # 이전에 반복문에서 계산해논 DP를 이용하여 i일에 상담 안해도 되는 경우 처리
    fin_date = i + t[i] - 1  # 끝나는 날짜
    if fin_date <= n:  #끝나는 날짜가 최종일 전일떄
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i]) #매개변수 1:상담 미포함 2: 상담 포함
print(max(dp))