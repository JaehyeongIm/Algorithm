import sys

N, M = list(map(int, input().split()))
graph = [[] for i in range(N+1)]
visited = [False] * (N + 1)
# 그래프 생성

# O(M)=O(N^2)
for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    graph[a].append(b)
    graph[b].append(a)


def dfs(a):
    # 입력된 graph에 a가 없거나 a를 이미 방문 했을경우
    if visited[a] == True:
        return False
    stack =[a]
    visited[a]=True
    #N
    while stack:
        popValue = stack.pop()
        for i in graph[popValue]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    return True


result = 0
# 모든 노드가 스택에 한번 들어갔다 나오므로 O(N)이 걸림
for k in range(1, N + 1):
    if dfs(k):
        result += 1
print(result)
