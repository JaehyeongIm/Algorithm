import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
T = int(input().rstrip())
MaxQueue=[]
MinQueue=[]
count = defaultdict(int)
for _ in range(T):
    k = input().rstrip()
    for _ in range(k):
        char, n = input().rstrip().split()
        if char == "D":
            if n == "1" :
                maxValue = heapq.heappop(MaxQueue)
                count[maxValue] -=1
            elif n == "-1" :
                minValue = heapq.heappop(MinQueue)
                count[minValue] -=1

        elif char == "I":
            if n>=0:


            else:
            heapq.heappush(MaxQueue,(-n, n))
            heapq.heappush(MinQueue,(n, n))  #




