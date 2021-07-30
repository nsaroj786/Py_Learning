#!usr/bin/python

print ("#### Generators ####")
# Generates list from number

def make_list(num):
    result = []
    for i in range(num):    # range is a generator
        result.append(i)
    return result

my_list = make_list(100)
print(my_list)

print(list(range(50)))      # range is a generator

#any generator is an iterator, eg: range
#but each iterator is not a generator, eg: list, for loop
#generator is usually a function

def generator_func(num):
    for i in range(num):
        yield i*2             # does the same append thing directly

for item in generator_func(10):
    print(item)

k = generator_func(5)
next(k)
print(next(k))

class MyGen():
    current = 0
    def __init__(self,first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current+=1
            return num
        raise StopIteration

gen = MyGen(0,100)
for i in gen:
    print (i)












