# n = int(input())
# k = list(map(int, input().split()))
# answer = []
# stack = []
# for i in range(n): # n 
#     while stack:
#         if stack[-1][1] > k[i]:
#             answer.append(stack[-1][0]+1)
#             break
#         else:
#             stack.pop()
#     if not stack:
#         answer.append(0)
#     stack.append([i,k[i]])
# print(" ".join(map(str, answer)))   


# 인덱스로 했는데 시간초과
n = int(input())
k = input().split()
map(str,k)
answer = []
for i in range(len(k)): # n 
    result = False 
    j=i
    while j !=0:
        j -=1
        if(k[i]<k[j]):
            answer.append(j+1)
            result = True
            break
        
    if not result:
        answer.append(0)
print(" ".join(map(str, answer)))   


        
    

        
    
