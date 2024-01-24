import sys

sys.setrecursionlimit(10 ** 5)
N, r, c = map(int, input().split())

# 2^N, 2^n인 2차원 배열의 r행 c열 까지 가는 최단거리 출력 (z방식)
def sol(N, r, c):
    if N == 0:
        return 0
# 2 * (r % 2) + (c % 2)는 네모칸 안에서 이동할 수 있는 범위

    return 2 * (r % 2) + (c % 2) + 4 * sol(N - 1, int(r / 2), int(c / 2))


print(sol(N, r, c))

# 좌표 r,c가 2배가 됨에 따라 값이 4의 배수로 확장
