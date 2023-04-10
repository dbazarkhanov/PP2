m = [-5, 1, 5, 0, -7]
f = [0]
for i in range(len(m)):
    f.append(f[i] + m[i])
print(max(f))