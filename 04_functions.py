'''''''#!usr/bin/python'''

print("### Functions ###")
'''Diif between method and function
	print, len - built in functions
	string.capitalize() : methods      - you can build your own methods also
'''

def sample_func():				#Function defination, wont run without calling it
	print("Sample functions")

sample_func()					#fun defination wont run without calling
print(sample_func)				#memory of func

#Parameters and arguments
def say_hello(name, emoji):			#Parameters: used in defined/called function
	print('hello '+ name +' ' +emoji)

#Positional arguments
say_hello('Saroj', ':)')			#Arguments: used in calling function
say_hello('Rosi', ':(')
#Keyword arguments
say_hello(emoji="::", name='Lovely')

#Default arguments
def say_hello_default(name = 'Sir/Mam',emoji = ':)'):
	print('hello ' + name + ' ' + emoji)
say_hello_default()
#Positional arguments
say_hello_default('Conti','__')
#Keyword arguments
say_hello_default(emoji='__', name = 'Conti')

#Return
print("### Return ###")
def sum1(num1,num2):
	return num1+num2
	print("Hello")	#wont run as return will exit from previous line
print(sum1(4,5))

##Nested FUnction with return
def outer_sum(num1,num2):
	def inner_sum(n1,n2):
		return n1+n2
	return (inner_sum(num1,num2))

#sum = inner_sum(5,7)	#not defined error
sum = outer_sum(5,7)	#calls inner_sum as mentioned in return
print("Sum is: "+ str(sum))

#DocString: In function ''' Info: ___ ''' - print(func.__doc__)-gives info of the function

# *args **kwargs- keyword arguments
# *args : takes any number of positional arguments
'''
def super_func(*args):
	print(args)
	return sum(args)
print(super_func(1,2,3,4,5,6,7,8,9,10))

def super_func(*args, **kwargs):
	print(kwargs)
	return sum(args)+sum(items in kwargs.values())
print(super_func(1,2,3,4,5,6,7,8,9,10, num3=11, num4=12))
'''

#Scope: what variable I have access to
print("### Scope of variable ###")
#global, local-if in a function
x=10			#Global
if True:
	y=20		#Global
def some_func():
	z=30		#Local to this function
print(x)
print(y)
#print(z)		# Error as local scope only

##Scope order- how debugger finds a variable
#1- start with local
#2- parent function local?
#3- GLobal
#4- built in pythonfunctions
a=5
def some_fun1():
	a=10
	return a

print(some_fun1())
print(a) 		#accessing global only a=5, not a=10- its only with in func

##global variable like in C
print("### Global keyword ###")
total =10
def count():
	global total
	total +=1
	return total
print(count())

##Nonlocal keyword
print("#### Nonlocal keyword ###")
'''
def outer():
	x = "local"
	def inner():
		nonlocal x
		x= "non-local"
		print("inner: ",x)
	inner()
	print("outer: ",x)
outer() '''



