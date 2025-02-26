import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
T=int(input())

results = []

for _ in range(T):
    k = int(input())
    maxQueue = []
    minQueue = []
    count = defaultdict(int)
    # 28 28 / 1 , 28  / 0     28 - 0
    for _ in range(k):
        char, n = input().split()
        n = int(n)
        if char == "I":
            heapq.heappush(maxQueue, (-n, n))
            heapq.heappush(minQueue, n)
            count[n] += 1
        elif char == "D":
            if n == 1:
                while maxQueue and count[maxQueue[0][1]] == 0:
                    heapq.heappop(maxQueue)
                if maxQueue:
                    value = heapq.heappop(maxQueue)[1]
                    count[value] -= 1
            elif n == -1:
                while minQueue and count[minQueue[0]] == 0:
                    heapq.heappop(minQueue)
                if minQueue:
                    value = heapq.heappop(minQueue)
                    count[value] -= 1
    # 결과 출력을 위한 작업
    while maxQueue and count[maxQueue[0][1]] == 0:
        heapq.heappop(maxQueue)
    while minQueue and count[minQueue[0]] == 0:
        heapq.heappop(minQueue)

    if not maxQueue or not minQueue:
        results.append("EMPTY")
    else:
        results.append(f"{maxQueue[0][1]} {minQueue[0]}")

for result in results:
    print(result)
