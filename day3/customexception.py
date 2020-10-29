class Error(Exception):
    pass
class InvalidInputTypeError(Error):
    pass
class InvalidNegativeInputError(Error):
    pass

try:
    s=input("enter number: ")
    if ((s>='a' and s<='z') or (s>='A' and s<='Z')):
        raise InvalidInputTypeError
    if (int(s)<0):
        raise InvalidNegativeInputError
    else:
        print("entered is positive number:",int(s))
except InvalidInputTypeError:
    print("invalid type")
except InvalidNegativeInputError:
    print("invalid negative type")


#output: 
#PS C:\Users\ctsvue04\documents\day2> python customexception.py
#enter number: w
#invalid type
#PS C:\Users\ctsvue04\documents\day2> python customexception.py
#enter number: -9
#invalid negative type
#PS C:\Users\ctsvue04\documents\day2> python customexception.py
#enter number: 12
#entered is positive number: 12