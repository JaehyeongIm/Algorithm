N, C = map(int, input().split())  # 예: 5 2
numberList = list(map(int, input().split()))  # 예: 2 1 2 1 2
count = {} # 빈도와 인덱스 저장
idx=0
for i in numberList:
    if i in count:
        count[i][0]+=1
    else: #처음 count에 들어올때 빈도수 1과 인덱스를 저장
        count[i] = [1,idx]
        idx+=1

# numberList.sort(key=lambda x: (-count[x], numberList.index(x))) < 두번째 기준이 왜안되는지 모르겠음

print(count)
numberList.sort(key=lambda x: (-count[x][0], count[x][1]))

for i in numberList:
    print(i, end=' ')
