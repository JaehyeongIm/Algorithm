n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]
for i in range(1, n):
    d[i] = max(array[i], d[i-1]+array[i]) #직전의 부분합이 양수면 이어가고, 음수면 새로시작
print(max(d))