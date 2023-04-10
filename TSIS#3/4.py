A = [int(i) for i in input().split()]
for i in range(len(A)):
    if A[i] > 0:
        print(A[i], end = ' ')
for i in range(len(A)):
    if A[i] == 0:
        print(A[i], end = ' ')