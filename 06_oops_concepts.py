#!usr/bin/python

#Encapsulation: Binding of attributes and methods
print ("### Encapsulation ###")
#Class with package of variables/attributes and methods

#Abstraction: providing only essential information to the outside world and hiding their background details
print ("### Abstraction ###")

#Private and Public
print("### Private and Public ###")
#class Employee

#Inheritance
print("### Inheritance ###")
class User:
    def sign_in(self):
        print("logged in")
    def attack(self):
        print("Do nothing in base class")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        #User.attack(self) # will work as opposite of virtual-> will assign to base class method
        print("Attacking with power of: "+ str(self.power))

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print("Attacking with arrows of: "+ str(self.num_arrows))

wizard1 = Wizard('A',50)
archer1 = Archer('B',100)
# By default child class method is called as we have defination again in the chield class
print(wizard1.attack())
print(archer1.attack())

#Polymerphism: many forms
print("### Polymorphism ###")





