# syntax error
print("hello")  #2nd version 2.7 it will execute if we not put brackets

for i in range(6):
    print(" ",i)


#runtime error
#print(10/0)    # infinite but 0 or1


print(dir(locals()['__builtins__']))

print(2+5/2)

print(1== int('1'))

print(1== '1')


#x=10
try:        # as x is not initialized we put try
    print(x)
except:     # to avoid error we put except to avoid exception
    print("X is not defined, x is yet to be defined")
else:       # this gets executed only when x is initialised
    print("program executed successfully")


try:
    #print(result)
    result=10/0
    print(result)
except ZeroDivisionError:
    print("Pls divide by any non-zero value")
except NameError:
    print("Variable is not defined")
else:
    print("Program executed successfully")



try:
    expertise= ["beginner","proficient","expert"]
    #print(expertise[3])     # index error
    print(expertise.index(3))   #  value error: 3 is not in list

except ValueError:
    print("value is not in the list")



#print(dir(locals()['__builtins__'])) ------->  displays the list of all errors
