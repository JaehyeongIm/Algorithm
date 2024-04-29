N = int(input())
solutionList = list(map(int,input().split()))
solutionList.sort()

left = 0
right = N-1
best_sum = float('inf')  # 최적의 합을 찾기 위해 무한대로 초기화
best_pair = (0,0)

while left<right:
    current_sum = solutionList[left] + solutionList[right]

    if abs(current_sum) <= abs(best_sum): # 예시 출력을 봤을때 새로 갱신된 것을 요구하기에 = 추가
        best_sum = current_sum
        best_pair = (solutionList[left],solutionList[right])

    if current_sum <0:
        left +=1
    elif current_sum > 0:
        right -=1
    else:
        break
print(best_pair[0],best_pair[1])