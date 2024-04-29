A,B,V = map(int,input().split())

# day : 일 수
# A * day - B (day-1) = V
day = (V-B)/(A-B)

if day == int(day):
    print(int(day))
else:
    print(int(day+1))