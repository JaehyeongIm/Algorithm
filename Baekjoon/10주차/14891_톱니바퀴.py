# ✨ 입력
import sys
from collections import deque
input = sys.stdin.readline
wheel = [deque(list(map(int,input().rstrip()))) for _ in range(4)] # 톱니 상태 deque 4개 로 저장


k = int(input()) # 회전 횟수
for _ in range(k):
    side = [] # 바퀴 마다 사이드 톱니 상태 저장
    for i in range(4):
        # 6번, 2번 톱니저장
        side.append([wheel[i][6],wheel[i][2]])
    n,d = map(int,input().split()) # 회전할 톱니와 방향
    n = n-1  #0 인덱싱

    # 톱니 돌리기
    wheel[n].rotate(d)
    # 현재 n번째 톱니바퀴의 왼쪽에 있는 톱니 돌리기
    # n == 0일때는 왼쪽 x
    if n != 0 :
        for i in range(n,0,-1):
            # i를 기준으로 잡고 왼쪽 i-1번째를 돌릴지 말지 조건체크
            # 현재 i번째 기준으로 톱니바퀴의 6번 위치 톱니와 왼쪽에 있는 톱니바퀴의 2번 위치 톱니의 극이 다른지 검사함
            if side[i][0] != side[i-1][1]: #극이다르면 회전
                if (n-(i-1))%2 == 0: #회전을 시작한 n번째 톱니바퀴로부터 몇번째인지 확인( 짝수면 d, 홀수면 -d)
                    wheel[i-1].rotate(d) #rotate(1) : [1,2,3,4,5] -> [5,1,2,3,4]
                elif (n-(i-1))%2 != 0:
                    wheel[i-1].rotate(-1*d)
            elif side[i][0] == side[i-1][1]:
                break

    # 현재 i번째 기준 오른쪽 있는 톱니 돌리기
    # n == 3일때는 오른쪽 x
    if n != 3:
        # i를 기준으로 잡고 오른쪽 i+1번째를 돌릴지 말지 조건체크
        # 현재 i번째 기준으로 톱니바퀴의 2번 위치 톱니와 왼쪽에 있는 톱니바퀴의 6번 위치 톱니의 극이 다른지 검사함
        for i in range(n,3):
            if side[i][1] != side[i+1][0]: # 극이 다를 때
                if (n-(i+1))%2 == 0:
                    wheel[i+1].rotate(d)
                elif (n-(i+1))%2 != 0:
                    wheel[i+1].rotate(-1*d)
            elif side[i][1] == side[i+1][0]: # 극이 같을 때
                break


# 출력
res = 0
if wheel[0][0] == 1:
    res+=1
if wheel[1][0] == 1:
    res+=2
if wheel[2][0] == 1:
    res+=4
if wheel[3][0] == 1:
    res+=8
print(res)