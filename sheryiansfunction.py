'''What are functions
Functions in Python group reusable code into a block that 
can be executed by calling the function name. This helps 
avoid repetition and makes programs modular and readable
There are many in-build functions in python like print(), input()
len() etc
But you can create your own function and they are called as 
user defined functions. To make your own function you have 
to use def keyword and then name the function. After this 
you have to call the function using name() and paranthesis
func are block of code that can be executed whenever we call
'''
# example code
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even(3))


'''functions parameters and arguements'''
# parameter
'''First thing I want to talk about is parameters, parameters are 
variables listed inside the function definition. 
the thing you accept is parameters
the thing you provide to parameters is arguements
parameter jo hai apan accept karte hai 
arguements apan parameters ko transfer karte hai

'''
# example code
# def sum(a,b):->parameters(these para can have multiple types of values jab jab hum chahe usse change kar sakte hai)
#     print(a+b)    |->variables
# sum(5,6)->arguements                     -->(positional arguements)
# jitne parameters toh utne arguements 

'''types of arguements '''
'''First example shows how positional arguments work
Second example shows hoe default argument works here if you 
don’t pass any value still the function will run
Last example shows how keyword argument works using this 
you can pass values in any order.'''


'''keyword arguement '''
# example code
# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")
# hello(age=22,name="piyush")
        #   |--> keyword arguement(pehle se hi key ko select karke arguement provide karna)          
'''this is a key where i am giving arguement by myself ab continuation me follow nahi karna padega'''

'''default arguement'''
# example code
# def sum(a,b=45):
            #  |-->default parameter
#     print(f"the sum is {a+b}")
# sum(12)--> default arguement stated as 45

'''ques'''
'''check string is pallindrome or not'''
# def pallindrome(n):
#     rev=""
#     for i in range(len(n)-1,-1,-1):
#         rev=rev+n[i]
#     if rev==n:
#         print("pallindrome")
#     else:
#         print("Not pallindrome")
# pallindrome("madam")

'''return'''
# return will give back the value where you call the function
# ek func hai jo print karega ya fir values ko return kardeta hai
# def h():
#     return "piyush"
# print(h())

