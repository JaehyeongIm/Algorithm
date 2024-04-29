import sys
input = sys.stdin.read

def find_three_sum_zero():
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]
    scores.sort()
    count = 0

    for i in range(N-2):
        if scores[i] > 0:  # 첫 번째 원소가 0보다 크면 합이 0이 될 수 없으므로 중단
            break
        left, right = i + 1, N - 1
        while left < right:
            three_sum = scores[i] + scores[left] + scores[right]
            if three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            else:
                # 세 수의 합이 0일 경우
                if scores[left] == scores[right]:  # 중복된 수 처리
                    count += (right - left + 1) * (right - left) // 2
                    break
                else:
                    # 중복된 수가 아닐 때는 각 수의 중복 개수 세기
                    l_count = 1
                    r_count = 1
                    while left + 1 < right and scores[left] == scores[left + 1]:
                        l_count += 1
                        left += 1
                    while right - 1 > left and scores[right] == scores[right - 1]:
                        r_count += 1
                        right -= 1
                    count += l_count * r_count
                    left += 1
                    right -= 1

    print(count)

find_three_sum_zero()
