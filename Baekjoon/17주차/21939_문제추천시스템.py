import heapq
import sys
from collections import defaultdict
minHeap=[]
maxHeap=[]
N = int(input())
input = sys.stdin.readline
check = defaultdict() # 문제가 실제로 존재하는지 체크하고 문제번호에 대한 가장 최근의 난이도를 저장함.
for i in range(N):
    P,L = list(map(int,input().rstrip().split()))
    heapq.heappush(minHeap,(L,P))
    heapq.heappush(maxHeap,(-L,-P))
    check[P] = L

M = int(input())
for i in range(M):
    inputList= input().rstrip().split()

    if inputList[0] == "recommend":
        if inputList[1] == "1":
            while -maxHeap[0][1] not in check or check[-maxHeap[0][1]] != -maxHeap[0][0]: # check의 저장된 난이도와 maxHeap의 저장된 난이도가 다를때, 즉 난이도가 갱신되었을떄
                heapq.heappop(maxHeap)
            print(-maxHeap[0][1])
        elif inputList[1] == "-1":
            while minHeap[0][1] not in check or check[minHeap[0][1]] != minHeap[0][0]:
                heapq.heappop(minHeap)
            print(minHeap[0][1])

    elif inputList[0] == "add":
        if inputList[1] in check: # 같은 문제번호가 있는 경우
            heapq.heappush(minHeap,(int(inputList[2]),int(inputList[1])))
            heapq.heappush(maxHeap,(-int(inputList[2]),-int(inputList[1])))
            check[inputList[1]] = int(inputList[2]) # 딕셔너리 갱신
        else:
            heapq.heappush(minHeap,(int(inputList[2]),int(inputList[1])))
            heapq.heappush(maxHeap,(-int(inputList[2]),-int(inputList[1])))
            check[int(inputList[1])] = int(inputList[2])
    elif inputList[0] == "solved":
        del check[int(inputList[1])]



# 다빈님 코드
# import sys
# import heapq
# from collections import defaultdict
#
# input = sys.stdin.readline
#
# minQ = []
# maxQ = []
# N = int(input())
# deleted = defaultdict(int)
#
# for i in range(N):
#     P,L = map(int, input().split())
#     heapq.heappush(minQ,(L,P)) #난이도 기준 정렬,번호기준
#     heapq.heappush(maxQ, (-L,-P))
#
#
# M = int(input())
# for i in range(M):
#     line = input().split()
#
#     if line[0] == 'add':
#         L = int(line[2])
#         P = int(line[1])
#         heapq.heappush(minQ,(L,P))
#         heapq.heappush(maxQ,(-L,-P))
#
#
#     # 우선순위큐(최소힙,최대힙)에서 P번 문제 제거
#     elif line[0] == 'solved':
#         deleted[int(line[1])] += 1 #해당 문제번호 삭제처리
#         # print("삭제한 번호 리스트 값",deleted[int(line[1])])
#
#     elif line[0] == 'recommend':
#
#         if int(line[1]) == 1: #난이도 높은 문제
#             # 삭제리스트[문제번호]에서 현 최대큐 우선순위값이
#             # 이미 solved에서 삭제처리 한 애임 => 여기서도 삭제해주자
#             while deleted[abs(maxQ[0][1])] != 0:
#                 #굳이 빼주는 이유는
#                 # -> 또 add (삭제했던)문제번호, 난이도로 들어올 수 있기에
#                 deleted[abs(maxQ[0][1])] -= 1 #0
#                 heapq.heappop(maxQ) #해당 값은 큐에서 정말 삭제
#             print(-maxQ[0][1])
#         else:
#             while deleted[minQ[0][1]] != 0:
#                 deleted[minQ[0][1]] -= 1
#                 heapq.heappop(minQ)
#             print(minQ[0][1])
#
#         # print("minQ",minQ)
#         # print("maxQ",maxQ)