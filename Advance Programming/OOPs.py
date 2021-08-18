
'''
everything we work on python is an object of some class
objects are instance of a class
class are the blueprint of an object
the function are called methods inside the class
the methods are created inside the class to keep them organised
the protected variable can be called from outside the class
private variables cannot be called from outside the class
the variables are by default public in python

OOPs Concepts in Python
1..Inheritance is the property by vitue of which a sub class can inherit the properties of a base class
2..Encapsualtion is used to restrict access to methods and variables
3..Polymorphisim means methods with same name can exist
    Dynamic Polymorphism
    Static Polymorphism
4..Abstraction Abstraction is used to hide internal details and show only functionalities. Abstraction is acheived through encapsulation

'''
class Car:
    
    def __init__(self,name,mileage,):        #...constructor
        self._name = name               #...declaring protected instance variable
        self.__mileage = mileage        #...declaring private instance variable
    
    def description(self):
        return f"the {self._name} gives mileage of {self.__mileage}km/l"
    
    def speed(self,speed):
        return f"{self._name} runs at {speed} km/hr"

class BMW(Car):        #...class BMW inherits Car
    
    def desc(self):
        return f"BMW is known for class"
    pass

class Ford(Car):       #...class Ford inherits Car
    
    def desc(self):
        return f"Ford is known for speed"

obj1 = BMW("BMW M760Li",24)            #...creating 1st object
print(obj1.description())       #...acessing protected variables through class
print(obj1.speed(200))

obj = Ford("Mustang",34)         #...creating 2nd objects
print(obj.description())        #...acessing protected variables through class
print(obj.speed(300))

print(obj._name)                #...accessing protected variable from outside the class
#print(obj.__mileage)           #...accessing private variable from outside the class(shows error)

for car in(obj1,obj):           #...two methods with same name is possible thrugh polymorphism
    print(car.desc())

print(obj.__dict__)



#...super function...
# the base class can be refered from the sub class using super function
class Human:

    def __init__(self, name):
        print(name, "is human")
    
class Fly(Human):

    def __init__(self, fly_name):
        print(fly_name, "cannot fly")

        super().__init__(fly_name)

class Swim(Human):

    def __init__(self, swim_name):
        print(swim_name, "can swim")

        super().__init__(swim_name)

class Species(Fly, Swim):

    def __init__(self, name):
        super().__init__(name)

obj = Species("John")


# abstraction
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")

t= Tesla ()   
t.mileage() 



# console input in class using decorators
class EmployeeSalary:
    
    def __init__(self,name,salary,bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    @classmethod                #...decorators
    def Input(data):                    #...function for user input
        return data(input('Name : '),
                    int(input('Salary : ')),
                    int(input('Bonus : '))
                   )
user = EmployeeSalary.Input()

class Department:

    def __init__(self,dept,max_employee):
        self.dept = dept
        self.max_employee = max_employee
        self.employee = []                      #...creating a list

    def add_employee(self,employee):
        if len(self.employee) < self.max_employee:
            self.employee.append(employee)
            return True
        return False

d = Department("Delivery",3)        #...creating a object
d.add_employee(user)                #...appending the data to list
       
for i in d.employee:                #...printing the values in list using loop
    print(i.name)
    print(i.salary)
    print(i.bonus)