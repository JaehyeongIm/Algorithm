#  입력
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
# 팀 배정상태 표시 (true면 스타트팀, false면 링크팀)
visited = [False for _ in range(N)]
res = 10000000000


# DFS
def dfs(peopleCount,idx):
    global res
    if peopleCount == N//2:
        A = 0
        B = 0
        # 방문한 곳에 대해 (A 인원) 능력치 합 더하기
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
        res = min(res, abs(A-B))
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            dfs(peopleCount+1,i+1)
            visited[i] = False

dfs(0,0)
print(res)