f = open('text.txt', 'a')
f.write('HELLO')

f = open('text.txt', 'r')
print(f.read())
f.close()