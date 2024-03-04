import sys

sys.setrecursionlimit(1000000)


k = int(input())
inequalitySignList = input().split()
#결과 배열
result=[]
# 만들어가는 배열
stringArray=[]
isUsed = [False for i in range(10)]

def inequiltySignIsOk(x,y,operation):
    if operation == ">":
        if x>y:
            return True
        else:
            return False
    else:
        if x>y:
            return False
        else:
            return True

#cur: 재귀 횟수
def dfs(cur):
    if cur== k+1:
        result.append(''.join(map(str, stringArray)));
        return
    # i가 0일때는 stringArray에 대해 인덱스 -1에 접근하니까 i==0 일때 조건 추가
    for i in range(10):
        if cur == 0 or (not isUsed[i] and inequiltySignIsOk(stringArray[cur-1],i,inequalitySignList[cur-1])):
            isUsed[i]=True
            stringArray.append(i)
            dfs(cur+1)
            stringArray.pop()
            isUsed[i]=False

dfs(0)
#최댓값, 최솟값 계산 따로 NO , 가장 처음에 성립한 숫자 배열이 최소, 나중이 최대임
print(result[-1])
print(result[0])





