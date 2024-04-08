num = int(input())
line = 1

while num > line: #1부터 차례로 빼주면서 line 번호 찾기
    num -= line
    line += 1

# 짝수일경우
if line % 2 == 0:
    numerator  = num
    denominator = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    numerator = line - num + 1
    denominator = num

print(f'{numerator}/{denominator}')