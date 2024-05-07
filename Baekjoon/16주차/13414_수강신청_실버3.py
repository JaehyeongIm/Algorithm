import sys

input = sys.stdin.readline
K, L = map(int,input().rstrip().split())
studentIDList = dict()
for i in range(L):
    studentId = input().rstrip()
    if studentId in studentIDList: 
        del studentIDList[studentId] #딕셔너리는 삽입한 순서대로 순서를 보장하니 지우고 다시 삽입
        studentIDList[studentId] = i
    else:
        studentIDList[studentId] = i
key = list(studentIDList.keys())
for i in key[:K]:
    print(i)

