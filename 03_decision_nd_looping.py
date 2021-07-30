#!usr/bin/python

import os
import sys

print "It is to learn decision and looping in Python \n"

###Decision making
var = 10

##IF statement
if (var==10):
    print "TRUE"
if (1):
    print "True"

##IF ELSE statement
if (var==20):
    print "True"
else:
    print "False"

##Nested if statement
if (var==1):
    print "value of var is 1"
elif(var==10):
    print "value of var is 20"
else:
    print "value of var is unkown"

#ternary operator
is_friend = True
can_message = "message allowed" if is_friend else "not allowed"
print(can_message)

###Looping
print("###Loop###")
count=0

##While loop
while (count<9):
    print "Count is: ", count
    count +=1

#Infinite loop
#while count == 9:
#    print "Infinite loop"

#Python supports else statement with loops
while (count>1):
    print "count is: ", count
    count -=1
else:
    print "Count is negative"


###For loop
#Syntax: for iterating_var in sequence:
#       ststements
#Iterable - list, tuple, dictionary, set, string
print "\n"

for letter in 'python':
    print letter

fruits= ['apple', 'banana', 'orange']
for fruit in fruits:
    print fruit

#Use of inbuilt function len
print len(fruits)
for index in range(len(fruits)):
    print fruits[index]

#Range
print("### Range ###")
list_n = [1,2,3,4,6,6,65,5,5]

for item in range(len(list_n)):
	print(list_n[item])
	
#Enumerate
print("###Enumerate###")
for i,char in enumerate("Hellllooooo"):
	print(i,char)
'''
#Else statenment with for
num = input("Enter an interger: ")
for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
'''

##Use of break, continue, pass statement
# Break statement cab be used with both for and while loop
print("### Break, continue, pass ###")
for latter in 'python':
    print latter
    if latter == 'h':
        break

count=0
while count < 9:
    print count
    count +=1
    if count==5:
        break
    
##Use of continue statement
# Continue statement rejects all the remaining statements in the current iteration of the loop

for latter in 'python':
    if latter=='h':
        continue
    print latter

count = 0
while count<9:
    count+=1
    if count==6:
        continue	#goes to while statement again, __<-|, doees not allow next statement to run in each loop
    print count

##Use of pass statement: Does nothing
#

for latter in 'Autonomous':
    print latter
    if latter=='n':
        pass
        print 'Its n'
    if latter=='o':
        pass
        print 'Its O'

      
raw_input()
