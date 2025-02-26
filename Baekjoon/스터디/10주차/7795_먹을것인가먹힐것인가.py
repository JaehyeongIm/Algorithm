T = int(input())
resultList=[]
for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    start = 0
    count = 0
    # A를 기준으로 비교
    for j in range(N):
        while True:

            if start == M or A[j] <= B[start]:
                count += start
                break
            else:
                start += 1

    resultList.append(count)

for i in resultList:
    print(i)