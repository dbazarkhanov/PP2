for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(i)
    f = open(i + '.txt', 'w')
    f.write(i)
    f.close()