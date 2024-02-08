
import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
#depth : 현재까지 선택한 숫자의 개수
def dfs(depth, i):
    if depth == 6:
        # *를 붙이면 내부 리스트의 요소들이 별도로 출력됨
        print(*output)
        return

    for i in range(i, count):
        if depth + count - i < 6: # 정답 배열에 넣으려는 인덱스를 더했을 경우 남은 요소들을 다 채워도 최종 길이를 만족하지 못한다면
            return
        output.append(LottoNumberList[i]) # 최종 길이를 만족할 수 있을 경우만 append
        dfs(depth + 1, i + 1) # 재귀
        output.pop() # 다음 요소 탐색을 위해 pop

while True:
    inputList = list(map(int, input().split()))
    count = inputList[0]
    LottoNumberList = inputList[1:]
    if count == 0:
        break
    output = []
    dfs(0, 0)
    print()


