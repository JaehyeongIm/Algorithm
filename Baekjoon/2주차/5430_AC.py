import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
output=[]
for i in range(N):
    commandList = list(sys.stdin.readline().rstrip())
    length = int(sys.stdin.readline().rstrip())
    # 0일때는 error로 예외처리

    # D 명령어 들어왔을때 길이가 0인 경우 flag
    error = False
    array = sys.stdin.readline().rstrip()
    numbers = array[1:-1].split(",")
    dQ = deque(numbers)

    for command in commandList:
        if command == "R":
            dQ.reverse()
        elif command == "D":
            if len(dQ) == 0:
                output.append("error")
                error=True
                break
            else:
                dQ.popleft()
        else:
            output.append("command error")
    if not error:
        output.append("[" + ",".join(dQ) + "]")
for i in output:
    print(i)
