fruits=['mango', 'apple', 'banana']
print(fruits)
print(fruits[2])
print(fruits[-2]) # list

print(fruits.index("apple"))

fruits.append('grapes')
print(fruits)   # append operation

vegetables=['onion', 'carrot', 'beetroot', 'tomato']
fruits.extend(vegetables)
print(fruits)   # extend operation

fruits.insert(2,'pineapple')
print(fruits)   # insert operation

vegetables.remove('carrot')
print(vegetables)   # remove operation

vegetables.pop(1)
print(vegetables)   # pop operation

vowels=['a', 'e', 'i', 'o', 'u']
print(vowels)

print(vowels[ :3])
print(vowels[2:])

print(vowels.count('a'))    #count operation

fruits.sort()
print(fruits)   # sort method
