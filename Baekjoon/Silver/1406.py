import sys
leftStack = list(sys.stdin.readline().rstrip())
rightstack = []
commandCount = int(sys.stdin.readline().rstrip())
for i in range(commandCount):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if leftStack:
            rightstack.append(leftStack.pop())
        
    elif command[0] == 'D':
        if rightstack:
            leftStack.append(rightstack.pop())
    elif command[0] == 'B':
        if leftStack:
            leftStack.pop()

    elif command[0] == 'P':
        leftStack.append(command[1])

print(''.join(map(str, leftStack)), ''.join(map(str, reversed(rightstack))),sep="")
