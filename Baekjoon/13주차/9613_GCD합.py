import sys,math
input = sys.stdin.readline
# 블로그 참고
def gcd(n1,n2): # 유클리드 알고리즘 : a % b = r , a와 b의 최대 공약수는 b와 r의 최대공약수와 같다. 이 과정을 반복하며 나머지가 0이 될 떄의 나누는 수가 a와 b의 최대공약수이다.
    while(True):
        r = n2 % n1
        if r == 0:
            return n1
        n2 = n1; n1 = r

for _ in range(int(input())):
    a = list(map(int,input().split()))
    n,nums,r = a[0],a[1:],0

    for i in range(n-1):
        for j in range(i+1,n):
            r += gcd(nums[i],nums[j])
    print(r)