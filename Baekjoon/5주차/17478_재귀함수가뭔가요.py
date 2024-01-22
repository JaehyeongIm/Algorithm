N =input()
str=""
def recursive(count):
    if count == 0:
        str+="재귀함수는 자기 자신을 호출하는 함수라네"
        return str
    str