A = [int(i) for i in input().split()]
for x in range(len(A)):
    if x%2 == 0:
        print(A[x], end = ' ')