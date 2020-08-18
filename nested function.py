def typeOfNum(num):         # outer function
    if num%2==0:
        def message():      # inner function
            print("you entered an even no")
    else:
        def message():      # inner function
            print("you entered an odd no")
    message()

typeOfNum(2)
typeOfNum(3)


def make_multipiersof(n):         # outer function
    def multipliers(x):         # inner function
        return x*n
    return multipliers          # closure- returning a ref to the funct

time_3 = make_multipiersof(3)       # multiplier of 3

time_5 = make_multipiersof(5)       # multiplier of 5

time_9 = make_multipiersof(9)       # multipliers of 9

print(time_3(9))        # output: 27

print(time_5(3))        # output: 15

print(time_9(5))        # output: 45
