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

