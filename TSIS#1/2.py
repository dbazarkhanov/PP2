#Slicing
b = "Hello, World!"
print(b[2:5])
#With negative
a = "Hello, World!"
print(a[-5:-2])
#Upper and lower
a = "Hello, World!"
print(a.upper())
print(a.lower())
#Strip
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#Replace
a = "Hello, World!"
print(a.replace("H", "J"))
#Split
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Format
"""
age = 36
txt = "My name is John, I am " + age
print(txt) 
is Wrong
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print("-------")

quantity = 3 #index 0
itemno = 567 #index 1
price = 49.95 #index 2
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  
#or with index numbers for example {2} {0} {1}
#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)