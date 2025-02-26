import sys
sys.setrecursionlimit(10**5)
# 파이썬 재귀는 기본적으로 1000임 (재귀 반복으로 인한 stack overflow 막기위해서) 이 코드로 늘려줄 수 있음


def dfs(x,y):
    if x<0 or x>=M or y<0 or y>=N:
        return False
    if graph[x][y]== 1:
        #방문처리
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

T = int(input())
resultList=[]
# 테스트 케이스 수 만큼 반복
for i in range(T):
    graph = []
    M,N,K = map(int,input().split())
    result=0
    # 그래프 0으로 세팅
    for _ in range(M):
        graph.append([0] * N)

    # 그래프 입력좌표 1로 세팅
    for _ in range(K):
        x, y = map(int,input().split())
        graph[x][y]=1
    for i in range(M):
        for j in range(N):
            if dfs(i,j)==True:
                result+=1
    resultList.append(result)
for i in resultList:
    print(i)

