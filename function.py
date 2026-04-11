# What are functions
# Functions in Python group reusable code into a block that 
# can be executed by calling the function name. This helps 
# avoid repetition and makes programs modular and readable
# There are many in-build functions in python like print(), input()
# len() etc
# But you can create your own function and they are called as 
# user defined functions. To make your own function you have 
# to use def keyword and then name the function. After this 
# you have to call the function using name() and paranthesis.
# def greet():
#     print("hello python")
# greet()  #calling the function
# its a block of reussable code that we create and whenever we want to call it by its name then only it will be run

# Functions parameters and arguments
# First thing I want to talk about is parameters, parameters are 
# variables listed inside the function definition. 
# For making the function we have to accept inside the 
# parenthesis of the function.
'''parameters-the thing you accept is parameters
arguement-the thing you provide to parameters is arguement
jitne parameters utne arguements pass karne padhte hai'''
'''positional arguement'''
def sum(a,b):
    print("the sum of your number is",a+b)
sum(12,34)
sum(45,45)



# Arguments are the Values passed to a function when it is called
# For example you can say you have created the parameters 
# that are working like variables then we can pass the values to
# our variables using arguments
# As you can see name is the parameter and Alice is the argument 
# that we passed to name. And you can pass N number of  
# parameters and arguments but they must be same like if you 
# have taken 3 parameters you have to provide 3 arguments 
# otherwise there will be error.
# And another thing is first parameter, will always capture first 
# argument and so on. These arguments are called 
# argument.
# positional
'''write one call multiple'''
'''there are two types of function
1.inbuilt(pre-defined function)-print,input,type,id,sum,max,min,len,int,str etc
2.user-defined (made by us )
'''
# syntax
# def fun_name(parameters):
#     fun_body
#     return (it divides in 2 parts 1.func declaration 2.func calling)
# fun_name(arguement)                   func calling

# what is optional in calling func -parameter,return,arguement
# def- to declare func
# return - to terminate any func
# return is written default in function so it gives output by calling it by default written at the end of function none
# def xyz():
#     print("python")
# result=xyz()it returns python 
# print(result) it returns none 

# def xyz():
#     return 'hello'
# result=xyz()
# print(result) now the ouput will be hello 

'''parameters'''
# required variable in function body declared as parameters 
'''arguement'''
# value agains parameter are called arguements 
'''code for it'''
# def add(x,y):
#     return (x+y)
# p=int(input("enter "))
# q=int(input("enter "))
# result=add(p,q)
# print(result)
# jitna parameters pass karenge utni values pass karni hogi 

'''user defined funct is divided into four types'''
'''
1.with arguement with return type
2.with arguement without return type 
3.without arguement with return type
4.without arguement without return

 '''

'''1.with arguement with return type'''
# def func_name(parameters):
#     func_body
#     return
# result = func_name(arguement)

'''2.with arguement without return type '''
# def func_name(parameters):
#     func_body
# result = func_name(arguement)

'''3.without arguement with return type'''
# def fun_name():
#     fun_body
#     return
# result = func_name

'''4.without arguement without return'''
# def fun_name():
#     fun_body
# result = func_name

'''function examples'''
# def natural_no(n):
#     for i in range(1,n+1):
#         print(i,end=' ')
# x=int(input("enter "))
# natural_no(x)

# def natural_no(n):
#     i=1
#     while i<=n:
#         print(i)
#         i=i+1
# x=int(input("enter "))
# natural_no(x)

# def natural_no(n):
#     for i in range(1,n+1):
#         print(2*i,end=' ')
# x=int(input("enter "))
# natural_no(x)

# def natural_no(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+2*i
#     print(sum)
# x=int(input("enter "))
# natural_no(x)

# def natural_no(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# x=int(input("enter "))
# natural_no(x)

'''maximum in string''' 
# s='python'
# max=0
# for i in s:
#     x=ord(i)
#     if max<x:
#         max=x
# print(chr(max))

# def max_chr(s):
#     max=0
#     for i in s:
#         x=ord(i)
#         if max<x:
#             max=x
#     print(chr(max))
# p=input("enter ")
# max_chr(p)

'''min string value'''
# def max_chr(s):
#     min=255
#     for i in s:
#         x=ord(i)
#         if min>x:
#             min=x
#     print(chr(min))
# p=input("enter ")
# max_chr(p)

'''length of str'''
# def len(s):
#     count=0
#     for i in s:
#         count=count+1
#     print(count)
# a=input("enter ")
# len(a)

