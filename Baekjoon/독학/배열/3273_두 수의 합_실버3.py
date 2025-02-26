# nlogn 이하
n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
x=int(input())

answer=0
left=0
right=len(numbers)-1
while left<right:
    temp = numbers[left] + numbers[right]
    if temp == x:
        answer+=1
        left+=1
    elif temp>x:
        right-=1
    else:
        left+=1
print(answer)
