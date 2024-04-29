N, M = list(map(int,input().split()))
treeHeights = list(map(int,input().split()))
#톱날의 높이 설정
start=1
end = max(treeHeights)

#절단기에 설정할 수 있는 높이의 최댓값
while start<=end:
    mid = (start+end) // 2
    treeSum = 0
    # 나뭇가지 길이 합계 더하기
    for treeHeight in treeHeights:
        if treeHeight>=mid: # 크면 자르고 treeSum에 더하기
            treeSum += treeHeight - mid

    if treeSum >= M: # 잘린 나무의 길이가 M보다 크다면 절단기의 높이가 더 높아도 되는지 확인하기 위해 start 조정
        start = mid +1
    else:
        end = mid -1 # # 잘린 나무의 길이가 M보다 작다면 절단기의 높이가 더 낮아야 하므로 end 조정
print(end) # 이진 탐색의 메커니즘 상 end에 최대 톱날 높이가 기록됨. 가능할땐 end 유지, 불가능할땐 end 조정
