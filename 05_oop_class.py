#!usr/bin/python
### Classes ###
print ("Classes")
# Evenrything in python is a class, and access through object - 'hi'.__()
print(type( None))
print(type(True))
print(type({}))

# Class is the blueprint and object is the instances of the same class
class FirstClass:       #Class
    pass
print(type(FirstClass))
f1 = FirstClass         #Instrant of the same class
print(type(f1))

# OOP helps multiple people work on different part/module and combine at the end
print("###PlayerCharacters###")
class PlayerCharacters:
    #Class object attribute
    membership = True
    #Constructor: called by default when a new object is created
    #def __init__(self, name, age):
    #default parameters are also allowed
    def __init__(self, name='anonymus', age=18):
        self.name = name    #attributes / data members
        self.age = age

    #method: called only when its called through object as player1.run()
    def run(self):          #methods / member functions
        print("Run/")

    #Class Method: can be accessed without creating object/instance
    def add_numbers(cls, num1, num2):
        return num1+num2

    #Static method: nothing to do with class attributes
    def add_two_numbers(num1, num2):
        return num1+num2

player1 = PlayerCharacters('Saroj', 27)
print(player1)
print(player1.name)
player2 = PlayerCharacters('Rosi',26)
print(player2.age)
print(player2.membership)
#Access default parameters of the member
player3 = PlayerCharacters()
print(player3.name)

#Access class method, no object creation required
#print(PlayerCharacters.add_numbers(10,5))
#print(PlayerCharacters.add_two_numbers(10,5))

class Employee:
    def __init__(self, e_id, e_name, e_salary):
        self._e_id = e_id
        self.e_name = e_name
        self.__e_salary = e_salary

    #required in overload member attributes
    #def get_employee_data():
    def get_employee_data(self):
        print(e_name)
        print("Employee  ID is: "+_e_id + " &name is: "+e_name+" &sal is: "+ __e_salary)

e1 =Employee(1,'Saroj',5000)
#e1.e_name='Saroj Kumar'

e1.get_employee_data()






