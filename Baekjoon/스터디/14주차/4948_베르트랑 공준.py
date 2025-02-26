decimal = [0] * 2 + [1] * 246912 #입력이 1<n<=123,456 이니 소수를 그 두배 까지 계산해야함

#에라토스테네스의 체 사용
for i in range(2, 246913):
    if decimal[i]:
        for j in range(i * 2, 246913, i):
            decimal[j] = 0  # 0=소수가 아님 / 1=소수임
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(decimal[n+1:n*2+1]))

