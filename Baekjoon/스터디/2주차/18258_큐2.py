from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
queue = deque()
printList = []
for i in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) == 0:
            printList.append(-1)
        else:
            printList.append(queue.popleft())
    elif command[0] == "size":
        printList.append((len(queue)))
    elif command[0] == "empty":
        if len(queue) == 0:
            printList.append(1)
        else:
            printList.append(0)
    elif command[0] == "front":
        if len(queue) == 0:
            printList.append(-1)
        else:
            printList.append(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            printList.append(-1)
        else:
            printList.append(queue[-1])
    else:
        print("error")
for i in range(len(printList)):
    print(printList[i])