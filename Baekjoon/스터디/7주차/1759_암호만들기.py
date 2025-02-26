import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

L, C = map(int,input().rstrip().split())
arr = [0]*L
isUsed = [0]*C # 중복 제거 (인덱스에 해당하는 arr 요소의 중복 여부)

numberList = sorted(input().rstrip().split())
# k개의 수를 택한 상황에서 arr[k] 정하고 출력하는 함수 (0인덱싱)
def recursion(k):
    # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
    if k == L:
        vowelCount =0
        consonantCount=0
        # 자음, 모음 수 세기
        for i in range(len(arr)):
            if arr[i] == "a" or arr[i] == "e" or  arr[i] == "i" or arr[i] == "o" or arr[i] == "u":
                vowelCount += 1
            else:
                consonantCount += 1
        # 최소 모음 하나, 자음 둘 이상인 경우만 출력
        if vowelCount>=1 and consonantCount>=2:
            for i in range(len(arr)):
                print(arr[i], end="")
            print()
            return
        return

    for i in numberList:
        if not isUsed[numberList.index(i)] :
            if k==0 or arr[k-1]< i:
                arr[k] = i
                isUsed[numberList.index(i)] = 1
                recursion(k + 1)
                # 재귀가 끝나면 사용표시 해제
                isUsed[numberList.index(i)] = 0

recursion(0)
