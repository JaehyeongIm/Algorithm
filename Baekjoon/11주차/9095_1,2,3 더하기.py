def countNumber(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return countNumber(n-1) + countNumber(n-2) + countNumber(n-3)
# 4= 1,1,1,1 / 1 1 2 / 2 2 / 3 1 / 2 1 1 / 1 2 1 /1 3

T = int(input())
results = []

for _ in range(T):
    number = int(input())
    results.append(countNumber(number))

for result in results:
    print(result)
