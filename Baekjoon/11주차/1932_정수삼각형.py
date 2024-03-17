n = int(input())
triangle=[]
for _ in range(n):
    triangle.append(list(map(int,input().split())))
# D[i] i열일때 수의 합의 최댓값
D = [[0] * i for i in range(1,n+1)]

D[0][0] = triangle[0][0]
if n >=2:
    D[1][0] = D[0][0]+triangle[1][0]
    D[1][1] = D[0][0] + triangle[1][1]
if n>=3:
# i : 행, j :열
    for i in range(2,n):
        for j in range(i+1):
            if j ==0:
                D[i][j] = D[i-1][j]+triangle[i][j]
            elif j == i:
                D[i][j] = D[i-1][j-1]+triangle[i][j]
            else:
                D[i][j] = max(D[i-1][j-1] + triangle[i][j], D[i-1][j]+triangle[i][j])

print(max(D[n-1]))