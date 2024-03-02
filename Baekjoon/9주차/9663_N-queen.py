
N = int(input())
cnt=0
leftDiagonal=[0] * 1000000
straight=[0] * 1000000
rightDiagonal=[0]* 1000000


# (row,col)에 둘수 있는지 확인하는 함수
# row와 col은 0인덱싱
def recursion(row):
    global cnt

    if row == N:
        cnt+=1
        return
    for col in range(N):
        # 퀸 이동 반경에 걸리면 contiunue
        if leftDiagonal[row+col] or straight[col] or rightDiagonal[row-col+N-1]:
            continue
        straight[col]=1
        leftDiagonal[row+col]=1
        rightDiagonal[row-col+N-1] = 1
        recursion(row+1)
        straight[col]=0
        leftDiagonal[row+col]=0
        rightDiagonal[row-col+N-1] = 0

        # row+col
        # row-col


recursion(0)
print(cnt)


