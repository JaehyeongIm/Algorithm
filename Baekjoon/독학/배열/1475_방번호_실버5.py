# nlogn 이하

N = input()
count = [0] *11
total = 0
for i in N:
    if i == "6" or i=="9":
        if count[6]>count[9]:
            count[9]+=1
        else:
            count[6]+=1
    else:
        count[int(i)]+=1

print(max(count))
