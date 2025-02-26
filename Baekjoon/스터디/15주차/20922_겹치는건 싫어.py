from collections import defaultdict

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 0

count = defaultdict(int)
result = 0
while right < N:
    if count[numbers[right]] < K:
        count[numbers[right]] += 1
        right += 1
    else:
        count[numbers[left]] -= 1
        left += 1
    result = max(result, right - left)
print(result)