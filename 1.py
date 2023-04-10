import re

cardNumbers = [str(input()) for i in range(int(input()))]
for num in cardNumbers:
    if re.search('(\d{4})-(\d{4})-(\d{4})-(\d{4})', num): 
        num = re.sub('-', '', num)
    if not re.search('^[0-9]{16}$', num): print('Invalid')
    elif not re.search('\A[456]', num): print('Invalid')
    elif re.search(r'(\d)\1\1\1', num): print('Invalid')
    else: print('Valid')