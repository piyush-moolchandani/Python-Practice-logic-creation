'''errors'''
'''Errors occur due to mistakes in the code that prevent it from 
running. These can be syntax errors or logical errors'''
# ex-
# print("hello world"-->SyntaxError: '(' was never closed error in py

'''indentation error'''
'''Exceptions
You already know what is indentation and if you don’t 
follow it you will get the error
There is one more tab error when you mix tabs and 
spaces.
These errors cannot be handled. but what can be handled 
are exceptions.'''
# a=12
# if a==12:    --->IndentationError: expected an indented block after 'if' statement on line 16
# print("hello")
'''these are some kind of errors we cannot handle
syntax error
indentation error
tab error'''

# ----------------------------------------------------------------------------------------------

'''exceptions'''
'''Exceptions are unexpected events or errors that occurs 
during the execution of a program, which disrupts the normal 
flow of the program.'''
# ex->
# a=int(input("enter your number "))
# print(10/a)-->ZeroDivisionError: division by zero
'''if user proivides 0 like 0/10 so in this case it will be give undefine value
the py will give error-0 division error'''
'''Exceptions are unexpected events or errors that occurs 
during the execution of a program, which disrupts the normal flow of the program
Now this is a ZeroDIvisionError and can be counted as 
Exception and because of this exception the next line cannot 
be executed
Like this there are many other exceptions just leave the three 
errors we saw at start otherwise others are exceptions.
And the good part is we can handel them lets see how.'''
a=int(input("enter your number "))
try:
    print(10/a)
except ZeroDivisionError:
    print("sorry you cannot divide by 0")
print("ok i have done the division ")
''' exception handling keywords
try
except
else
finally
raise
'''
