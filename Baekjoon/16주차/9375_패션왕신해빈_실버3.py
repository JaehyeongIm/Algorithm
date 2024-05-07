from collections import defaultdict
testCount = int(input())
outputs=[]
for _ in range(testCount):
    n = int(input())
    clothes = []
    output = 1
    clothesType =defaultdict(int)
    for i in range(n):
        clothes.append(input().split())
        clothesType[clothes[i][1]]+=1 # 특정 타입에 대한 옷 개수 측정
    values = list(clothesType.values())

    for i in range(len(values)):
        output *= (values[i]+1) # 각 옷종류마다 안입는 선택지 있으니 1 추가
    outputs.append(output-1) # 알몸인 경우 한 가지 빼서 출력값 넣어주기
for i in outputs: # 결과 출력
    print(i)

