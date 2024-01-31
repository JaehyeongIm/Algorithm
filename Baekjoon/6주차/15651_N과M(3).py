import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = input().rstrip().split()
arr = []
isUsed = [0]*N

# 1부터 N까지 중복을 허용하면서  M개를 고른 뒤 수열을 출력하는 함수
def recursion(k):
    # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
    if k == M:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        return

    for i in range(N):
        if not isUsed[i]:
            arr[k] = i
            isUsed[i] = 1
            recursion(k + 1)
            isUsed[i] = 0


recursion(0)
