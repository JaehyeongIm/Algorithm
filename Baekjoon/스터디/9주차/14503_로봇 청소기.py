import sys

sys.setrecursionlimit(1000000)
N, M = list(map(int, input().split()))
x, y, d = list(map(int, input().split()))
room = []
for i in range(N):
    room.append(list(map(int, input().split())))  # 입력을 정수로 변환

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서 , 여기서 dx,dy는 x,y 좌표가 아니라 행과 열의 변화량임.
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]  # 방문 배열 크기 수정
cnt = 0

# x는 행, y는 열
def dfs(x, y, d):
    global cnt
    if not visited[x][y]:
        visited[x][y] = True
        cnt += 1
    # 청소되지 않는 빈칸이 있는 경우
    for _ in range(4):
        # 90도 회전
        if d==0:
            nd=3
        else:
            nd= d-1
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 범위 안에 있고 벽이 아닐때, 청소안한 방일떄 전진
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny, nd)
            return
        d = nd
    # 청소되지 않는 빈칸이 없는 경우
    nd = (d + 2) % 4  # 후진 방향
    nx = x + dx[nd]
    ny = y + dy[nd]
    # 범위 안에 있고 벽이 아닐때 후진
    if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
        dfs(nx, ny, d)

dfs(x, y, d)
print(cnt)
