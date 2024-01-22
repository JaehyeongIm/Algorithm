import sys
sys.setrecursionlimit(10 ** 5)


N = int(input())
area = []
maxValue = 0
result = 0
# O(N)
for i in range(N):
    inputList = list(map(int, input().split()))
    # 입력받을 때 maxValue 저장 (빗물의 높이가 maxValue까지 loop 돌게 하기 위해서)
    if maxValue < max(inputList):
        maxValue = max(inputList)
    area.append(inputList)


def dfs(i, j, maxHeight):
    # 범위 벗어나면 False 종료
    if i < 0 or i > N - 1 or j < 0 or j > N - 1:
        return False

    # 빗물 양 보다 같거나 작으면 False 종료 / 이렇게 하면 안전한 영역만 탐색
    if area[i][j] <= maxHeight:
        return False

    if visited[i][j] == False:
        visited[i][j] = True
        dfs(i + 1, j, maxHeight)
        dfs(i - 1, j, maxHeight)
        dfs(i, j + 1, maxHeight)
        dfs(i, j - 1, maxHeight)
        return True
    return False
#

for maxHeight in range(maxValue + 1):
    tmp = 0
    # 초기화
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 안전한 영역이 발견될 때 tmp+=1
            if dfs(i, j, maxHeight) == True:
                tmp += 1
    # 최댓값 계산
    if tmp > result:
        result = tmp
print(result)
