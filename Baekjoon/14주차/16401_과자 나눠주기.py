import sys
input = sys.stdin.readline

m, n = list(map(int, input().rstrip().split()))
snacks = list(map(int, input().rstrip().split()))
res = 0

start = 1
end = 10 ** 9
while start <= end:
    mid = (start + end) // 2 # 조카에게 나눠줄 과자의 크기
    total = 0              #  total은 mid의 길이로 과자를 나누어주었을 때 받을 수 있는 사람의 수
    for snack in snacks:
        total += snack // mid
    if total >= m:
        res = max(res, mid) # res은 결과
        start = mid + 1
    elif total < m:
        end = mid - 1

print(res)