result = []
while True:
    L, P, V = list(map(int,input().split()))
    if L == 0 and P ==0 and V ==0:
        break
    quotient = V//P
    remainder = V % P
    result.append(quotient*L+min(remainder,L)) #남은 날이 L보다 작으면 남은 날만 큼 사용, 남은 날이 L보다 크면 L만큼 사요가능 
for i in range(len(result)):
    print(f"Case {i+1}: {result[i]}")


