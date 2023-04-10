A = [int(i) for i in input().split()]
while min(A) and min(A) < 0 or min(A) == 0:
    A.remove(min(A))
if min(A) > 0:
    print(min(A))