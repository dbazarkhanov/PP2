f = open('text2.txt', 'w')
l = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
n = int(input())
for i in range(0, len(l), n):
    f.writelines(list(l[i:i+n] + ['\n']))
f.close()