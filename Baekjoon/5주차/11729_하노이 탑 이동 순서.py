import sys
sys.setrecursionlimit(10 ** 5)

# start에서 end로 n개의 원판을 옮기는 과정을 출력하는 함수
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
    # 장대가 3개이므로 6-start-end가 start와 end를 제외한 나머지 장대가 된다.
    hanoi_tower(n-1, start, 6-start-end) # 1단계 : 나머지 막대에 n-1개의 원판을 옮김
    print(start, end) # 2단계 : 제일 아래 원판을 end에 옮김
    hanoi_tower(n-1, 6-start-end, end) # 3단계 : end에 n-1개의 원판을 옮김

n = int(input())
# 왜 2**n 인지 이해안됨.
print(2**n-1)
hanoi_tower(n, 1, 3)