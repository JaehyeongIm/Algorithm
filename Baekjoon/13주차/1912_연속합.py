n = int(input())
numberList = list(map(int, input().split()))

d = [0] * n
d[0] = numberList[0]
for i in range(1, n):
    d[i] = max(numberList[i], d[i-1]+numberList[i]) #직전의 부분합이 양수면 이어가고, 음수면 새로시작
print(max(d))