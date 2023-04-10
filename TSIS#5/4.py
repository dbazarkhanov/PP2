f = open('text.txt', 'r')
for i in f.readlines()[-5:]:
    print(i)
f.close()