N = int(input())
str = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n"

recursiveCount = 0


# count = 재귀를 실행할 count, recursiveCount는 실제로 재귀를 반복한 count
def recursive(N, recursiveCount):
    global str
    str += "____" * recursiveCount + "\"재귀함수가 뭔가요?\"\n"

    if N == 0:
        str += "____" * recursiveCount + "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n"
        str += "____" * recursiveCount + "라고 답변하였지.\n"
        return str
    str += "____" * recursiveCount + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n"
    str += "____" * recursiveCount + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n"
    str += "____" * recursiveCount + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n"
    # 입력으로 주어진 재귀 숫자는 줄이고 실제 재귀 Count는 늘려서 재귀 함수 호출
    recursive(N - 1, recursiveCount + 1)
    str += "____" * recursiveCount + "라고 답변하였지.\n"
    return str

print(recursive(N, 0))
