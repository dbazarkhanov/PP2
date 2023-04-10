from collections import Counter

f = open('text.txt', 'r')
print(Counter(f.read().split()))
f.close()