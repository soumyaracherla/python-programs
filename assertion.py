def validate(age):

    try:
        assert (int(age))>=18

    except AssertionError:
        print("ValueError: age value should be >=18 ")

    else:
        print("age is correct as expected so can continue...")

age= input("Age:")
validate(age)
print(" ")

validate(23)
print(" ")

validate(12)
print(" ")