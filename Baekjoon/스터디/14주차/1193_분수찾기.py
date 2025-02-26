x = int(input())
line = 1

while x > line: #1부터 차례로 빼주면서 line 번호 찾고 몇번째에 있는지 찾기 (x).
    x -= line
    line += 1   # x=5 1 x= 4 2 , x=2 3

# 각 라인의 요소들은 분모와 분자의 합이 line+1임
# 라인이 짝수이면 분자가 x와 같고 홀수이면 분모가 x와 같음, 여기서 x는 몇번째에 있는지

# 라인이 짝수
if line % 2 == 0:
    numerator  = x
    denominator = line + 1 -x
# 라인이 홀수
elif line % 2 == 1:
    numerator = line + 1 -x
    denominator = x

print(f'{numerator}/{denominator}')