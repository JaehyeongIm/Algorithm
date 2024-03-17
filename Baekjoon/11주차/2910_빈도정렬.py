N, C = map(int, input().split())  # 예: 5 2
numberList = list(map(int, input().split()))  # 예: 2 1 2 1 2
count = {}
idx=0
for i in numberList:
    if i in count:
        count[i][0]+=1
    else:
        count[i] = [1,idx]
        idx+=1
# numberList.sort(key=lambda x: (-count[x], numberList.index(x)))
numberList.sort(key=lambda x: (-count[x][0], count[x][1]))

for i in numberList:
    print(i, end=' ')
