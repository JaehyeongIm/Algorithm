# n log n 이하 O(M)
from collections import deque
import sys
input = sys.stdin.readline
LStack = list(input().rstrip())
M = int(input().rstrip())
RStack=deque([])
commands=[]
for i in range(M):
    commands.append((input().rstrip().split()))
for i in range(M):
    if commands[i][0] == "P":
        LStack.append(commands[i][1])
    elif commands[i][0] == "L" and LStack:
        RStack.appendleft(LStack.pop())
    elif commands[i][0] == "D" and RStack:
        LStack.append(RStack.popleft())
    elif commands[i][0] == "B" and LStack:
        LStack.pop()

for i in LStack:
    print(i,end="")
for j in RStack:
    print(j,end="")