'''frequencies of str'''
# def count(s,ch):
#     count=0
#     for i in s:
#         if i==ch:
#             count=count+1
#     print(count)
# a=input("enter ")
# b=input("ch ")
# count(a,b)

'''type of arguements
1.positional
2.default positional
3.variable length positional arguement(*args)
4.keyword positional arguement 
5.default keyword positional arguement
6.variable length keyword positional argument(**kwargs)''' '''(alias same memory) '''

''' 1.postional arguement'''
# def fun_name(para1,para2,para3):
#     fun_body
# fun_name(argu1,argu2,argu3)
'''examples of positional arguments'''
# def add(a,b,c):
#     return (a+b+c)
# m=int(input("enter "))
# n=int(input("enter "))
# p=int(input("enter "))
# plus=add(m,n,p)
# print(plus)

# def new(a,b,c):
#     print(a,b,c)
# new(2,4,6)
# new() new() missing 3 required positional arguments: 'a','b' and 'c'(error)
# new(2) new() missing 2 required positional arguments: 'b' and 'c
# new(2,4,6,8) new() takes 3 positional arguments but 4 were given

''' 2.default positional'''
# def fun_name(para1=0,para2=0,para3=0):
#     fun_body
# fun_name(argu1,argu2,argu3)
'''example'''
# def new(x=0,y=0,z=0):
#     print(x,y,z)
# # new()
# new(2)
# new(3,6)

'''3.variable length positional arguement(*args)'''
# def fun_name(*args):
#    print(args)
#    print(type(args))
# fun_name()
'''example'''
# def fun_name(*args):
#    print(args)
#    print(type(args))
# fun_name()
# fun_name(2,4,6,7,8,4,65,7)

'''questions of *args'''
# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)
# n=int(input("enter how many numbers you want to add"))
# l=[]
# for i in range(1,n+1):
#     value=int(input(f"enter{i}value"))
#     l.append(value)
# print(*l)
# add(*l)
# if we remove*then it will goes like([2,4,5,6],)
# parameter me packing
# argument me unpacking
'''when we remove * from we have to apply nested loop'''
# def add(*n):
#     sum=0
#     for i in n:
#         for j in i:
#             sum=sum+j
#         print(sum)
# n=int(input("enter how many numbers you want to add"))
# l=[]
# for i in range(1,n+1):
#     value=int(input(f"enter{i}value"))
#     l.append(value)
# print(l)
# add(l)
'''4.keyword positional arguement '''
# syntax
# def fun_name(x,y,z):
#     print(x,y,z)
# # fun_name(z=5,y=2,x=10)
# fun_name()
# fun_name(z=5)

'''5.default keyword positional arguement'''
# def fun_name(x=0,y=0,z=0):
#     print(x,y,z)
# fun_name()
# fun_name(z=5)

'''6.variable length keyword positional argument(**kwargs)'''
# def fun_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# fun_name()
# fun_name(x=10,y=10,z=10)
# fun_name(x=10)

'''operations on kwargs'''
# d={"x":10,"y":20,"z":30}
# l=[]
# for i in d:
    # print((i,d[i]))
    # x=(i,d[i])
    # l.append(x)
    # l.append(i)
    #   l.append(d[i])
# print(l)

'''def kwargs'''
# def fun_name(**kwargs):
#     l=[]
#     for i in kwargs:
#         l.append(i)
#     print(l)
# fun_name(x=10,y=20,z=30)

'''scopes of variable'''
# x=10 global variable(scope throughout programm)
# def new():
#     y=20 local variable (scope within the block)
#     print(x)
# new()
# print(y)
'''2'''
# x=10
# def new():
#     x=20
#     print(x)
# new()
# print(x)
'''3'''
# x=10
# def new():
#    print(x)
#    y=20 changed variable name
# new()
# print(x)
# print(x) error:UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

'''4 local to global'''
# x=10
# def new():
#     global x
#     x=20
#     print(x)
# new()
# print(x)

'''5 global to local'''
# x=10
# def new():
#     print(globals()["x"])
#     x=20
# new()
# print(x)

'''non local variable'''

# def outer():
#     x=10
#     def inner():
#         nonlocal x
#         x=20          kisi bhi local ko nonlocal modify karne ke liye hum nonlocal ka use karte hai 
#         # print(x)
#     inner()
#     print(x)
# outer()

# -----------------------------------core python end------------------------------------------------











