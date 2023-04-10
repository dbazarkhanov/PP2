A = [int(i) for i in input().split()]
B = int(input())
if B >= 0:
    for i in range(len(A)):
        if i + B < len(A):
            print(A[i - B], end = ' ')
        elif i + B >= len(A):
            print(A[i - B], end = ' ')
else:
    B = abs(B)
    for i in range(len(A)):
        if i + B < len(A):
            print(A[i + B], end = ' ')
        elif i + B >= len(A):
            print(A[i + B- len(A)], end = ' ')#4 error