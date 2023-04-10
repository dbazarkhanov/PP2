import random

f = open('text2.txt', 'r')
print(random.choice(f.readlines()))
f.close()