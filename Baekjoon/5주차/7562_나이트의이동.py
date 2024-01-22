from collections import deque


def bfs(start, dest):
    x, y = start
    a, b = dest
    count = 0
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        # 시작노드에서  한번 이동한 노드 와 두번 이동한 노드를 반복문으로 나눠주고, 반복문이 끝날때 count+=1를 진행.
        for _ in range(len(queue)):
            popX, popY = queue.popleft()
            if popX == a and popY == b:
                return count
            for i in range(8):
                nx = popX + dx[i]
                ny = popY + dy[i]
                if 0 <= nx <= l - 1 and 0 <= ny <= l - 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                continue
        count += 1
    return False


dx = [2, 1, 1, 2, -1, -2, -2, -1]
dy = [1, 2, -2, -1, 2, 1, -1, -2]
T = int(input())
output = []
for _ in range(T):
    l = int(input())
    visited = [[False] * l for _ in range(l)]
    x, y = map(int, input().split())
    # 목적지 좌표 a, b
    a, b = map(int, input().split())

    count = bfs([x, y], [a, b])
    output.append(count)
for i in output:
    print(i)
