#!usr/bin/python

print ("Hello Continental")
print ("This is first python program")

###PYTHON NUMERICS- int, long, float, complex
##Python variables do not need explicit declaration, declaration happens automatically with equal operator
var_int= 10
var_float= 10.0
var_char = "Saroj"

print (var_int)
print var_float
print var_char

##Python allows to assign a single value to multiple variables at a time
a=b=c=100
print ("Value of a is: "), a
print b
print c

##Multiple objects to multiple variables at a time 
x,y,z= 10, 20.30, "Saroj"
print ('First vslur is: '),x
print y
print z

##Delete operation for a variable
#Deleting single variable
del a
del b
#Dleleting multiple variables at a time
del x,y,z
#To check del operation
#print a


###PYTHON STRINGS
print ("\n")
str = "The world is small"
print str
#To print the particular  latter
print str[0]
print str[2]
#To print particular range of the string using :
print str[2:8]
print str[2:]
print str[:8]
#To print same string multiple times using *
print str*3
#To concatenate two strings using +
print str + " It depends on the person how he wants to see the world"

###PYTHON LISTS
#Python list is a compound datatype. It is similar to array but it can hold data of different datatype
list_1 = [10,20,'India', 'Conti', 200.50]
list_2 = [20,50, "Autonomous Driivng"]
print '\n'
print list_1
print list_1[2]
print list_2[1]
list_2[1]= "Future Tech"

##PYTHON TUPLE
#Tuple is similar to list but the syntax uses () instead of [] and it is read only, write operatijon will through synatax error
tuple_1 = (10,50,'abcd', 'ef')
#tuple_1[4]= "gh" throws error as tuple doesnot suppport assignment


"""
###PYTHON Operators
Python language supports the following types of operators.

Arithmetic Operators: 
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators """

##Arithmatic operator
a=2;
b=3;
print "\n"
#To calculate a to the power b
print a**b
#Floor division: 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
print a//b

##Comparision opearator
## ==, !=, <>, <,>,<=, >=,

##Assignment operator
## =, arithmatic= eg: +=, -=, *=

##Bitwise operator
a=60
b=30

print a&b
print a|b
print a^b
print ~a
print a<<2
print a>>2


##Logical operator
#AND 
#OR
#NOT

##Membership operator
#in
#notin

##Identity operator
#is
#is not




print ('\n')
raw_input("This is the last line, press enter to close")
