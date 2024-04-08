import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

diction = {}  # 리스트 사용했을때 시간초과 발생 -> 딕셔너리 사용
for i in range(len(cards)):
    diction[cards[i]] = 0  # 0으로 초기화

for j in range(M):
    if checks[j] not in diction:
        print(0, end=' ')
    else:
        print(1, end=' ')