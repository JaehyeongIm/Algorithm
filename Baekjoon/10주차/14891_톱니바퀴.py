# ✨ 입력
import sys
from collections import deque
input = sys.stdin.readline
t = [deque(list(map(int,input().rstrip()))) for _ in range(4)] # 톱니 상태 저장


k = int(input()) # 회전 횟수
for _ in range(k):
    r = [] # 바퀴 마다 사이드 톱니 상태 저장
    for i in range(4):
        # 6번, 2번 순서
        r.append([t[i][6],t[i][2]])
    n,d = map(int,input().split()) # 회전할 톱니와 방향
    n = n-1 #0인덱싱

    # 현재 i번째 기준 왼쪽에 있는 톱니 돌리기
    # n == 0일때는 왼쪽 x
    if n != 0 :
        for i in range(n,0,-1):
            #현재 톱니바퀴의 6번 위치 톱니와 왼쪽에 있는 톱니바퀴의 2번 위치 톱니의 극이 다른지 검사함
            if r[i][0] != r[i-1][1]:
                if (n-(i-1))%2 == 0: #회전을 시작한 톱니바퀴로부터 몇번째인지 확인( 짝수면 d, 홀수면 -d)
                    t[i-1].rotate(d) #rotate(1) : [1,2,3,4,5] -> [5,1,2,3,4]
                elif (n-(i-1))%2 != 0:
                    t[i-1].rotate(-1*d)
            elif r[i][0] == r[i-1][1]:
                break

    # 현재 i번째 기준 오른쪽 있는 톱니 돌리기
    # n == 3일때는 오른쪽 x

    if n != 3:
        for i in range(n,3):
            if r[i][1] != r[i+1][0]:
                if (n-(i+1))%2 == 0:
                    t[i+1].rotate(d)
                elif (n-(i+1))%2 != 0:
                    t[i+1].rotate(-1*d)
            elif r[i][1] == r[i+1][0]:
                break
    # 본인 톱니 돌리기
    t[n].rotate(d)

# 출력
res = 0
if t[0][0] == 1:
    res+=1
if t[1][0] == 1:
    res+=2
if t[2][0] == 1:
    res+=4
if t[3][0] ==1:
    res+=8
print(res)