T = int(input())
result = []
for _ in range(T):
    day = int(input())
    stocks = list(map(int,input().split()))
    stocks.reverse() #뒤의 값에 따라 앞의 연산이 결정되기 떄문에 뒤집기
    resultValue = 0
    maxValue=stocks[0]
    # 10 8 3 5
    for i in range(day):
        if maxValue>=stocks[i]:
            resultValue += maxValue-stocks[i]
        else:
            maxValue=stocks[i]

    result.append(resultValue)


for i in result:
    print(i)
