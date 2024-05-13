import heapq

N = int(input())
numberList =[]
for i in range(N):
    heapq.heappush(numberList, int(input()))
count = 0
while len(numberList) >=2: # 카드 1뭉치가 남으면 끝냄
    a = heapq.heappop(numberList)
    b = heapq.heappop(numberList)
    count += (a+b)
    heapq.heappush(numberList,a+b)

print(count)
