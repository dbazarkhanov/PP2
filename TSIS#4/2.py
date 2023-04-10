import re
T = []
a = int(input())
while len(T) < a:
    T.append(input())
b = 0
while b < len(T):
    print(bool(re.search(r'^[+-]?\d*\.\d+$', T[b])))
    b = b + 1