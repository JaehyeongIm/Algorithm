# N = int(input())
# dogList = list(map(int, input().split()))
# fiftyflag = False
# fiftyOverFlag = False
# fiftydownFlag = False
# count = 0
# for i in dogList:
#     if i == 50:
#         fiftyflag = True
#     if i >= 50:
#         fiftyOverFlag = True
#
# if fiftyflag:
#     count = 1
# elif len(dogList)==1 or fiftyOverFlag:
#     count = 0
# else:
#     arrayLength = len(dogList)
#     isUsed = [False] * arrayLength
#     for i in range(arrayLength):
#         if isUsed[i] == False:
#             for j in range(i + 1, arrayLength):
#                 if isUsed[j] ==False:
#                     if dogList[i] == dogList[j]:
#
#                         isUsed[i] = True
#                         isUsed[j] = True
#                         count += 1
#                         break
# print(count)
# 깃허브 체그용
