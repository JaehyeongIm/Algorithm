import heapq
import sys

input = sys.stdin.readline
N = int(input().rstrip())
priority_queue = []
for i in range(N):
    x = int(input().rstrip())
    if x == 0:
        if len(priority_queue)==0:
            print(0)
        else:
            print(heapq.heappop(priority_queue))
    else:
        heapq.heappush(priority_queue,x)
