l = map(int, input().split())
evens = []
for i in l:
    if i%2 == 0 and i != 0: evens.append(i)
print(evens)