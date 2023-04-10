A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
S = set(())
for i in A:
    S.add(i)
for i in B:
    S.add(i)
print(len(A) + len(B) - len(S))