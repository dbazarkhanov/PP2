n = str(input())
product, sum = 0, 1
for i in range(len(n)):
    product = int(n[i]) * product
    sum = int(n[i]) + sum
print(product - sum)