#!usr/bin/python

print ("############## Decorators ##############")

#del: while deleting hello it will only delete hello not greet, greet will be assigned for same memory but no function data at that address
def hello():
    print("helllllllllooooooooo")
greet = hello()
del hello
print(greet) # still indicate to same memory address


#Higher order function: which takes a function as argument or returns a function         filter, map also HOF
# Function takes another function as argument
def greet(func):
    func()
# FUnction returns another function
def greet2():
    def func():
        return 5
    return func

#Decorator: function that raps another function

def my_decorator(func):
    def wrap_func():    #just a wrapper
        print("*************")
        func()
        print("*************")
    return wrap_func

@my_decorator
def hello():
    print("hellooooooo")
hello()         # *s are used for the decoration in my_decorator
@my_decorator
def bye():
    print("See you later")
bye()

#another way to declare with decorator for a normal fucntion
def hello_2():
    print("Helloooo")
hello_3 = my_decorator(hello_2)
hello_3()



## Example: to find how long a function execution takes
from time import time

def performance(fn):
    def wrapper(*args, **kawargs):
        t1 = time()
        result = fn(*args, **kawargs)
        t2 = time()
        t = t2-t1
        print("your function took "+ str(t)+ " seconds to execute")
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
       i*5
long_time()

