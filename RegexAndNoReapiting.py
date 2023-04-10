import re

UID = [input() for c in range(int(input()))]
for c in UID:
    if len(c) != 10: print('Invalid')
    elif len(re.findall('\d', c)) < 3 or len(re.findall('[A-Z]', c)) < 2: print('Invalid')
    elif re.search(r'(.).*\1', c) != None: print('Invalid')
    elif re.search('[a-zA-Z0-9]{10}', c) == None: print('Invalid')
    else: print('Valid')
    
    # vvv without RegEx vvv
'''
l = [input() for i in range(int(input()))]
uppers, digits, all_digits = 2, 3, '1234567890'
for i in l:
    cont = False
    cntDig = cntUpp = 0
    for j in range(len(i)):
        if i[j] in all_digits: cntDig += 1
        if i[j].isupper() == True: cntUpp += 1
        if cont == False:
            for k in range(len(i)):
                if i[j] == i[k] and j < k:
                    cont = True
                    print('Invalid')
                    break
    if cont == True: continue
    elif len(i) != 10 or cntDig < digits or cntUpp < uppers: print('Invalid')
    else: print('Valid')
'''