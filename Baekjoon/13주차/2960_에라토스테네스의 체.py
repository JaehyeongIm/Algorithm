from collections import deque

N, K = list(map(int, input().split()))
# 1초 : 1억 , O(n^2) 됨 1000, 1000
numberList = deque([])
for i in range(2, N + 1):
    numberList.append(i)
print(numberList)
cnt = 0
while True:
    number = numberList.popleft()
    cnt += 1
    j = 2
    if cnt == K:
        break
    while True:  # 배수 지우기
        for i in range(len(numberList)):
            if numberList[i] == number * j:
                numberList.remove(number * j)
                cnt += 1
                j += 1
                break
        if cnt == K:
            break

print(cnt)
