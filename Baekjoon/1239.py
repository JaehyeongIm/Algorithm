N = int(input())
dogList = list(map(int, input().split()))
fiftyflag = False
fiftyOverFlag = False
fiftydownFlag = False
visited = [False] * len(dogList)
count = 0
for i in dogList:
    if i == 50:
        fiftyflag = True
    if i >= 50:
        fiftyOverFlag = True

if fiftyflag:
    count = 1
elif fiftyOverFlag:
    count = 0
else:
    arrayLength = len(dogList)
    for i in range(arrayLength):
        for j in range(i + 1, arrayLength):
            if dogList[j] == dogList[i]:
                dogList.pop(j)
                dogList.pop(i)
                count += 1

print(count)
