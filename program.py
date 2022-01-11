name="resul G"
print(name)
print(type(name))
type(name) == str 
isinstance(name, str)
print(name.lower())


condition = True
if condition == True:
    print("The condition")
    print("was true")
else:
    print("The condition")
    print("was false")    

items = ["Roger", "xx", "Syd","yyy"]
print(items)

items.append("resul")

print(items)

items.extend(["beril","özlem"])

print(items)

#items.sort(key=str.lower)

print(sorted(items, key=str.lower))
print(items)

#tuple
tuples = ("Roger", "xx", "Syd","yyy")
print(tuples)

#dictionary
dog = { 'name': 'Roger', 'age': 8 }
print(dog)

print(dog['name'])
print(dog.get('name','default'))
print(dog.get('name1','default'))

#print(dog.pop('name'))
print(dog)

if 'age' in dog:
    print("age field exists in dog dictionary")

print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))

del dog['age']

print(dog)

def hello(name='my friend'):
    print('hello ' + name)

hello("resul")
hello()

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(4):
    print(item)

items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)



from lib import dog

tony = dog.Dog('tony',1)

tony.bark()
tony.walk()

import math
print(math.sqrt(4)) # 2.0

from math import sqrt
print(sqrt(4)) # 2.0