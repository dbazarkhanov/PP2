s = input()
bold = '\033[1m' + s + '\033[0m'
italic = '\033[3m' + s + '\033[0m'
underline = '\033[4m' + s + '\033[0m'
print(bold, italic, underline, sep=' ')