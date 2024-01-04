from collections import deque

count_2 = 0
count_3 = 0
N, M = map(int, input().split())
numberList = deque(map(int, input().split()))
dQ = deque(range(1, N + 1))
# 찾는 숫자의 인덱스가 n/2  보다 작으면 2번연산, 크거나 같으면 3번연산 / greedy한 접근이 맞음. 왜냐면 오른쪽으로 빼든 왼쪽으로 빼든 결과 배열이 똑같음.
for number in numberList:
    if list(dQ).index(number) <= len(dQ) / 2 :
        while True:
            if dQ[0] == number:
                dQ.popleft()
                break
            else:
                dQ.append(dQ.popleft())
                count_2 += 1
    elif list(dQ).index(number) > len(dQ) / 2 :
        while True:
            if dQ[0] == number:
                dQ.popleft()
                break
            else:
                dQ.appendleft(dQ.pop())
                count_3 += 1
    else:
        print("error")
print(count_2 + count_3)

# 10 10
# 1 6 3 2 7 9 8 4 10 5

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 당장의 선택에 충실하면 됨 greedy