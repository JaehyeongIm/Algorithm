n = int(input())
m = int(input())
count =0
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
friend = []
# 1과 연결된 친구
if graph[1]:
    for i in graph[1]:
        friend.append(i)
    # 친구의 친구
    for node in graph[1]:
        for value in graph[node]:
            # 친구의 친구 중 friend 에 없고 1이 아니면 추가
            if value != 1 and value not in friend:
                friend.append(value)
print(len(friend))