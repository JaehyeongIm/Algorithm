from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)] # 인접행렬
resultGraph = [[0]*N for i in range(N)] # 결과 인접행렬, 방문 배열로 사용

def bfs():
    queue = deque([])
    for i in range(N):
        queue.append(i)
        while queue: # 노드 큐에서 빼고 인접노드들 다시 큐에 넣는 로직
            node = queue.popleft()
            for j in range(N):
                if graph[node][j] == 1 and resultGraph[i][j] ==0: # 연결되어있고 결과 인접행렬에 표시 안되어있을때
                    queue.append(j)
                    resultGraph[i][j] = 1


bfs()
for row in resultGraph:
    print(*row)
