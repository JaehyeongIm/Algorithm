N, K = map(int, input().split())
valueList=[]
for _ in range(N):
    valueList.append(int(input()))

count = 0
for i in reversed(range(N)):
    if valueList[i] <= K :
        count += K // valueList[i]
        K = K % valueList[i]
        if K==0:
            break

print(count)

