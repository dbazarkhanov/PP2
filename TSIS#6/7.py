s = input()
cntU = cntL = 0
for i in s:
    if i.isupper(): cntU += 1
    elif i.islower(): cntL += 1
print('Number of Upper case characters: ' + str(cntU))
print('Number of Lower case characters: ' + str(cntL))