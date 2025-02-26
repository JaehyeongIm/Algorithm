# n^2 이하

N = int(input())
numbers = input().split()
v = int(input())
count = 0
for i in numbers:
    if int(i) == v:
        count+=1

print(count)
