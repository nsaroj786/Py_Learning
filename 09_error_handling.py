#!usr/bin/python

print ("#### Error Handling ###")
# syntax error: func() but : is missing, name error: name not defined but used
# key error: while trying to access dictionary key beyond defined, 5/0: divisionByZero error

while True:
    try:
        age = input("What's your age ?")
        print(age)
    except NameError:
        print("Please enter a number !")
    else:
        print("Thanks !!")
        break

def sum(num1, num2):
    try:
        return num1+num2
        # 10/0
        #raise Error('Error happened, so stopping the process')
    except TypeError as err:
    # except (TypeError, ZeroDivisionError):
        #print ("Its of non-number" + str(err))
        print(err)
    finally: # atleast this we want to run/display by default
        print("Thanks You !")
print(sum('10',20))

