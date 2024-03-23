T = int(input())
result=[]

for _ in range(T):
    inputNumber = int(input())
    DP=[0] *(inputNumber+1)
    if inputNumber >=1:
        DP[1] = 1
    if inputNumber >=2:
        DP[2] = 2
    if inputNumber>=3:
        DP[3] = 4
    if inputNumber >=4:
        for i in range(4, len(DP)):
            DP[i] = DP[i-1]+DP[i-2]+DP[i-3]
            
    # 7일때
    # D[6]+1

    # = D[6]

    # D[5]+ 2
    # = D[5]

    # D[4]+3
    # = D[4]

    result.append(DP[inputNumber])



for i in result:
    print(i)



