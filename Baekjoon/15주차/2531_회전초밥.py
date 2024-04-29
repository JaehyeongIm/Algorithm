#GPT 참고
from collections import defaultdict

N,d,k,c= map(int,input().split())
sushiList = [int(input()) for i in range(N)]
sushi_count = defaultdict(int) # 자동초기화 dict
maxSushi = 0
sushi_count[c] +=1 # 쿠폰 초밥은 하나 더 먹을 수 있음

# 초기 설정
for i in range(k):
    sushi_count[sushiList[i]] += 1

for start in range(N):
    currenctSushi = len(sushi_count) # 현재 초밥 가지수 (0이 아닌 갑슫ㄹ의 개수)
    maxSushi = max(maxSushi,currenctSushi) # 초밥가지 수 최대값 갱신
    
    
    first_sushi = sushiList[start] #제일 앞 초밥 삭제
    sushi_count[first_sushi] -=1
    if sushi_count[first_sushi] ==0:
        del sushi_count[first_sushi] ## 딕셔너리에서 삭제
    # 다음 초밥 선정
    next_sushi = sushiList[(start+k)%N] # N 초과시 한바퀴 도는 효과
    sushi_count[next_sushi] += 1
print(maxSushi)


