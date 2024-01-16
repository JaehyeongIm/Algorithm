import sys

sys.setrecursionlimit(10 ** 5)

N = int(input())
graph = []
result = 0
#지도 생성
for _ in range(N):
    graph.append(list(map(int, input())))


count=0
def dfs(a, b):
    #전역 변수로 count를 사용하겠다고 선언
    global count
    # 범위 바깥은 return
    if a < 0 or a > N - 1 or b < 0 or b > N - 1:
        return False
    ## 그래프 값으로 방문 표시
    if graph[a][b] == 1:
        graph[a][b] = 0
        count+=1
        dfs(a + 1, b)
        dfs(a - 1, b)
        dfs(a, b + 1)
        dfs(a, b - 1)
        return count
    return False

output=[]
## 모든 지도의 지점에 대해 dfs 돌리고 true 시 result ++ , 반환값으로 탐색한 노드 수 저장
for i in range(N):
    for j in range(N):
        houstCount = dfs(i,j)
        if houstCount:
            output.append(houstCount)
            # ** 한 탐색의 노드 개수를 저장했으므로 count를 리셋 해줘 야함 (이 부분 뺴먹어서 고생)
            count=0
            result += 1
print(result)

# 정렬 (원본데이터 손상x)
for i in sorted(output):
    print(i)
