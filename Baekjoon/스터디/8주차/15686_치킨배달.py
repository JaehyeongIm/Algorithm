import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 각 치킨집의 치킨거리 구하기
# 오름차순 정렬 후 M개까지 선택 itertool.combinations
# 나머지 폐업
ch = []
home = []
for i, pan_ in enumerate(pan):
    for j, value in enumerate(pan_):
        if value == 2:
            ch.append((i,j))
        if value == 1:
            home.append((i,j))
ch_distance = [[] for i in range(len(home))]
min_city_distance = float('inf') # 도시의 치킨 거리 저장할 변수
for chs in combinations(ch,M): # M개의 치킨집 조합으로 선택
    city_distance = 0 # 현재 선택한 M개의 치킨집으로 도시의 치킨 거리를 저장할 변수
    for i, value_home in enumerate(home): # 집들의 좌표
        min_distance = float('inf') # 가장 적은 치킨거리를 저장할 변수 선택
        for j, value_ch in enumerate(chs): # 치킨집의 좌표
            distance = abs(value_home[0]-value_ch[0]) + abs(value_home[1]-value_ch[1]) # 치킨집과 집의 거리
            if min_distance>distance: # 치킨집과 집의 가장 최소 거리 선택
                min_distance = distance
        city_distance += min_distance # 최소거리를 도시의 치킨 거리에 합함
    if min_city_distance>city_distance: # M개를 선택할 때마다 가장 작은 도시 치킨 거리를 저장함
        min_city_distance=city_distance

print(min_city_distance) #출력