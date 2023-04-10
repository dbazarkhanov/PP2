s = input().split('-')
s1 = ''
for i in sorted(s):
    s1 = s1 + i + '-'
print(s1.rstrip('-'))

'''
items=[i for i in input().split('-')]
items.sort()
print('-'.join(items))
'''