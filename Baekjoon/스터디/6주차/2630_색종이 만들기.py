import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input().rstrip())
matrix = []
# 입력값 정수 타입으로 저장
bluePaperCount = 0
whitePaperCount = 0
for i in range(N):
    matrix.append(list(map(int, input().rstrip().split())))


def recursion(size, row, column):
    global bluePaperCount
    global whitePaperCount

    if size == 1:
        if matrix[row][column] == 0:
            whitePaperCount += 1
        elif matrix[row][column] == 1:
            bluePaperCount += 1
        return
    # 행렬안의 요소가 다른지 비교
    isDiffrent = False

    for i in range(size):
        for j in range(size):
            if matrix[row][column] != matrix[row + i][column + j]:
                isDiffrent = True
                break
        if isDiffrent:
            break
    # 다르면 재귀
    if isDiffrent:
        recursion(size // 2, row, column)
        recursion(size // 2, row, column + size // 2)
        recursion(size // 2, row + size // 2, column)
        recursion(size // 2, row + size // 2, column + size // 2)
        
    # 같으면 색종이 개수 추가
    else:
        if matrix[row][column] == 0:
            whitePaperCount += 1
        elif matrix[row][column] == 1:
            bluePaperCount += 1
        return

recursion(N, 0,0 )
print(whitePaperCount)
print(bluePaperCount)
