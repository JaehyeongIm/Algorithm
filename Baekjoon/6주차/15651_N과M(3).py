import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [0] * M # 수열을 저장할 배열 (0 인덱싱)


# k개의 수를 택한 상황에서 arr[k] 정하고 출력하는 함수 (k: 인덱스)
# 중복 가능
def recursion(k):
    # 1. 종료 지점 설정
    # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
    if k == M:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
        return
    # 2. step (k<M)
    for i in range(1, N + 1):
        arr[k] = i
        recursion(k + 1)

recursion(0)
