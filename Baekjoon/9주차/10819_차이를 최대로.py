
# 문제 이해 잘 못함. 짝수번쨰에서 홀수번째 뺴는 문제인줄 알았음. 그게 아니라 인접한 요소의 차이를 계산하는 문제였음, 또한 절댓값을 간과함
# N = int(input())
# array = list(map(int, input().split()))
# max = -100000
# isUsed = [0] * 8
#
#
#
# def recursion(idx, sum):
#     global max
#     if idx == N:
#         if sum > max:
#             max = sum
#         return
#     # i 는 배열의 인덱스, 중복 체크 배열도 이 인덱스에 맞게 사용
#     for i in range(N):
#         if isUsed[i] != 1:
#             isUsed[i] = 1
#             if idx % 2 ==0 :
#                 recursion(idx + 1, sum+array[i])
#             else:
#                 recursion(idx + 1, sum-array[i])
#             isUsed[i] = 0
#
#
#
#
# recursion(0, 0)
# print(max)
import sys
sys.setrecursionlimit(100000000)
N = int(input())
array = list(map(int, input().split()))
max = -100000
isUsed = [0] * 8
list =[]

def recursion(cur, sum):
    global max
    if cur == N:
        if sum > max:
            max = sum
        return
    # i 는 배열의 인덱스, 중복 체크 배열도 이 인덱스에 맞게 사용
    for i in range(N):
        # 첫번째 자리는 그냥 sum 전달

        if cur==0:
            if isUsed[i] == 0:
                isUsed[i] = 1
                list.append(array[i])
                recursion(cur + 1, sum)
                list.pop()
                isUsed[i] = 0
        # 두번째 자리부터 앞의 것과 차 계산
        else:
            if isUsed[i] == 0:
                isUsed[i] = 1
                list.append(array[i])
                recursion(cur + 1, sum + abs(list[cur-1] - list[cur]))
                list.pop()
                isUsed[i] = 0


recursion(0, 0)
print(max)
