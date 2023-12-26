N,K = map(int, input().split())
arr = list(range(1,N+1))

list = []
number = 0

for i in range(N):
    number += K-1
    if number >= len(arr):
        number = number % len(arr)

    list.append(str(arr.pop(number)))
print("<",", ".join(list),">",sep='')


