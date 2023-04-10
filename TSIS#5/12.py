f = open('text.txt', 'w')
for i in input().split():
    f.write('%s\n' % i)

f = open('text.txt', 'r')
print(f.read())
f.close()