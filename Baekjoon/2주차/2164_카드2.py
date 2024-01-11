import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

dQ = deque(range(1,n+1))
count=0
while len(dQ)>1: # n-1 O(n)
    count+=1
    if count%2 == 1:
        dQ.popleft()
    else:
        dQ.append(dQ.popleft())


if len(dQ)==1:
    print(dQ[0])