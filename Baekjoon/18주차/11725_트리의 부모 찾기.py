from collections import deque
N = int(input())
p = [0] * (N+1)
adj = [[] for _ in range(N+1)] # 인접리스트
for i in range(N-1):
    node1, node2 = map(int,input().split())
    adj[node1].append(node2)
    adj[node2].append(node1)

def bfs(root):
    queue = deque([])
    queue.append(root)
    while len(queue) > 0:
        cur = queue.popleft()
        for node in adj[cur]:
            if node == p[cur]: #인접 노드가 부모일때는 넘어가기
                continue
            queue.append(node)
            p[node] = cur
bfs(1)
for i in p[2:]:
    print(i)


