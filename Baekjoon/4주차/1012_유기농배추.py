T = int(input())
for i in range(T):
    graph = []
    M,N,K = map(int,input().split())
    for _ in range(N):
        graph.append([0] * N)
    for _ in range(int(K)):
        x, y = map(int,input().split())
        graph[x][y]=1
    for



def bfs(V):
    list=[]
