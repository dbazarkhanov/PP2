f = open('text.txt', 'r')
txt = f.read()
txt = txt.replace(',', ' ') #but when 'word, word' it makes 3 objects in list, so need if else, i guess
print(len(txt.split(' ')))
f.close()