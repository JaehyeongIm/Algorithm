k = int(input())
list = []
for i in range(k):
    inputNumber = int(input())
    if inputNumber==0:
        list.pop()
    else:
        list.append(inputNumber)
sum=0
for i in list:
    sum+=i
print(sum)
    
