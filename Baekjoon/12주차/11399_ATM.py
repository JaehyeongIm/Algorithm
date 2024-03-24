N = int(input())
timeList = list(map(int,input().split()))
timeList.sort()
totalSum=0
for i in range(N):
    totalSum += timeList[i]*(N-i)
print(totalSum)
# 빨리 끝내는 순서
# 누적해서 더해나가야함

# length =len(timeList)
# totalsum=0
# def findMin(k):
#     global totalsum
#     if k == length:
#         print(totalsum)
#         return
#     minIndex= 0
#     minValue=100000
#     for i in range(len(timeList)): # 최솟값, 최소 인덱스 찾기
#         if minValue > timeList[i]:
#             minValue = timeList[i]
#             minIndex=i
#     print(timeList.pop(minIndex)) # timeList에서 최솟값 제거
#     totalsum+=minValue
#     findMin(k+1)
# findMin(0)