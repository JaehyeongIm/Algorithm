N, K = list(map(int, input().split()))
valueList=[]
for _ in range(N):
    valueList.append(int(input()))

# 최소 거리값 찾기

count = 0
totalSum=0
while True:
    minlength=1000000000
    idx=-1
    # 최소거리값 찾기
    for i in range(len(valueList)):
        if totalSum+valueList[i] <= K :
            if (4200-valueList[i]) < minlength:
                minlength=4200-valueList[i]
                idx= i # 최솟값 인덱스
                # print(valueList[i])

    totalSum+=valueList[idx]
    count+=1
    if totalSum == K:
        print(count)
        break