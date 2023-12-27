count = 1
result = True
stack = []
opList = []

N= int(input())
for i in range(N):
    num = int(input())
    while count<=num:
        stack.append(count)
        count+=1
        opList.append('+')
    if(stack[-1] == num):
        stack.pop()
        opList.append('-')
    else:
        result = False
        break

if result == False:
    print("NO")
else:
    for i in opList:
        print(i)

    

        