f = open('text.txt', 'r')
cnt = 0
for i in f:
    cnt += 1
print(cnt)
f.close()