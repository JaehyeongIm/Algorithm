import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input().rstrip())
matrix = []

for i in range(N):
    matrix.append(input().rstrip().split())

zeroCount = 0
minusOneCount = 0
plusOneCount = 0


# 현재 사이즈의 행렬의 matrix에 써진 -1,0,1의 개수를 기록하는 함수
# row,column은 시작점의 행과 열을 나타냄
def paper(size, row, column):
    global zeroCount
    global minusOneCount
    global plusOneCount
    start = matrix[row][column]

    # 1일때는 그냥 리턴
    if size == 1:
        if matrix[row][column] == "0":
            zeroCount += 1
        elif matrix[row][column] == "-1":
            minusOneCount += 1
        elif matrix[row][column] == "1":
            plusOneCount += 1
        return

    # 현재 사이즈의 행렬의 요소가 다른지 같은지 확인
    isDiffrent = False
    for i in range(size):
        for j in range(size):
            if start != matrix[row + i][column + j]:
                isDiffrent = True
                break
        if isDiffrent:
            break
    # 행렬 안의 요소가 다를 떄
    if isDiffrent:
        paper(size // 3, row, column)
        paper(size // 3, row, column + size // 3)
        paper(size // 3, row, column + 2 * size // 3)
        paper(size // 3, row + size // 3, column)
        paper(size // 3, row + size // 3, column + size // 3)
        paper(size // 3, row + size // 3, column + 2 * size // 3)
        paper(size // 3, row + 2 * size // 3, column)
        paper(size // 3, row + 2 * size // 3, column + size // 3)
        paper(size // 3, row + 2 * size // 3, column + 2 * size // 3)
        return
    # 행렬 안의 요소가 전부 같을 떄
    else:
        if matrix[row][column] == "0":
            zeroCount += 1
        elif matrix[row][column] == "-1":
            minusOneCount += 1
        elif matrix[row][column] == "1":
            plusOneCount += 1
        return

paper(N, 0, 0)
print(minusOneCount)
print(zeroCount)
print(plusOneCount)


# 느낀 것 정수 저장할떄 int로 할 건지 string으로 할건지 확실히 하기, string으로 저장하고 integer랑 비교해서 답이 안나왔음.