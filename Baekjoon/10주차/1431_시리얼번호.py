# 입력 받기
N = int(input())
serialNumberList = []
for i in range(N):
    serialNumberList.append(input())


# 시리얼 넘버의 모든 자리수 합을 계산하는 함수
def sum_of_digits(serial):
    return sum(int(char) for char in serial if char.isdigit())


# 정렬 조건
# key : 정렬 기준을 정의하는 함수
# 1. 시리얼 번호의 길이가 짧은 것부터
# 2. 길이가 같으면 자리수 합이 작은 것부터
# 3. 그 외에는 사전 순으로
serialNumberList.sort(key=lambda x: (len(x), sum_of_digits(x), x))

# 정렬된 시리얼 번호 출력
for serial in serialNumberList:
    print(serial)
