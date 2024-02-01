# import sys
#
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
#
# N = int(input().rstrip())
#
# matrix = [["*"] * N for i in range(N)]
#
#
# def recursion(size, row, column):
#     if size == 3:
#         matrix[row + 1][column + 1] = ""

import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3)
    L = []

    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))