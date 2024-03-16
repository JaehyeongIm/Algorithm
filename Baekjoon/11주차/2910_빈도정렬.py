N, C = map(int, input().split())
numberList = list(map(int, input().split()))
print(numberList)
count = {k: 0 for k in numberList}
for i in numberList:
    count[i] += 1


numberList.sort(key=lambda x: (-count[x], numberList.index(x)))
print(numberList)

for i in numberList:
    print(i, end=' ')
