import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [0] * M
numberList = map(int,input().rstrip().split())

sortedList = sorted(numberList)
isUsed = [0] * (max(sortedList) + 1)  # 중복 제거용

# arr[k] 포함하여 이후에 올 값을 다 정하는 재귀함수 (k는 인덱스)
def recursion(k):
    # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
    if k == M:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
        return

    for i in sortedList:
        if not isUsed[i]:
                arr[k] = i
                isUsed[i] = 1
                recursion(k + 1)
                isUsed[i] = 0


recursion(0)
