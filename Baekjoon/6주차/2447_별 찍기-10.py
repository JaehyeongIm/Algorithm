import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input().rstrip())

matrix = [["*"] * N for i in range(N)]

# length * length 행렬에서 가운데를 뚫은 패턴을 matrix에 재귀적으로 구현하는 함수
def recursion(length, row, column):

    # base condition
    if length == 3:
        matrix[row + 1][column + 1] = " "
        return

    # step
    else:
        for i in range(length // 3):
            for j in range(length // 3):
                # 가운데 구멍 뚫기
                matrix[row + length // 3 + i][column + length // 3 + j] = " "
        # 가운데르 제외한 나머지 8방향에서 재귀호출
        recursion(length // 3, row, column)
        recursion(length // 3, row, column + length // 3)
        recursion(length // 3, row, column + 2 * length // 3)
        recursion(length // 3, row + length // 3, column)
        recursion(length // 3, row + length // 3, column + 2 * length // 3)
        recursion(length // 3, row + 2 * length // 3, column)
        recursion(length // 3, row + 2 * length // 3, column + length // 3)
        recursion(length // 3, row + 2 * length // 3, column + 2 * length // 3)
        return

# 출력

recursion(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end="")
    print("")
