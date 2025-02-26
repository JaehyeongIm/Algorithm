# 1. 입력 : 첫줄
tempList = input().split()
N = int(tempList[0])
restList = tempList[1:]
# 1.1 뒤집어서 받기
for i in range(len(restList)):
    restList[i] = restList[i][::-1]
    # 0 제거
    while restList[i][0] == "0":
        restList[i] = restList[i][1:]
numbers = []
numbers.extend(restList)

# 2. 입력 : 두번째 줄부터
while len(numbers) < N:
    temp = input().split()
    # 2.1 뒤집어서 받기
    for i in range(len(temp)):
        temp[i] = temp[i][::-1]
        # 0 제거
        while temp[i][0] == "0":
            temp[i] = temp[i][1:]
    numbers.extend(temp)
result = list(map(int,numbers))
result.sort()
for i in result:
    print(i)
