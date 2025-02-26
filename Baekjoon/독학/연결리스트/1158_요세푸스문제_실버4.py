#O(n)
N,K = map(int,input().split())
numbers = [i+1 for i in range(N)]
idx=0
result=[]
while numbers:
    idx= (idx+K-1)%len(numbers)
    result.append(numbers.pop(idx))
for i in range(len(result)):
    if i==0:
        print("<",end="")
    if i == len(result)-1:
        print(result[i],end="")
        print(">")
    else:
        print(result[i],end=", ")
