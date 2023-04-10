import re
s = input()
k = input()
m = re.search(k, s)
pattern = re.compile(k)
if not m: print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(), m.end()-1))
    m = pattern.search(s, m.start()+1)