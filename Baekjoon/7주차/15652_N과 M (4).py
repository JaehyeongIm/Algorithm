import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
arr = [0]*M

# arr[k] 정하는 함수 (k는 인덱스)
def recursion(k):
    # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
    if k == M:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1,N+1):
            # 첫번째 자리거나 i가 그 전 자리 수보다 크거나 같을 때 (비내림차순)
            if k==0 or i>=arr[k-1]:
                arr[k] = i
                recursion(k + 1)



recursion(0)
