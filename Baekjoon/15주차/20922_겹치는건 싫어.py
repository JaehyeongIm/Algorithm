N,K = input().split()
numberList = input().split()

left, right = 0,0
counter = [0] * (max(numberList)+1)
answer = 0
while right<              N:
    if counter[numberList[right]] <K:
        counter[numberList]