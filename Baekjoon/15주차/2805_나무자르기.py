N, M = list(map(int,input().split()))
treeHeights = list(map(int,input().split()))
# O(n)  n = 백만, n^2 = 1조 , nlogn = 600만, nlogn 이하로 끝내야함
start=1
end = max(treeHeights)

while start<=end:
    mid = (start+end) // 2
    log = 0
    for i in treeHeights:
        if i>=mid:
            log += i -mid

    if log >= M:
        start = mid +1
    else:
        end = mid -1
print(end)
