# 블로그 참고
# 괄호를 한번 치는 건줄 알았는데 여러번 칠 수 있는 거 였음
exp = input().split('-')

num = []
for i in exp:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum) #num에 sum들 다 저장
n = num[0]

for i in range(1,len(num)):
    n -= num[i]
print(n)
