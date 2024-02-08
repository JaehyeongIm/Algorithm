import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def recursion(idx, count):
    # 6개 다 뽑으면 출력
    if count == 6:
        print(*arr)
        return

    # 현재 수의 다음 수부터 뽑을 수 있게 반복문 처리 => 순서, 중복 제거 (조합)
    for i in range(idx, k):
        arr.append(lottoNumberList[i])
        recursion(i + 1,count+1)
        # 해당 i 에 대한 조합 전부 생성되었으므로 pop
        arr.pop()


while True:
    inputList = list(map(int, input().rstrip().split()))
    k = inputList[0]
    lottoNumberList = inputList[1:]
    if k ==0:
        break
    arr=[]
    # recursion 안에서 출력
    recursion(0,0)
    # 테스트 케이스마다 줄바꿈
    print()





