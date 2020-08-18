class UnderAgeException:
    """This is exception subclass yo validate age  """
    pass

def validate(age):

    #try:
        if (int(age)<18):
            raise ValueError
        else:
            print("you are allowed for voting")

    #except ValueError:
        #print("ValueError: age value should be >=18 ")

    #else:
        #print("age is correct as expected so can continue...")

age= input("Age:")
validate(age)
print(" ")

validate(23)
print(" ")

validate(12)
print(" ")