N = int(input()) # O(n^2) 됨 n=1000
numberList = list(map(int,input().split()))
DP =[[0,0] for i in range(N)] # DP[i] i번째 까지의 수까지의 가장 큰 증가 부분수열
#DP[i][0] : i번째 수 포함안함, DP[i][1] : i번째 수 포함함
sequence = []
DP[0][0]= 0
DP[0][1] = numberList[0]
sequence.append(numberList[0]) # DP[i][1] 즉 i번째 인덱스의 수 포함하는 경우 그 수열을 저장해둠

if N>=2:
    for i in range(1,N):
        # print(f"sequence : {sequence}")
        while sequence[-1] >= numberList[i]: #가장 위의 것이 크거나 같다고 하면 pop 작을떄까지 pop
            sequence.pop()
            if len(sequence)==0:
                break
        sequence.append(numberList[i])
        DP[i][0] = max(DP[i-1][0], DP[i-1][1])
        DP[i][1] = sum(sequence)
        # print(f"포함 x : {DP[i][0]}")
        # print(f"포함 x : {DP[i][1]}")

print(max(DP[N-1][0],DP[N-1][1]))

