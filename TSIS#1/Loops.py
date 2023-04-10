#While loop
i = 1
while i < 6:
  print(i)
  i += 1
#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("---------")

for x in "banana":
  print(x)

print("---------")

for x in range(6):
  print(x)

print("---------")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)