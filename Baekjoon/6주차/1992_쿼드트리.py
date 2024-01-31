import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input().rstrip())
matrix = []
for _ in range(N):
    matrix.append(list(input().rstrip()))


# 압축한 결과를 괄호 안에 묶어서 출력하는 함수
def recursive(length, row, column):
    if length == 1:
        if matrix[row][column] == "1":
            print("1", end="")
            return
        elif matrix[row][column] == "0":
            print("0", end="")
            return
        else:
            print("error")
            return

    # 요소가 전부 같은지 다른지 확인, 다르면 반복문 종료
    isDiffrent = False
    for i in range(length):
        for j in range(length):
            if matrix[row][column] != matrix[row + i][column + j]:
                isDiffrent = True
                break
        if isDiffrent:
            break
    # 다르면 괄호 치고 4개로 나눠서 재귀
    if isDiffrent:
        print("(", end="")
        recursive(length // 2, row, column)
        recursive(length // 2, row, column + length // 2)
        recursive(length // 2, row + length // 2, column)
        recursive(length // 2, row + length // 2, column + length // 2)
        print(")", end="")
    # 다 같을떄
    else:
        if matrix[row][column] == "0":
            print("0", end="")
            return
        elif matrix[row][column] == "1":
            print("1", end="")
            return


recursive(N, 0, 0)


# 느낀 점
# 좌표로 접근하면 x좌표가 column과 매칭되어서 헷갈리게 된다. 인덱스 접근할 떄 row와 column으로 접근하자.