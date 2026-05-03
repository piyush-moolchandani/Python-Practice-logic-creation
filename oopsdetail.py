'''OOPS (Object-Oriented Programming System) is a 
programming paradigm based on the concept of "objects", 
which can contain data (attributes) and code (methods)
I know it is tough to understand right now but it will be easy 
after learning there are many concepts that we have to learn 
like classes, objects , Encapsulation, inheritance, 
Polymorphism,  etc. So lets start
code reuse
multiple cheezo ko ek saath execute kar sakte ho
security provide karta hai
aur jab bhi aap oops banate ho management system ke bohot kaam 
aata hai-bank management library management project in oops'''

# classes in oops
'''A class is like a blueprint or template for creating objects
Think of a class like the blueprint of a house. It defines what 
the house should have (rooms, windows, etc.) but doesn’t 
build the house. An object is the actual house built using that 
blueprint.'''

'''Creating a class is super simple now lets see what is inside 
class. There are 2 types of things inside class Attributes and 
Methods
Attributes - Variables defined inside the class are Attribute
Methods - Functions defined inside a class are Methods'''
# basic syntax of class
# class Factory:
#     a=12  --> attributes
#     def hello(self): -->method
#         print("python")
    
    
#     print("i am getting initiliased")
# obj=Factory().a
# print(obj)
# obj2=Factory().hello()     --> calling first we call factory class then only we can acess them
# print(obj2)                --> in class there are attributes and methods


# objects
'''For understanding objects first look at this example you have 
a bag factory and that factory requires material of the bag, 
number of zips you need in that bag and number of pockets 
you need in your bag.
So this is a kind of a blueprint and using this blueprint 
Reebok, campus and some other companies provided 
their requirements and created their bags
Thus these companies became objects who created their 
bags using the blueprint.'''
# objs have all the powers of class these are basically childs of class 


# What is constructor

'''You saw last example where we wanted material, zips and 
pockets from the user to create an object.
If we talk about a function we can ask the user using 
parameters, but in class we can’t have parameters for that 
we use constructor.
A constructor is a method that runs automatically when we 
call a class and this constructor function will target the 
objects location'''

# class Students:
#     def __init__(self,name,roll_no):
#         self.name=name  --> instance attributes
#         self.roll_no=roll_no
#     def show(self):
#         print(f"your object details are {self.name},{self.roll_no}")
# creating an object with a value
# obj=Students("piyush",121)  
# accessing the attributes
# # print(obj.name,obj.roll_no)
# obj.show()


'''🔹 1. Create a Simple Class

Create a class Person with:

attributes: name, age
print them using an object'''

# class Person:
#     name="piyush"
#     age=12
# obj=Person().name
# obj2=Person().age
# print(obj,obj2)

'''🔹 2. Add a Method

Modify the Person class:

Add a method introduce() that prints:
"Hi, my name is ___ and I am ___ years old"'''

# class Person:
#     name="piyush"
#     age=12
#     def introduce(self):
#         print("Hi, my name is ___ and I am ___ years old")
# obj=Person()
# print(obj.name,obj.age)
# obj.introduce()

        
'''🔹 3. Constructor Practice

Create a class Car:

Use __init__ to initialize brand and model
Print them using an object'''

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# obj=Car("BMW","Sclass")
# print(obj.brand,obj.model)

'''🔹 4. Default Values

Create a class Student:

attributes: name, marks=0
Print both values'''

# class Student:
#     def __init__(self,name,marks=0):
#         self.name=name
#         self.marks=marks
# obj=Student("piyush")
# obj2=Student("piyush",85)
# print(obj.name,obj.marks)
# print(obj2.name,obj2.marks)


'''🔹 5. Multiple Objects

Create a class Dog:

attributes: name, breed
Create 2 different objects and print their details'''

# class Dog:
#     name="fronzy"
#     breed="germanshepherd"
# obj=Dog().name
# obj2=Dog().breed
# print(obj,obj2)
    

'''🔹 6. Simple Calculation Method

Create a class Rectangle:

attributes: length, width
method: area() → returns area '''

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# l = int(input("Enter length: "))
# w = int(input("Enter width: "))
# obj = Rectangle(l, w)
# print(obj.area())
        

'''🔹 8. Update Attribute

Create a class Account:

attribute: balance
method: deposit(amount) → increases balance'''

# class Account:
#     balance=10000
#     def deposit(self,amount):
#         return self.balance+amount
# a=int(input("enter amount to add "))
# obj=Account()
# print(obj.deposit(a))

# class Account:
#     def __init__(self):
#         self.balance = 10000
#     def deposit(self, amount):
#         self.balance += amount   
# a = int(input("Enter amount to add: "))
# obj = Account()
# obj.deposit(a)
# print(obj.balance)

'''🔹 9. Basic Inheritance

Create:

Parent class Animal with method sound()
Child class Dog that prints "Bark"


🔹 10. Method Overriding

Modify previous:

Parent Animal.sound() → "Some sound"
Child Dog.sound() → "Bark"'''




    

