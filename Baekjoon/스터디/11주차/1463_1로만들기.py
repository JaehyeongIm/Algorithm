N = int(input())

D = [0] * (N + 1)
D[1] = 0
# D[i] - i를 1로만드는데 최소 연산 횟수
for i in range(2, N + 1):
    D[i] = D[i - 1] + 1
    if i % 2 == 0:
        D[i] = min(D[i // 2] + 1,D[i])
    if i % 3 == 0:
        D[i] = min(D[i // 3] + 1,D[i])
print(D[N])
