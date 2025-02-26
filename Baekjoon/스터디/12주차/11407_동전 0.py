N, K = map(int, input().split())
valueList=[]
for _ in range(N):
    valueList.append(int(input()))

count = 0
for i in reversed(range(N)):
    if valueList[i] <= K :
        count += K // valueList[i] # 가장 큰 돈으로 나누기
        K = K % valueList[i] #잔액 수정
        if K==0:
            break

print(count)

