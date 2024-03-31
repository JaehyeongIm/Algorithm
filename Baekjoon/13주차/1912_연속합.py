#1초 - 1억번 연산
# n = 100000, n^2 = 백억 O (nlogn이나 n 필요)

n = int(input())
numberList = list(map(int,input().split()))
print(numberList)
DP = [0] * n # DP[i][j]  = 인덱스 i까지의 최대 연속 합, j는 마지막을 포함하는지 안하는 지 여부
totalSum = numberList[0]

if n >=2:
    for i in range(1, n): # O(n)
        maxValueIncludeI=0
        totalSum = max(totalSum, totalSum+numberList[i])
        DP[i][0] = max(DP[i-1][1],DP[i-1][0])
        DP[i][1] =
# 10 -4 3


