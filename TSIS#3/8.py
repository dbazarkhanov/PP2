A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
S1 = set()
S2 = set()
for x in A:
    S1.add(x)
for x in B:
    S2.add(x)
for x in S1.intersection(S2):
    print(x, end = ' ')