A,B = map(int, input().split())

Aset = set(map(int, input().split()))
Bset = set(map(int, input().split()))

print(len(Aset - Bset))
print(*sorted(list(Aset - Bset)))  # Set에서 A-B를 지원함.