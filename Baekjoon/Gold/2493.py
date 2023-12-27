n = int(input())
k = list(map(int, input().split()))
answer = []
stack = []
for i in range(n): # n 
    while stack:
        if stack[-1][1] > k[i]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i,k[i]])
print(" ".join(map(str, answer)))   


        
    
