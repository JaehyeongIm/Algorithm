#O(TN)
import sys
input = sys.stdin.readline
T = int(input().rstrip())
test=[]
for i in range(T):
    test.append(input().rstrip())
for sequence in test:
    RStack =[]
    LStack = []
    for char in sequence:
        if char == "<":
            if LStack:
                RStack.append(LStack.pop())
        elif char == ">":
            if RStack:
                LStack.append(RStack.pop())
        elif char == "-":
            if LStack:
                LStack.pop()
        else:
            LStack.append(char)
    for i in LStack:
        print(i,end="")
    for j in reversed(RStack):
        print(j,end="")
    print()