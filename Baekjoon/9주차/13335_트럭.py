from collections import deque

n, w, l = map(int, input().split())
truckList = deque(list(map(int, input().split())))

bridge = deque([0] * w)
time = 0
weightSum = 0
while bridge:
    time += 1
    # 다리 가장 앞쪽 pop하고 무게 합에서 빼기
    weightSum -= bridge.popleft()
    # 트럭이 남아있으면
    if truckList:
        if (truckList[0] + weightSum) <= l:
            truck = truckList.popleft()
            bridge.append(truck)
            weightSum += truck
        else:
            # 트럭이 있는데 못타는 경우는 0을 채우고 트럭이 없으면 0 안 채워서 다리가 끊김
            bridge.append(0)
print(time)
