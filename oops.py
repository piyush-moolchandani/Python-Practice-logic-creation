'''real world entieties ko code me convert karne ko oops kehte hai '''


'''magic method(dinder method)'''
# x=10
# print(dir(x))

# class student:
'''students are :'''

# class student:
'''students are :'''
# obj=student
# print(id(student),id(obj))
# print(dir(student))
# print(student.__doc__)
# obj=student()
# print(id(obj),id(student))

'''"First letter must be capital and if we use two words, first must be Capital."

# object_name = class_name()
# object_name = class_name

# Class variable (Propertic) = class varible, instance, local varible. 
# Class methods (Function, behaviour) = instance, class, static methods. + Magic method dinder methods, constructor = __init__()
# """ Doc string. inside the class. """ 

# x = 10 
# print(dir(x))

class Aniruddh: 
    """Hello"""

# print(dir(Aniruddh))
# print(Aniruddh.__doc__)

# Modulirity and doc string for desciption.

objq = Aniruddh  # with out parencethesis create same as 
print(id(Aniruddh),id(objq))

obj = Aniruddh()  # responsible for instance or object
print(id(obj),id(Aniruddh))

"new method it is responsible for create object and assign  value in obect we use init / constructor and not create the object."'''
    

'''maaz oops'''
# -----------------------------------------------------------------------------------------------------
'''todays work'''
# class student:
#     print("hello")
# obj=student
'''both have same memory address'''
# obj=student()
'''now both have different memory address'''
'''()-is responsible for creating object'''
'''call karne pe internal 2 method call hoti hai
__new__(cls)-responsible to create obj
__init__(self)-constructor intials value provide karta hai obj ki
''''self ek refrence parameter hai jo  current obj ka memory address hold karta hai ye memory address.name bula lega ''''
they both are in dir method '''
# class student:
#     def __new__(cls):
#         print("from__new__method")
#         obj=super().__new__(cls)
#         return obj
#     def __init__(self):
#         print("constructor called")
#         print(id(self))
# obj=student()
# print(id(obj))
'''self-obj and self are ek variable ek hi bande ke doo naam
new naam object ne obj aur self ko memory address diya hai
if we remove init then also it will create object
init ke through kabhi obj create nahi hota'''

'''externally called new method '''
# class student:
#     pass
#     # def show(self):
#     #     print("hello")
# obj=student.__new__(student)
# print(id(student))
# print(id(obj))

'''init method'''
# class student:
#     def __init__(self,x,y,z):
#         print(x,y,z)
#         print(id(self))
# obj=student(10,20,30)
# print(id(obj))
'''by-default obj ka memory address jaega self me tabhi 3 positional arguement ki error dega as an first argue obj ka adress jata hai'''
'''we will always represent by self only '''
'''till now what we studied in oops 
class-blueprint of design
obj-physical existence
self-refrence jo current obj ka address hold karta hai '''
# -----------------------------basic class syntax----------------------------------------------------
'''how many constructor in a class '''
'''we can create n number of constructor but if we call object the last one will
call and give its value '''
# class students:
#     def __init__(self):
#         print("hello")
#     def __init__(self,x):
#         print("hello")
#     def __init__(self,x,y,z):
#         print("hello")
# obj=students()
'''method overload-ek class ke andar same constructor method this is not supported by python'''

# class students:
#     print("hello")
# cons-special type of method we dont need to call
# self-its a reference parameter jo current obj ka address hold karta hai  

'''variables'''
# its a obj visible property jo hum dekh sakte hai
# 3 types of var
'''instance
class
local'''

