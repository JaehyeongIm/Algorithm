# 배열 만들어 규칙 찾으면서 풀다가 실패

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

stars = [[' '] * 2 * n for _ in range(n)]


def recursion(i, j, size):
    if size == 3:
        # 0행
        stars[i][j] = '*'
        # 1행
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        # 2행
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"

    else:
        newSize = size // 2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)


# n-1은 가운데 좌표
recursion(0, n - 1, n)
for star in stars:
    print("".join(star))
