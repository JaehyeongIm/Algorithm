
def sum_digit(x):
    # isdigit() string의 모든 문자가 숫자일떄 True
    return sum([int(i) for i in x if i.isdigit()])

N = int(input())
stringList = []
for _ in range(N):
    stringList.append(input())
# key는 정렬조건 지정
stringList.sort(key=lambda x: (len(x), sum_digit(x), x))

for i in stringList:
    print(i)
