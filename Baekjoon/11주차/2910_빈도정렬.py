N, C = map(int, input().split())
numberList = list(map(int, input().split()))
count = {k: 0 for k in numberList}
for i in numberList:
    count[i] += 1


numberList.sort(key=lambda number: (-count[number], numberList.index(number)))
print(numberList)

for i in numberList:
    print(i, end=' ')
