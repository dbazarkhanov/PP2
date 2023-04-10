import re
s = input()
a = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm +-])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm +-])', s, re.I)
if a == []: print(-1)
else: print(*[i for i in a], sep='\n')  