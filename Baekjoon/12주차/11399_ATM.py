N = int(input())
timeList = list(map(int,input().split()))
timeList.sort()
totalSum=0
for i in range(N):
    totalSum += timeList[i]*(N-i)
print(totalSum)
# 빨리 끝내는 순서로 정렬하고 숫자 뺼떄마다 totalsum에 남은 개수만큼 더해줌