'''instance variable (object dependent variable)
(self dependent variable)
self ke saath jo variable hai wo saare instance hai 
= ke right side pe value hoti hai aur left pe variable
cons ka pehla variable memory address hold karta hai 
ese var jo obj ki value pe dependent hai jo obj badalte hi naam badalde wo instance var hai
'''
# class student:
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
# obj1=student("piyush",101)
# obj2=student("maaz",102)
# print(obj1.n,obj2.r)
# esa method jiska pehla parameter self hota hai use instance method kehte hai
'''instance variable declaration
inside class(inside ke andar kaha declare kar sakte hai)-inside constructor,inside instance method
outside class'''
# class student:
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#     def add_new(self,city):
#         self.c=city
# obj=student("piyush",101)
# obj.add_new("bhopal")
# obj.x=10
"""calling instance var same as declaration (class ke andar access through self,class ke bahar access through obj)"""
# class student:
#     def __init__(self,name,roll):
#         self.n,self.r=name,roll
#         print(self.n,self.r)
#     def add_new(self,city):
#         self.c=city
#         print(self.n,self.r,self.c)
# obj=student("piyush",101)
# obj.add_new("bhopal")
# obj.x=200
# print(obj.n,obj.r,obj.c,obj.x)

'''error'''
# class student:
#     def __init__(self,name,roll):
#         self.n,self.r=name,roll
#         print(self.n,self.r)
#     def add_new(self,city):
#         self.c=city
#         print(self.n,self.r,self.c)
# obj=student("piyush",101)
# # obj.add_new("bhopal") if we remove this it will give error 
# print(obj.n,obj.r,obj.c)
''' kisi bhi class ke andar func uss class ki method kehelati hai 
func-isko direct call kar sakte hai
method-method hamesha obj ke saath create hota hai isko hum direct call nahi kar sakte 
iske liye humme obj ki requirement hai '''

'''class variable'''
'''ye wo var hai jo obj badalne me apni value nahi badalta
(object independent variable)
'''
'''declaration /calling
inside class-in class scope,in constructor,in instance method
outside class'''
'''class ke andar inside var banane ke liye class ke naam ke saath banate hai'''
# class student:
#     school_name='shss'
#     def __init__(self,name,roll):
#         self.n,self.r=name,roll
#         student.school_code=12345
#         print(student.school_name,student.school_code)
# obj=student('piyush',101)

'''instance method ke through dec/call'''
# class student:
#     school_name='shss'
#     def __init__(self,name,roll):
#         self.n,self.r=name,roll
#         student.school_code=12345
#         print(student.school_name,student.school_code)
#     def add_new(self):
#         student.school_city='bhopal'
#         print(student.school_name,student.school_city)
# obj=student('piyush',101)
# obj.add_new()
'''interview-kya const ko bahar call kar sakte hai toh ha ye special method hai
jo '''

'''outside of the class'''
# class student:
#     school_name='shss'
#     def __init__(self,name,roll):
#         self.n,self.r=name,roll
#         student.school_code=12345
#         print(student.school_name,student.school_code)
#     def add_new(self):
#         student.school_city='bhopal'
#         print(student.school_name,student.school_city)
# obj=student('piyush',101)
# obj.add_new()
# student.course="python"
# print(student.school_name,student.school_code,student.school_city,student.course)

'''interview question'''
'''suppose roll galat ho gayi toh const ki help se modify kar sakte hai'''
# class student:
#     school_name='shss'
#     def __init__(self,name,roll):
#         self.n,self.r=name,roll
#         student.school_code=12345
#         print(student.school_name,student.school_code)
#     def add_new(self):
#         student.school_city='bhopal'
#         print(student.school_name,student.school_city)
# obj=student('piyush',101)
# print(obj.n,obj.r)
# obj.__init__('rahul',110)
# print(obj.n,obj.r)
'''ab const ko hum keh rahe ki call nahi karte toh uska dusra juggad kya hai
agar hum yaha pe method banade to iss jugaad se hum value update kar sakte hai '''
# class student:
#     school_name='shss'
#     def __init__(self,name,roll):
#         self.n,self.r=name,roll
#         student.school_code=12345
#         print(student.school_name,student.school_code)
#     def add_new(self):
#         student.school_city='bhopal'
#         print(student.school_name,student.school_city)
#     def update_instance(self,up_n,up_r):
#         self.n=up_n
#         self.r=up_r
# obj=student('piyush',101)
# print(obj.n,obj.r)
# obj.update_instance('rahul,',110)
# print(obj.n,obj.r)

