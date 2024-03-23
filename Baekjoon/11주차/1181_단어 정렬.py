N = int(input())
str =[]
for i in range(N):
    temp = input()
    if temp in str: #중복 제거
        continue
    else:
        str.append(temp)
str.sort(key=lambda x:(len(x),x)) # 1.길이, 2 문자 순서
for i in str:
    print(i)
