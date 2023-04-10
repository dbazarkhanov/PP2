f = open('text.txt', 'r')
arr = []
for i in f:
    arr.append(i)
print(arr)
f.close()