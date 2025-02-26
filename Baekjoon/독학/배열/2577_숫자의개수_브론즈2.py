A = int(input())
B = int(input())
C = int(input())
multiple = A*B*C
count= [0] *10

for char in str(multiple):
    count[int(char)]+=1

for i in count:
    print(i)