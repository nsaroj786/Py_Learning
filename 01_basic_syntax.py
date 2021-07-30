#!/usr/bin/python
#Run the python script

#Syntax to print in the console: single or double or triple quotations can be used to represent strings
print ('Hell world !')
print ("Hello Google")
print ('"Hello machine !!"')

#Syntax to write identifiers: Name used to identify a variable, function, class, etc. It can use a-z or A-Z in starting followed by underscore(_) or numeric characters(0-9)
var_1=10;
print ("Value of var_1 is: ")
print (var_1)

#Python is case sensitive, so var_1 and Var_1 are 2 different variables
var_1= 100;
Var_1= 200;

print (var_1)
print (Var_1)

#Syntax to write Blocks: Python does not allow braces to indicate blocks of code for class or function definition or loop or conditional statements
#Indentation: Continuous lines indented with same no of spaces are considered as a block 
if True:
	print ("true")
	print ("True")
else:
	print ("False")

if True:
 print ("Lines with same indentation")
 print ("considered as same block")
 
#Syntax for multi_line statements: Python allows to use continuation character (\) to denote the line continues
var_2 = var_1 \
		+ \
		Var_1
print ("The sum is: first line \
		second line")
		
#Syntax for comments: # is used for single line comment, '''   '''' is used for multiline comment lines

#This is a single line comment
'''
This is first line of comment
This is second line of comment
'''

#Syntax for new line: \n is used creating new line
print("\n\nNew line is inserted")

#raw_input is used to keep a terminal open till user gives Enter to exit the terminal
raw_input=("Press the Enter key to exit or terminate. ")

#Multistatement in single line: Use of semicolon alllows to write multiple statements in a single line
var_4=500; var_5= 600; var_6= var_4+var_5; print (var_6)



