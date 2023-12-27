import sys
testCase = int(input())
for _ in range(testCase):
    inputList = list(sys.stdin.readline().rstrip())
    LStack = []
    RStack = []
    for i in inputList:
        if i == "-":
            if LStack:
                LStack.pop()
        elif i == "<":
            if LStack:  
                RStack.append(LStack.pop())
        elif i == ">":
            if RStack:
                LStack.append(RStack.pop())
        else :
            LStack.append(i)
    
    LStack.extend(reversed(RStack))
    print(''.join(LStack))