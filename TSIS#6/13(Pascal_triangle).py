n = int(input())
trow = [1]
y = [0]
for x in range(n):
    print(trow)
    trow=[l+r for l,r in zip(trow+y, y+trow)]