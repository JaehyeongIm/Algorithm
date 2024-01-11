import sys

N = int(input())
stack = []
cnt = 0
for i in range(N):
    str = sys.stdin.readline().rstrip()
    for j in str:
        if len(stack) == 0 or stack[len(stack) - 1] != j:
            stack.append(j)
        else:
            stack.pop()
    if len(stack) == 0:
        cnt += 1
    stack.clear()
print(cnt)

## 첫 A랑 마지막 이랑 같은거, 마지막이랑 다른거
