bar_razor = list(input())
answer = 0
st = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        st.append('(')

    else:
        if bar_razor[i-1] == '(':
            st.pop()
            answer += len(st) # 스택에 남아있는 ( 다 더함

        else:
            st.pop() 
            # 해당 )를 스택에서 제거
            answer += 1

print(answer)

