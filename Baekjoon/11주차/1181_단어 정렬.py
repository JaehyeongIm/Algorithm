N = int(input())
str =[]
for i in range(N):
    temp = input()
    if temp in str:
        continue
    else:
        str.append(temp)
str.sort(key=lambda x:(len(x),x))
for i in str:
    print(i)
