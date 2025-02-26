import sys

sys.setrecursionlimit(100000000)
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())


def recursion(number, square, mod):
    # base condition

    if square == 1:
        return number % mod
    # 나머지에 관한 성질 이용 ex. 2^10 % 3 => (2^5 % 3) * (2^5 % 3) % 3
    result = recursion(number, square // 2, mod)
    result = result * result % mod
    # 짝수면 그대로 출력 (square가 k일때 성립하면 2k, 2k+1 도 성립함 -> 귀납적 사고)
    if square % 2 == 0:
        return result
    else:
        return result * number % mod


print(recursion(A, B, C))
