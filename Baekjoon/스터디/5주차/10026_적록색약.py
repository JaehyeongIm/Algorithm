import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())

# 색상 배열
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

normal_cnt, blind_cnt = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    #현재 색상 좌표를 방문해준다.
    visited[x][y] = True
    current_color = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            # 방문하지 않았고, 현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs
            if visited[nx][ny]==False:
                if graph[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs
        if visited[i][j]==False:
            dfs(i,j)
            normal_cnt += 1

#blind 실행 전에 R를 G로 다 바꿔줌
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

#visited 초기화
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            blind_cnt += 1

print(normal_cnt,blind_cnt)