'''local variable'''
'''scope dependented var ko local kehte hai bahar call nah ikar sakte'''
'''dec/call
inside class-in class scope,in constructor,in instance method
outside class
scope ke bahar acceseble nahi hai
kisi bhi dusre scope pe na define kar sakte hai na call kar sakte hai
call kahape hoga ye -within the scope jis scope me wo define hoga wahi ye call ho sakta hai
bahar nahi 
ye sab class ki properties hai
'''
# class student:
#     school_name='shss'
#     def __init__(self):
#         x=10
#         print(x)
#     def add_new(self):
#         y=20
#         print(y)

"""always use camel case first letter capital"""
"""kya kya ho gaya
class class name:
    doc string
    variables
    """
"""python ke pp8 ke sare recomendation dikhao chat gpt"""
# -----------------------------------------------variables end---------------------------------------------------
"""methods"""
'''instance method(first parameter is self)done up
class(first parameter is cls & @classmethod)
static(withou self and cls as a parameter & @staticmethod decorator ka use)'''

'''class method'''
'''hum class method se uski value ko modify ya change karne ke liye use karte hai'''
# class Student:
#     school_name='shss'
#     grad='10th'
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#     @classmethod
#     def up_grade(cls,new_grad):
#         cls.grad=new_grad
# obj=Student('piyush',101)
# print(Student.school_name,Student.grad,obj.n,obj.r)
# obj.up_grade('11th')
# print(Student.school_name,Student.grad,obj.n,obj.r)
# isme cls matlab class ka naam (Student)

'''new variable add karna'''
# class Student:
#     school_name='shss'
#     grad='10th'
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll
#     @classmethod
#     def up_grade(cls,new_grad,city):
#         cls.grad=new_grad
#         cls.c=city
# obj=Student('piyush',101)
# print(Student.school_name,Student.grad,obj.n,obj.r)
# obj.up_grade('11th','bhopal')
# print(Student.school_name,Student.grad,obj.n,obj.r,Student.c)

'''static method(na obj se rishta na class se rishta)'''
# class Student:
#     school_name='shss'
#     grad='10th'
    # def __init__(self,name,roll):yaha pe self object hai
        # self.n=name
        # self.r=roll
    # @staticmethod
    # def show()
    # def show(self,cls):Student.show() missing 2 required positional arguments: 'self' and 'cls'(error)
    # def show(self,cls):yaha pe self ek parameter hai
#         print('hello')
#         print(self,cls)
# obj=Student("piyush",101)
# obj.show(10,20)
# obj.show()Student.show() takes 0 positional arguments but 1 was given(error)

'''overall summary'''
# class classname:
#     '''doc string'''
#     constructor
#     variables-instance(self),class,locals
#     method-instance(self),class(cls) @classmethod,static @staticmethod

# terms
# object
# self
# constructor
# ---------------------------------------------------------------------------------------------------------
                                     #  properties 
"""1.abstraction(data protection)
2.encapsulation   (access specifier(python me nahi hota)/modifier)      
------------------------------------------------
3.inheritence             (parent-child relation(code reusability in inheritence))(types of inheritence,supermethod),mro(method resolution order-child ke pass jo sabse pass parent hoga wo usse dhundega fir uske baad aur parent),method overiding(python supported)
4.polymorphism  (ek hi func alag alag value ke liye alag alag behave karne lage ek hi bande ke ek se zyada roop hone se wo poly kehlata hai)(dada ji ki zammen papa ke pass by default means jo cheez carryforward ho rahi hai),method overloading(not python supported)"""



'''inheritence'''
# it tells parent child relationship
# syntax:-
# class Parent:
#     properties
#     behaviours
# class child(Parent):
#     pass
# child ki help se main class ka obj aur var access kar paenge
# inheritence type
'''single level inheritence
          parent class
              |
              child clas'''
