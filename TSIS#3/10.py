n = int(input())
D = dict([input().split() for x in range(n)])
key = input()
for k, v in D.items():
    if key == k:
        print(v)
    elif key == v:
        print(k) 