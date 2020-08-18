class CustomException(Exception):
    pass

class PreceedingLetterException(CustomException):
    pass

class SucceedingLetterEexception(CustomException):
    pass

alphabet='E'

while True:
    try:
        letter=input("enter alphabet:")

        if letter < alphabet:
            raise PreceedingLetterException
        elif letter > alphabet:
            raise SucceedingLetterEexception
            print("wow!!! you guessed it correct")

            break

    except PreceedingLetterException:
        print("you have entered preceeding letter... plz try again")

    except SucceedingLetterEexception:
        print("you have entered succeeding letter... plz try again")

print("wow!!! you guessed it correct")