'''CODE'''
# basically parent ki cheez use karna child ke pass khud ka kuch nahi hai jaise mere pass sab papa ka diya hua mera kuch nahi hai
# uppar class me jo code likha hai use dubara na likhna pade child se usse hum access kar skate hai code reusibility
# ek hi level hai
# class Parent:
#     x=10
#     def home(self):
#         print('home from parent class')
# class Child(Parent):  
#     pass
# obj=Child()
# print(obj.x)
# obj.home()

'''multi-level inheritence'''
""" grandparents         """
'''  |
      parent
        |
      child'''
# code
# dadaji ki property papa ke pass papa ki property bacche ke pass aur bacche ne kuch nahi kiya par sab kuch mil gaya
# class A:
#     def home(self):
#         print("home from gp")
# class B(A):
#     def home(self):
#         print("home from p")
#         super().home()
#     def car(self):
#         print("car from p")
# class C(B):
#     pass
# obj=C()
# obj.home()
# obj.car()
# 2 alag alag class ke andar same method hoti hai use method overwrite python supports it inheritence ke anadr hi hona chaiye
# main class super class uske neeche sub class 

'''multiple inheritence'''   
'''parent 1   parent 2
            |
        child'''
# mummy ki property aur papa ki property bachhe ke pass
'''code'''
# class A:
#     def home(self):
#         print('home from a')
# class B:
#     def home(self):
#         print('home from b')
#     def car(self):
#         print('car from b')
# class C(A,B):
#     pass
# obj=C()
# obj.home()
# obj.car()
''' dusre waale parent ke ghar ko access karne ke liye method(mro)-method resolution order
it works on depth first algorithm'''
# class A:
#     def home(self):
#         print('home from a')
# class B:
#     def home(self):
#         print('home from b')
#         A().home()
#     def car(self):
#         print('car from b')
# class C(B,A):
#     pass
# obj=C()
# obj.home()
# obj.car()
# is logic ko mro bolte hai kis parent ke pass sabse pehle jaega

'''harechical inheritence'''
''' parent
     |
   child1-child2        '''

# class A:
#     def home(self):
#         print('home from a')
#     def car(self):
#         print("car from a")
# class B(A):
#     pass
# class C(A):
#     pass
# obj1=B()
# obj2=C()
# obj1.home()
# obj1.car()
# obj2.home()
# obj2.car()

'''hybrid inheritence'''
''' parent
     |
   child1-child2 
    |
    --ek se zyada inheritence jaha hai usko hybrid kehte hai       '''
# code
# class A:
#     def home(self):
#         print('home from a')
# class B:
#     def home(self):
#         print('home from b')
#     def car(self):
#         print('car from b')
# class C(A,B):
#     pass
# obj=C()
# obj.home()
# obj.car()
# class A:
#     def home(self):
#         print('home from a')
#     def car(self):
#         print("car from a")
# class B(A):
#     pass
# class C(A):
#     pass
# obj1=B()
# obj2=C()
# obj1.home()
# obj1.car()
# obj2.home()
# obj2.car()


'''abstraction'''
# impt data ko hide karna 
'''1.declare at least Abstract class
2.at least one abstract method
3.kisi bhi class ke andar abc ko  inherit karne ko abs krhte hai
4.@abstract koi ek method ka naam declare karde isko hum abs mehtod kehte hai
bina chaabi ke bike ko access nahi kar sakte ese hi @abstractmethod chabbi hai class ki
'''
'''code syntax'''
# from abc import ABC,abstractmethod
# class Calculator(ABC):
#     @abstractmethod
#     def register(self):  lock
#         pass
# class B(Calculator):
#     def register(self):  key
#         print('hello')
# obj=B()

