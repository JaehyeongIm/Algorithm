import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, targetSum = map(int, input().rstrip().split())
inputList = list(map(int, input().rstrip().split()))
count = 0

# 부분집합의 합을 계산하여 목표 합과 비교하고, 카운트하는 함수
def recursion(idx, current_sum):
    global count

    # 부분집합의 합이 목표 합과 일치하면 카운트
    if idx!= 0 and current_sum == targetSum:
        count += 1

    # 현재 인덱스 이후의 수들을 포함하는 부분집합 생성
    # 현재 수의 다음 수부터 뽑을 수 있게 반복문 처리 => 순서, 중복 제거
    for i in range(idx, N):
        recursion(i + 1, current_sum + inputList[i])

# 백트래킹 함수 호출
recursion(0, 0)
print(count)
