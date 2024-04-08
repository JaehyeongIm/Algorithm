N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= N and left <= right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)
    # 이렇게 했을떄 시작점으로부터 모든 경우가 다 count됨
    if total == M:
        cnt += 1
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1
print(cnt)
