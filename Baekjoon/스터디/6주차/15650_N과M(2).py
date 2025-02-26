import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
arr = [0]*M
isUsed = [0]*(N+1) # 중복 제거용

# k개의 수를 택한 상황에서 arr[k] 정하고 출력하는 함수 (0인덱싱)
def recursion(k):
    # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
    if k == M:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1,N+1):
        if not isUsed[i] :
            # 첫번째 자리거나 i가 그 전 자리 수보다 클 때 (오름차순)
            if k==0 or i>arr[k-1]:
                arr[k] = i
                isUsed[i] = 1
                recursion(k + 1)
                # 재귀가 끝나면 다시 k번째 뽑기
                isUsed[i] = 0


recursion(0)
