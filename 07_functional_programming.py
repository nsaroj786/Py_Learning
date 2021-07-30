#!usr/bin/python
#Functional programming: classify into functions and variables
print ("###Functional Programming###")

#Pure function: 1) should give same output for the same input 2)No side effect or dependency on outside the world/ outside function things
#Useful for avoiding bugs in code, no dependency on outside variables
def multiply_by2(li): # 1) gives same o/p for same i/p 2) no outside variables are used which can be changed outside the function
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

#map, filter, zip and reduce used to make pure functions
print("### Map ###") #helps to connect individual pure function and variable
my_list= [10,11,12]
def multiply_by3(item):
    return item*3

print(map(multiply_by3,[5,6,7]))
print(map(multiply_by3,my_list))
print(my_list)                      #does not change the outside variable value, so pure function

print("### Filter ###") #helps in filtering boolean value
def only_odd(item):
    return (item % 2) != 0

print(filter(only_odd,my_list))
print(my_list)                      #does not change the outside variable value

print("### zip ###")    #combines two lists
first_list = [10,12,14]
second_list = [11,13,15]
print(zip(first_list,second_list))
name_list = ['Saroj', 'Rosi', 'Other']
ph_no_list = ['8763893389', '9040993389', '9876543121']
print(zip(name_list,ph_no_list))

print("### reduce ###")
#does not come by default
from functools import reduce
def accumulator(acc, item):
    print(acc, item)
    return  acc+item

print(reduce(accumulator, my_list, 0))



# Lambda expression: is an expression can be used only once, used to replace function which is ud=sed only once
print("### Lambda expression ###")
print(list(map(lambda item:item*2, my_list)))
print(list(filter(lambda item: item % 2 ==0, my_list)))

#Lambda practice eg: convert powered list
my_list1 = [5,4,3]
powered_list = list(map(lambda item: item**2 , my_list1))
print(powered_list)
#List sorting: based on second element of each tuple
a=[(0,2),(4,3),(9,9),(10,-1)]
a.sort()    # based on first key
a.sort(key= lambda x:x[1])
print(a)


### List comprehension: list, set, dict
#General method
my_list2 = []
for char in 'hello':
    my_list2.append(char)
print(my_list2)

#Comprehension method
# list = [param for param in iterable]
my_list2 = [item for item in 'hello']
print(my_list2)
#number from 0 to 100: only list
my_list3 = [num for num in range(0,100)]
print(my_list3)
#power 2 of number from 0 to 100: list with operation
my_list3 = [num**2 for num in range(0,100)]
print(my_list3)
#power 2 of number from 0 to 100, but only if it is even
my_list3 = [num**2 for num in range(0,100) if num %2 == 0]  #list comprehenssion
print(my_list3)

#Set comprehension: change only bracket
my_set = {num for num in range(0,100)}

#Dict comprehension
simple_dict = {
    'a':1,
    'b':2
}
my_dict = {k:v**2 for k,v in  simple_dict.items()}
print(my_dict)
my_dict2 = {key: value **2 for key, value in simple_dict.items() if value %2 == 0}
print(my_dict2)

#find duplicates
some_list = ['a','b','a', 'c', 'd','e','e','f']
duplicates = [x for x in some_list if (some_list.count(x)>1 )]
print(duplicates)
duplicate = list(set([x for x in some_list if (some_list.count(x)>1 )]))
print(duplicate)
