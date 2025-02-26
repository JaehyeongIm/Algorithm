N,P,Q = map(int,input().split())
dic = dict()
dic[0] = 1

def infiniteSquence(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = infiniteSquence(n//P) + infiniteSquence(n//Q)
        return dic[n]

print(infiniteSquence(N))