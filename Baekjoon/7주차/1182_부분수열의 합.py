# import sys
#
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
#
# N, targetSum = map(int, input().rstrip().split())
# inputList = list(map(int, input().rstrip().split()))
# arr = [0] * N
# isUsed = [0] * N  # 중복 제거용
#
# count = 0
#
# # k개의 수를 택한 상황에서 arr[k] 정해주는 함수 (k: 인덱스)
# # k : 합
# def recursion(k, currentSum):
#     global count
#     # k 가 m이 되면 m개를 모두 골라서 수열이 만들어 지므로 출력
#     if k and currentSum == targetSum:
#         count += 1
#         for i in range(len(arr)):
#             print(arr[i], end=" ")
#         print()
#     if k == N:
#         return
#     # 차례로 하는게 아님. 듬성 듬성 포함할 수 도 있음, 또한 순서를 고려하지 않음
#     # for i in inputList:
#     #     usedIndex = inputList.index(i)
#     #     if not isUsed[usedIndex]:
#     #         arr[k] = i
#     #         isUsed[usedIndex] = 1
#     #         #현재 수를 포함하는 경우
#     #         recursion(k + 1, currentSum + i)
#     #         #현재 수를 안 포함하는 경우
#     #
#     #         recursion(k + 1, currentSum)
#     #         # 재귀가 끝나면 사용 표시 제거
#     #         isUsed[usedIndex] = 0
#     # 1개 뽑을때, 2개뽑을때 .. N개뽑을때로 나눔
#     for i in range(1,N+1):
#
#         templist=[]
#
#
#
#
#
# recursion(0, 0)
# print(count)
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
    for i in range(idx, N):
        recursion(i + 1, current_sum + inputList[i])

# 백트래킹 함수 호출
recursion(0, 0)
print(count)
