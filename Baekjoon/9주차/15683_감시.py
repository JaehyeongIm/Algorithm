# CCTV 유형별 감시 방향
N, M = map(int, input().split())  # 사무실의 크기 입력 받기
officeRoom = [list(map(int, input().split())) for _ in range(N)]  # 사무실의 상태 입력 받기

# 사무실의 상태를 나타내는 2차원 배열에서 CCTV 위치와 사각 지대(0)의 수 초기화
cctvlist = []  # CCTV 위치 저장
zeroCount = 0  # 사각 지대의 수

for row in range(N):
    for col in range(M):
        if officeRoom[row][col] == 0:
            zeroCount += 1
        elif officeRoom[row][col] != 6:
            cctvlist.append((row, col, officeRoom[row][col]))  # CCTV 위치와 유형 저장

# CCTV 유형별 감시 방향 설정
directions = {
    # 0, 1, 2, 3  = 상. 우, 하, 좌
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌 이동
dy = [0, 1, 0, -1]


# 감시 가능 영역 표시 함수
# 감시 가능 영역 표시 및 감시된 영역의 수를 반환하는 함수
def watch(x, y, direction, temp_isUsed):
    # watched : 탐색한 방의 수
    watched = 0
    # ex. 3번 타입의 cctv direction은 [0,1]
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or officeRoom[nx][ny] == 6:
                break
            if officeRoom[nx][ny] == 0 and not temp_isUsed[nx][ny]:
                temp_isUsed[nx][ny] = True
                watched += 1
    return watched


# 재귀 함수 내에서 감시 영역을 계산하고 zeroCount를 업데이트
def recursion(cur, isUsed, zeroCount):
    global min_zero
    if cur == len(cctvlist):
        min_zero = min(min_zero, zeroCount)
        return

    x, y, cctvType = cctvlist[cur]
    # direction = 특정 타입의 cctv의 한 방향
    for direction in directions[cctvType]:
        # isUsed 복사 (각자의 재귀 마다 독립적인 isUsed만들어주기)
        temp_isUsed = [row[:] for row in isUsed]

        # watched는 해당 cctv type의 한 direction에 대해 탐색 처리 하고 탐색한 방의 수를 리턴
        watched = watch(x, y, direction, temp_isUsed)
        recursion(cur + 1, temp_isUsed, zeroCount - watched)  # watched만큼 사각지대 수 감소


min_zero = 1000000  # 사각 지대의 최소 크기를 저장할 변수
isUsed = [[False] * M for _ in range(N)]  # 감시 영역을 표시할 2차원 배열

recursion(0, isUsed, zeroCount)  # 재귀 함수 실행

print(min_zero)  # 최소 사각 지대의 크기 출력
