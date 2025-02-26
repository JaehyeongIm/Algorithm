# 블로그 참고 코드
import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, input().rstrip().split()))) # 보석의 무게로 최소힙 구성
bags = []
for _ in range(K):
    bags.append(int(input().rstrip()))
bags.sort() # 가방의 최대용량을 오름차순으로 정렬
# 각 가방에 담을 수 있는 최대 가치의 보석을 담되 용량이 작은 가방부터 보석을 담는다.
# 가방의 순서를 신경쓰지 않고 보석을 담는다면 보석을 담지 못하는 경우가 생긴다.
answer = 0
tmp_jew = [] # 가능한 가장 가치있는 보석을 찾는 최대힙
for bag in bags:
    while jew and bag >= jew[0][0]: # 가방보다 작거나 같은 무게의 보석들을 가치가 큰순으로 넣음
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew) #가치가 -로 저장되서 -=를 하면 가치가 더해짐
    elif not jew:
        break
print(answer)

# N, K = input().split()
# jewels=[]
# for _ in range(N):
#     jewels.append(input().split())
    