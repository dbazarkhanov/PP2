f = open('text.txt', 'r')
txt = f.read()
print(sorted(txt.split(), key=len, reverse=True)[0])
f.close()