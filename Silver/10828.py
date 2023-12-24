n = int(input())
stack = []
printList = []
for i in range(n):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) != 0:
            printList.append(stack.pop())
        else:
            printList.append(-1)
    elif command[0] == 'size':
        printList.append(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            printList.append(1)
        else:
            printList.append(0)
    elif command[0] == 'top':
        if len(stack) != 0:
            printList.append(stack[-1])
        else:
            printList.append(-1)
    else:
        print('error')
for i in printList:
    print(i)
