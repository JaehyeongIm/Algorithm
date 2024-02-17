import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
answer = []

def NandM7(index, N, M):
    if index == M :
        print(' '.join(map(str, answer)))
        return

    for i in range(N):
        answer.append(N_list[i])
        NandM7(index+1, N, M)
        answer.pop()

NandM7(0, N, M)