import sys


output = []
while True: # 입력 수:n 문자열 길이:m O(nm)
    stack = []
    input = sys.stdin.readline().rstrip()
    if input == ".":
        break
    inputList = list(input)
    # 처음 기호로 )이나 ]을 만나는 경우 flag 을 true로 설정하여 output에 no로 설정함.
    flag=True

    for char in inputList:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if len(stack)!=0 and "(" == stack[-1]:
                stack.pop()
            else:
                flag=False
                break
        elif char == "]":
            if len(stack)!=0 and "[" == stack[-1]:
                stack.pop()
            else:
                flag=False
                break

    if len(stack) == 0 and flag: # 바로 )이나 ]을 만나는 경우 스택은 비어있는데 no이기 때문에 flag 사용
        output.append("yes")
    else:
        output.append("no")

for i in output:
    print(i)
