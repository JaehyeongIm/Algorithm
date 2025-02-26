import sys

sys.setrecursionlimit(1000000)
N = int(input())
numberList = list(map(int, input().split()))
operatorCountList = list(map(int, input().split()))
operatorList = ["+"] * operatorCountList[0] + ["-"] * operatorCountList[1] + ["*"] * operatorCountList[2] + ["/"] * operatorCountList[3]
isUsed = [0] * (N-1) #연산자 수만큼 중복 체크배열 생성
# 값의 범위가  -10억~10억이므로 10억으로 설정
max = -1000000000
min = 1000000000


# 연산자를 바꿔가며 풀어보자.
# 나누기할때 음수를 나눌떄는 양수로 바꾼뒤에 나누고 결과의 부호를 바꾼다. 그렇지 않으면 -5/2 같은 경우 -2이 아니라 -3을 반환한다. 즉 양수의 나눗셈과 값이 다르다.
# 왜냐하면 파이썬은 반올림 방향이 음수를 향해있음
# max,min 절댓값 작게 설정해서 여러번 틀린 문제
def recursion(cur, sum):
    global max, min
    if cur == N - 1:
        if sum > max:
            max = sum
        if sum < min:
            min = sum
        return
    # N-1번 돌아감 (연산자 수만큼)
    # i는 연산자 배열의 인덱스
    # 마지막 재귀일떄 cur은 N-1임 . 그러므로 N-1일때 리턴
    for i in range(N - 1):
        if not isUsed[i]:
            isUsed[i] = 1
            if operatorList[i] == "+":
                recursion(cur + 1, sum + numberList[cur+1])
            elif operatorList[i] == "-":
                recursion(cur + 1, sum - numberList[cur + 1])
            elif operatorList[i] == "*":
                recursion(cur + 1, sum * numberList[cur+1])
            elif operatorList[i] == "/":
                # numberList는 양수가 보장되니 sum의 부호만 고려
                if sum<0:
                    recursion(cur + 1, -(-sum // numberList[cur + 1]))
                else:
                    recursion(cur + 1, sum // numberList[cur + 1])

            isUsed[i] = 0


recursion(0, numberList[0])
print(max)
print(min)
