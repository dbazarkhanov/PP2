from shutil import copyfile

f = open('text.txt', 'r')
copyfile('text.txt', 'text2.txt')
f.close()