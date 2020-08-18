age = 2
if age >= 18:
    print('user is allowed for voting')    # if condition

mark=60
if mark>=65:
    print('awarded class1')
else:
    print('awarded class2 ')    # if...else condition

x=100
if x==200:
    print('correct')
    print(x)
elif x==150:
    print('correct')
    print(x)
elif x==100:
    print('correct')
    print(x)
else:
    print('wrong')      # elif condition



nationality= 'indian'
age= int(input('enter age'))    # converts str to int int(imput(enter
if nationality== 'indian':
    if age>=18:
        print('valid voter')
    else:
        print('age is invalid')
else:
    print('oops!! voting is allowed only for indians')      # nested if condition


