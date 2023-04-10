f = open('text.txt', 'r')
print([i.strip('\n') for i in f.readlines()])
f.close()