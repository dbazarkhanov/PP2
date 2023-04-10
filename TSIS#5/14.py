f, f1 = open('text.txt', 'r'), open('text2.txt', 'r')
for i, j in zip(f, f1):
    print(i + j)
f.close(), f1.close()