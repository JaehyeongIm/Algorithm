# import sys
# from collections import deque
#
# N = int(input())
# wordCount = 0  # 좋은 단어 개수
#
# for _ in range(N):
#
#     str = list(sys.stdin.readline().rstrip())
#     dQ = deque(str)
#     result = True
#     # 첫 문자와 마지막 문자가 같을때 다를 때로 구분
#     # 같을 때는 대칭, 다를 때는 AAAABBBB 이런식으로 진행
#     # 같을 때
#     if dQ[0] == dQ[-1]:
#
#         while len(dQ) >= 2:
#             # 같을 때는 앞 뒤로 뺀게 서로 같아야함, 다르면 result로 false 리턴
#             if dQ.popleft() != dQ.pop():
#                 result = False
#                 break
#     #다를 때
#     else:
#         if len(dQ) < 4:
#             result =  False
#         else:
#             first = dQ[0]
#             last = dQ[-1]
#             while len(dQ) >= 2:
#
#                 # 다를 때는 앞 뒤로 뺀게 처음에 뺀 것과 같아야함, 다르면 result로 false 리턴
#                 if first != dQ.popleft() or last != dQ.pop():
#                     result = False
#                     break
#
#     #1이 되었다는 것은 홀수라는 뜻, 홀수는 짝지어질수 없음
#     if len(dQ) != 1 and result:
#         wordCount += 1
# print(wordCount)

import sys
from collections import deque

N = int(input())
wordCount = 0  # 좋은 단어 개수

for _ in range(N):

    str = list(sys.stdin.readline().rstrip())
    dQ = deque(str)
    result = True
    # 첫 문자와 마지막 문자가 같을때 다를 때로 구분
    # 같을 때는 대칭, 다를 때는 AAAABBBB 이런식으로 진행
    # 같을 때
    if dQ[0] == dQ[-1]:

        while len(dQ) >= 2:
            # 같을 때는 앞 뒤로 뺀게 서로 같아야함, 다르면 result로 false 리턴
            if dQ.popleft() != dQ.pop():
                result = False
                break
    #다를 때
    else:
        if len(dQ) < 4:
            result =  False
        else:
            first = dQ[0]
            last = dQ[-1]
            while len(dQ) >= 2:

                # 다를 때는 앞 뒤로 뺀게 처음에 뺀 것과 같아야함, 다르면 result로 false 리턴
                if first != dQ.popleft() or last != dQ.pop():
                    result = False
                    break

    #1이 되었다는 것은 홀수라는 뜻, 홀수는 짝지어질수 없음
    if len(dQ) != 1 and result:
        wordCount += 1
print(wordCount)
