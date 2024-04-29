N, M = list(map(int,input().split()))
passwordList = dict()
outputList = []
for _ in range(N):
    data = input().split()
    passwordList[data[0]]= data[1]
for _ in range(M):
    outputList.append(passwordList[input()])
for i in outputList:
    print(i)