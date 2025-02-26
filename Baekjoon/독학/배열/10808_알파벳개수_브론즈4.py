S = list(input())
lowercase_alphabets= [chr(i) for i in range(97,123)]
count = [0] *26
for i in S:
     count[ord(i)-97] +=1
for i in count:
    print(i, end=" ")
