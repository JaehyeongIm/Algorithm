import sys

input=sys.stdin.readline

N = int(input())
inputList= []
for _ in range(N):
    inputList.append(list(map(int,input().split())))

sortedList = sorted(inputList,key=lambda x: (x[1],x[0])) # 오류 : 종료 시간 기준으로 만 정렬할게 아니라 종료시간이 동일할때 시작시간이 빠른 것 순으로 정렬해야함
meeting=[]
meeting.append(sortedList[0])
if N>=2:
    for i in range(1, N):
        if sortedList[i][0] >= meeting[-1][1]: #현재 마지막으로 추가된 회의의 종료시간보다 시작시간이 크거나 같으면 추가한다, 종료시간이 가장 짧은 걸 추가하는게 답이다.
            meeting.append(sortedList[i])
print(len(meeting))
