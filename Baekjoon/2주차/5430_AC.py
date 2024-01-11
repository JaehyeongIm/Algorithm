import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
output = []
for i in range(N):  # n
    commandList = list(sys.stdin.readline().rstrip())
    length = int(sys.stdin.readline().rstrip())
    # 0일때는 error로 예외처리

    # D 명령어 들어왔을때 길이가 0인 경우 flag
    isError = False
    array = sys.stdin.readline().rstrip()[1:-1].split(",")
    
    # 빈 배열 을 따로 처리해줘야함, slice하면 ' ' , split하면 [] 가 됨
    if array != ['']:
        numbers=list(array)
    else:
        numbers=[]

    dQ = deque(numbers)
    isReversed = False
    for command in commandList:  # O(k)
        if command == "R":
            # dQ.reverse()  k가 걸려서 너무 오래걸림 O(k^2)
            if isReversed==False:
                isReversed = True
            else:
                isReversed=False

        elif command == "D":
            if not dQ: # 빈 배열일 때 에러출력
                output.append("error")
                isError = True
                break
            elif isReversed == False:
                dQ.popleft()
            elif isReversed == True:
                dQ.pop()
        else:
            output.append("command error")
    if not isError: # O(k)
        if not isReversed:
            output.append("[" + ",".join(dQ) + "]")
        else:
            dQ.reverse()
            output.append("[" + ",".join(dQ) + "]")
for i in output:
    print(i)
