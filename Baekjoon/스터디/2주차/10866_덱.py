from collections import deque
n = int(input())
dQ = deque()
output=[]
for i in range(n):
    command = input().split()
    if command[0]=="push_back":
        dQ.append(int(command[1]))
    elif command[0]=="push_front":
        dQ.appendleft(int(command[1]))
    elif command[0] == "pop_front":
        if len(dQ) == 0:
            output.append(-1)
        else:
            output.append(dQ.popleft())
    elif command[0] == "pop_back":
        if len(dQ) == 0:
            output.append(-1)
        else:
            output.append(dQ.pop())
    elif command[0] == "size":
        output.append(len(dQ))
    elif command[0] == "empty":
        if len(dQ) == 0:
            output.append(1)
        else:
            output.append(0)

    elif command[0] == "front":
        if len(dQ) == 0:
            output.append(-1)
        else:
            output.append(dQ[0])
    elif command[0] == "back":
        if len(dQ) == 0:
            output.append(-1)
        else:
            output.append(dQ[-1])
for i in range(len(output)):
    print(output[i])