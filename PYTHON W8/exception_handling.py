# try and except are used for exception handling , when you add the exception for the nameError it reads for the variable.
# try:
#     print(x)
# except NameError:
#     print( "variable x is not defined")
    
# except:
#     print("an exception occurred")
    
    # finally block is an optional block ,the code is excuted regardless if the exception has been made or not.

try:
    print(x)
except NameError:
    print("Variable x is not defined")
    x = -1  # Set x to a default value if it wasn't defined

if x < 0:
    raise Exception("Sorry, no numbers below zero")
    