# # conditional statements
# ''' Conditional statements in Python allow decision-making by
# executing different blocks of code based on conditions
#  Decision making can be understood with an example 

#  eg - you will receive a number from the user if the number is 

#  greater than 10 you will do task A and lower than 10 you 

#  will do task b
 
#  Here the situation is simple Number will decide which task
# will be executed
#  That means now we will control the flow of our program
# based on some conditions thats why these statements are
# also known as control flow statement.'''

# # a=int(input("enter to do the task"))
# # if a>10:
# #     print("task a")
# # else:
# #     print("task b")

# # types of conditional statements
# '''  Generally there are 3 types of variation in conditional
# statements
# 5 For syntax you have to watch the video for better
# understanding
# 5 if - Executes if the condition is True*
# 5 if-else - Executes if True, another if Fals3
# 5 if-elif-else - Checks multiple condition in sequence.'''

# #if
# a=13 # IF a value is greater than 10 i will do task a if a value is less than 10 i will do task b

# if a>6:
#     print("i will do task a")
#      # yes it is comparision operator what it gives it gives answer in true and false now what
# #if will do? it captures comparision operator and provide result basis on it
# ''' why we use : colons when we apply colons press enter we wil see on line 37 there is 5 spaces
# and these 5 spaces are known as indentations
# indentation means if you are using any specific block of code we have to follow 4-5 spaces
# in that we doesnt do that it shows error '''

# #else 
# '''can we write condition in else statement also answer is no we cannot write condition in it
# we can write conditional statement only in if statement. if (if) condition statement is true 
# then only it will execute and if (if) condition is false then it will not execute then
# the else will execute'''


# if a>10:
#     print("i will do task a")# ya toh ye hoga agar if statement hua true then if will execute 
# else:
#     print("i will do task b")# ya toh ye hoga agar if statement false then else statement will be execute

# '''this all this is dependent on our condition that we provide by using comparision operators'''

# v=int(input("pls provide me the money"))
# if v==10:
#     print("chocobar")
# elif v>=30:
#     print("cone")
# else:
#     print("mango dolly")

# questions

# a=int(input("enter your number 1"))
# b=int(input("enter your number 2"))
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")

# gender=input("please enter your gender").strip()
# if gender=="male":
#     print("good morning sir")
# elif gender=="female":
#     print("good morning mam")
# else:
#     print("invalid")

# check=int(input("enter number to check even or odd"))
# if check%2==0:
#     print("even")
# else:
#     print("odd")

# name=input("enter your name")
# age=int(input("enter your age to check eligibility  "))
# if age>=18:
#     print(f"hello{name} you are eligible for voting")
# else:
#     print("hello",name,"you are not eligible")

# year=int(input("enter year to check"))
# if year%4==0:
#     print("its a leap year")
# else:
#     print("it is not a leap year ")
#check whter it is postive and even
# num=int(input("enter your number to check"))
# if num>0 and num%2==0:
#     print("yes it is positive and even")
# else:
#     print("invalid output")

