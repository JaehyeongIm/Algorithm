# # 메모리 초과 코드
# N = int(input())
# sequence = []
# for _ in range(N): # N = 200만, 200만 제곱 = 4조 , 200만 로그 200만 = 1천만 ,
# # 시간 복잡도 충분함-> 정렬시키면 됨, 근데 메모리 초과 발생
#     numbers = list(map(int,input().split()))
#     for number in numbers:
#         sequence.append(number)
# sequence.sort()
# print(sequence[-5])


import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
priority_queue = []
for _ in range(N): # N = 200만, 200만 제곱 = 4조 , 200만 로그 200만 = 1천만 ,
    # 시간 복잡도 충분함-> 정렬시키면 됨, 근데 메모리 초과 발생
    numbers = map(int,input().split())
    for number in numbers:
        heapq.heappush(priority_queue, number)
        if len(priority_queue) > N:
            heapq.heappop(priority_queue)
result = heapq.heappop(priority_queue)
print(result)






