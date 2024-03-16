T = int(input())
import copy



def dfs(array, plusCount):
    global totalCount
    global usedArray
    if plusCount == 1:
        return
    for i in range(plusCount):
        newArray = copy.deepcopy(array)
        newArray[i] = array[i] + array[i + 1]
        newArray.pop(i + 1)
        ## 중복 체크
        usedArray.append(newArray)

        flag = False
        for i in usedArray:
            if i == newArray:
                flag = True
        if not flag:
            totalCount += 1
            # print(newArray)
        ## dfs
        dfs(newArray, plusCount - 1)

result = []
# i numberList의 숫자 인덱스
for i in range(T):
    number = int(input())
    plusCount = number - 1
    numberList = [1] * number
    totalCount = 0
    usedArray = []

    dfs(numberList, plusCount)
    # 1,1,1,1 까지 더해줘야함
    result.append(totalCount + 1)

for j in result:
    print(j)
