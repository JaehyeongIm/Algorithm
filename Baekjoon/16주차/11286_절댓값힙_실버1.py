import heapq
import sys

input = sys.stdin.readline
N = int(input().rstrip())
priority_queue = []
for i in range(N):
    x = int(input().rstrip())
    if x != 0 :
        heapq.heappush(priority_queue, (abs(x),x))
    else:
        if len(priority_queue) == 0 :
            print(0)
        else:
            priority, data = heapq.heappop(priority_queue)
            print(data)

