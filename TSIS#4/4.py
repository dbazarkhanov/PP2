import re
digit = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(digit.group(1) if digit else -1)