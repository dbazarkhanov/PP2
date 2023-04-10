def ispangram(s):
    for i in aplphabet:
        if i in s.lower(): continue
        else:
            return False
    return True
aplphabet = 'abcdefghijklmnopqrstuvwxyz'
print(ispangram(input()))