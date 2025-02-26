N = int(input())

def fac(m):
    mul = 1
    for i in range(1, m + 1):
        mul = mul * i

    return mul
cnt = 0
number =list(str(fac(N)))
for i in number[::-1]:
    if i != '0':
        break
    else:
        cnt+=1
print(cnt)
