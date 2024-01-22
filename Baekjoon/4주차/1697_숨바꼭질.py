from collections import deque
N,K = map(int,input().split())
visited=[0]*1000001 # 노드가 최대 100000개


def bfs(a, b):
    queue = deque()
    # 튜플에 현재 위치와 초 대입
    queue.append((a,0))
    visited[a]=1
    while queue:
        V,steps=queue.popleft()
        if V == b:
            return steps
        for nextNode in [V-1,V+1,2*V]:
            # 노드가 범위 안에 있고 방문하지 않았으면 1초 추가하고 queue에 넣기
            if 0<=nextNode<100001 and  not visited[nextNode] :
                queue.append((nextNode,steps+1))
                visited[nextNode]=1
    # 못 가는 경우 -1 리턴 , 이 문제의 경우 못 갈 수는 없음
    return -1
result = bfs(N,K)
print(result)

# a라는 값의 노드는 인접한 a-1, a+1 , 2a의 노드가 있고 이 구조가 재귀적으로 반복된다.
# 깊이정보를 튜플로 가지고 탐색하며, 방문목록을 list로 따로 두어, 방문하지 않은 노드만 방문한다.
# bfs로 b의 값이 될때까지 탐색한다. 도착한 순간 바로 그 깊이정보가 최단거리 값이 된다.