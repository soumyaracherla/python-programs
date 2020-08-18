
students= {'name': 'ram', 'age': 20,'course': 'web developer'}
print(students)

students['id']= 12345
print(students)     # add new element to the dict

students.popitem()
print(students)     # pop() deletes last item

students.clear()
print(students)    # clear the list and returns the  empty list

students= {'name': 'ram', 'age': 20,'course': 'web developer'}
print(students)
print(students['name'])

print(students.get('name'))

print(students.get('address'))

print('name' in students)   # in is a keyword in python
print('address' not in students)    # not in is also a keyword in python

if 'name' in students:
    print('name is mentioned')
else:
    print('not mentioned')      # if...else stsmt


