#!usr/bin/python
##Data types in Python
##Fundamental data types
	#int, float, bool, str, list, tuple, set, dictionary
#int
print(type(2+4))
print(2-4)
print(2*4)
print(type(2/4)) # int in 2.7 but float in python 3.x

#float
print(type(0))
print(type(0.0))
print(type(20+0.0))
#print(size(0))
#print(size(0.0))

#Operator presedance -> (), ** or power, /*, +-

#Boolean
#1->True, 0-> False

#string
print(type("Hello world"))
usr_name = 'Saroj'
psw = 'xyz'
long_string = '''
WOW
Nice
'''
print(long_string)

first_name = 'Saroj'
last_name=  'Kumar'
full_name = first_name + ' ' + last_name
print(full_name)
print(first_name + ' ' + last_name)
#print("your full name is {first_name} {last_name}") #f -> formatted string Feature of python 3.x

#String indexing -> [start:stop:step-over]
selfish = "me me me"
print(selfish[0:5])
print(selfish[0:5:2])
print(selfish[::2])

numbers = "123456789"
print(numbers[-1])
print(numbers[::-1]) #reverses the string

#String immutability
#numbers[0] = 2 #does not support in python, complete str have to be reassigned
numbers = "223456789"

print(len(numbers)) # built in function format -> function_name()
                    # length of thr string, starts from 1 not from 0
                    #String methods format -> string.function()
print(selfish.upper())  #Converts full string to capital
print(selfish.capitalize())
print(selfish.find("Me"))


#List
list1 = [1,2,3,4,5]
list2 = ["a","b","c"]
list3 = [1,"a",bool(0),5.5,20,15]
print (type(list3[2]))

#List slicing
print(list3[0:5:1]) #startindex:stopindex:interval
#Assignment
list3[2] = bool(1)
print(list3)

#Matrix
matrix  = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(type(matrix))  #multi-dimensoinal matrix
print(len(matrix))   #length-3, again each element is a list of size 3
matrix.append(100)  #100-integer, [100]-list
print(matrix)
matrix.insert(2,[10,11,12]) #index,data
print(matrix)
matrix.pop()
print(matrix)   #default removes last element
matrix.pop(2)   #removes the item of mentioned index
print(matrix)

#Dictionary
print("Dictionary")
Employee = {
	'id':1,				#'key':value
	'name':"Saroj",
	'sal':[50,7,3]
}
print(Employee)
print(Employee['name'])
print(Employee['sal'][1])
print(Employee.get('age'))		#when there is no data but should not give error
print(Employee.get('age',25))	#when no data, set the value as key_value 
#dictionary methods
print('name' in Employee)

#Tuples: immutable list, can not change the value, can access like list
print("###Tuple###")
my_tuple = (1,2,3,4,5)
print(my_tuple[1])


#SET
print("###SET###")
my_set = {1,2,3,4,5}
print(my_set)
my_set = {1,2,3,4,5,5,5}
print(my_set)				#takes only one time any item
my_set.add(6)
my_set.add(2)
print(my_set)
#print(my_set[1])		#Set doesnot support indexing
print(list(my_set)[2])	#convert to list, and access through indexing
#Set operation
#differnce, intersection, update, etc


##Classes -> custom types
	#SuperCar
	
##Specialized data types-> Modules,
