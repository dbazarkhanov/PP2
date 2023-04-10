def func(l):
    l.sort()
    print(len(l))
    for i in l:
        print(i, end=' ')
    print()
A, B = [int(i) for i in input().split()]
SA = set()
SB = set()
for i in range(A):
    SA.add(int(input()))
for i in range(B):
    SB.add(int(input()))
func(list(SA.intersection(SB)))
func(list(SA.difference(SB)))
func(list(SB.difference(SA)))