'''example code'''
'''calculator'''
from abc import ABC,abstractmethod
# class Calculator(ABC):
#     def add(self,*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         print(sum)
#     @abstractmethod
#     def multi(self):
#         pass
# class A(Calculator):
#     def multi(self,*n):
#         multi=1
#         for i in n:
#             multi=multi*i
#         print(multi)
# obj=A()
# obj.add(5,89,56)
# obj.multi(5,6)

'''gate me do taale hai aur hum ek chaabi de rahe hai'''
'''normal method 
concrete method'''
# class Calculator(ABC):
#     def add(self,*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         print(sum)
#     @abstractmethod
#     def multi(self):
#         pass
#     @abstractmethod
#     def division(self):
#         pass
# class A(Calculator):
#     def multi(self,*n):
#         multi=1
#         for i in n:
#             multi=multi*i
#         print(multi)
#     def division(self,*n):
#         sum2=0
#         for i in n:
#             sum2=sum2+i
#         print(sum2)
        
# obj=A()
# obj.add(5,89,56)
# obj.multi(5,6)
# obj.division(24,2)

'''encapsulation'''
'''saaari class ko ek me mix kardena encapsulation hota hai
uppar jitni padi saari issi ka example hai'''
'''to acheive encap uske andar acces modifier ya access modifier
they are of 3 categories
1.public variable/method(python term x=10,show(self):) har jaga acceseble
2.protected variable/method (_x,_show(self)) covered campus ground bahar ka koi aceess child class iske andar acess uske ghar ke log acess
3.private variable/method (__x,__show(self)) phone ka pass sirf hum hi access kar skate hai child bhi nahi'''

'''code '''
'''public variable/method'''
# class Students:
#     school='shss'
#     def data(self):
#         print("method from student class")
# class A(Students):
#     pass
# obj=A()
# print(Students.school)
# obj.data() har jagah accesseble hai

'''protected variable/method(ye har jagah acceseble hai python not supported)
bana sakte hai par flavour lene ke liye ye kaam nahi karega'''
# class Students:
#     _school='shss'
#     def _data(self):
#         print("method from student class")
# class A(Students):
#     pass
# obj=A()
# print(Students._school)
# obj._data()


'''private var/method'''
# class Students:
#     __school='shss'
#     def __data(self):
#         print("method from student class")
# class A(Students):
#     pass
# obj=A()
# # print(Students.__school)
# # obj.__data()
# print(dir(Students)) using dir we take out the name store in memory then we can print it 
# why it is not acceseble

'''name menegeling logic apply here 
 we are making just for fun python doesnt support it '''

class Students:
    __school='shss'
    def __data(self):
        print("method from student class")
class A(Students):
    pass
obj=A()
print(Students._Students__school)
obj._Students__data()
# obj.__data()
print(dir(Students))
# what is name mengle
'''it is a technique where private var allot a memory where class name is saved
changeable by this we can access it everywhere it is access specifier and modifier '''


'''polymorphism'''
# function poly:-
# s='python'
# print(len(s))-output-6

# s=['python']
# print(len(s))-output-1
# ek func alag alag data type ke liye alag alag behave karna

'''operator polymorphism'''
# x=10
# y=20
# z=x+y
# print(z)output=30

# x='10'
# y='20'
# z=x+y
# print(z)-output=1020
'''ek hi operator alag alag behave kar rha'''

'''method polymorphism'''
# class A:
#     def speak(self):
#         print("human")
# class B:
#     def speak(self):
#         print('animal')
# for i in [A(),B()]:
#     i.speak()

'''Class and Calling Functions'''
# class Students:
#     def show(self):
#         print("oops")
# obj=Students()
# obj.show()

''' multilevel inheritence'''
# class Gp:
#     def home(self):
#         print(" hello from gp")
# class Parents(Gp):
#     def car(self):
#         print("car from parents")
# class Child(Parents):
#     def got(self):
#         print("got property")
# c=Child()
# c.home()
# c.car()
# c.got()

'''method polymorphism'''
class A:
    def bark(self):
        print("dog")
class B:
    def bark(self):
        print("cat")
for i in [A(),B()]:
    i.bark()
    



       












        

