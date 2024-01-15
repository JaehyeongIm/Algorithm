from collections import deque

n = int(input())
a, b = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
# 리스트에 부모, 자식 관계 입력
for i in range(m):
    parent, child = list(map(int, input().split()))
    graph[parent].append(child)
    graph[child].append(parent)


def bfs(a, b):
    result = 0  # a와 b의 거리
    q = deque([a])
    visited[a] = True
    while q:
        # 현재 깊이의 노드 수
        nodeCount = len(q)
        # 현재 깊이의 노드를 처리하는 반복문 따로 생성 (한 층 계산하고 끊어주기)
        for _ in range(nodeCount):
            popValue = q.popleft()
            if popValue == b:
                return result
            # d 인접한 노드 큐에 추가
            for i in graph[popValue]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        result += 1
    # 연결 안될 경우
    return -1


output = bfs(a, b)
print(output)
