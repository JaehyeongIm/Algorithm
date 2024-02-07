import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, sum = map(int, input().rstrip().split())
inputList = list(map(int, input().rstrip().split()))
arr = [0] * N
isUsed = [0] * N  # 중복 제거용

count = 0


# k : 합
def recursion(k, currentSum):
    global count
    # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
    if k and currentSum == sum:
        count += 1  
    if k == N:
        return
    # 순서대로 하는게 아님. 듬성 듬성 포함할 수 도 있음
    # for i in inputList:
    #     usedIndex = inputList.index(i)
    #     if not isUsed[usedIndex]:
    #         arr[k] = i
    #         isUsed[usedIndex] = 1
    #         recursion(k + 1, currentSum+i)
    #         # 재귀가 끝나면 사용 표시 제거
    #         isUsed[usedIndex] = 0
    
    #현재 원소 미포함
    recursion(k + 1, currentSum)
    # 현재 원소 포함
    recursion(k+1 , currentSum+inputList[k])


recursion(0, 0)
print(count)
