'''Reverse a string without using [::-1]'''
# s = 'python'
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# print(rev)

'''Check if a string is palindrome'''
# s = "madam"
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# if rev==s:
#     print('palindrome')
# else:
#     print(' not palindorem')

'''Count vowels and consonants in a string'''
# s = 'piyush'
# vowel_count=0
# consonants_count=0
# for i in s:
#     if i in 'aeiou':
#         vowel_count+=1
#     else:
#         consonants_count+=1
# print({'vowel_count':vowel_count,'consonants_count':consonants_count})

'''Count frequency of each character in a string'''
# s = 'banana'
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''Remove duplicate characters from a string while preserving order'''
# s = "programming" 
# d={}
# ans=""
# for i in s:
#     if i not in d:
#         ans+=i
#         d[i]=1
# print(ans)

'''Find the first non-repeating character'''
# s='abaccd'
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]==1:
#         print(i)
#         break

'''Find the first repeating character'''
# s='abaccd'
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>1:
#         print(i)
#         break

'''Count words in a sentence'''
# s = "I am learning Django"
# l = s.split()
# count = 0 
# for i in l:
#     count+=1
# print(count)

'''Find the longest word in a sentence'''
# s = "I am learning Django"
# l=s.split()
# max_count=0
# for i in l:
#     if len(i)>max_count:
#         max_count=len(i)
#         ans=i
# print(ans)

'''Reverse every word of a sentence'''
# s = "I am learning Django"
# l = s.split()
# rev = ""
# for i in l:
#     for j in range(len(i)-1,-1,-1):
#         rev = rev + i[j]
#     rev = rev+" "
# print(rev)

# ====================================== LIST =====================================================

'''Find duplicates in a list'''
# l=[1,2,2,3,4,4]
# d = {}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>1:
#         print(i)

'''Remove duplicates from a list without using set()'''
# l=[1,2,2,3,4,4]
# d={}
# ans = []
# for i in l:
#     if i not in d:
#         ans.append(i)
#         d[i]=1
# print(ans)
 
'''13. Remove duplicates while preserving order'''
# l=[1,2,2,3,4,4]
# d={}
# ans = []
# for i in l:
#     if i  not in d:
#         ans.append(i)
#         d[i]=1
# print(ans)

'''14. Find common elements between two lists'''
# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 4, 5, 6, 7]
# for i in l1:
#     if i in l2:
#         print(f"the common elements are {i}")

'''Find elements present in first list but not second'''
# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 4, 5, 6, 7]
# ans=[]
# for i in l1:
#     if i not in l2:
#         ans.append(i)
# print(ans)

'''Flatten a simple nested list'''
# l = [[1,2], [3,4], [5]] 
# ans=[]
# for i in l:
#     for j in i:
#         ans.append(j)
# print(ans)

'''Find maximum and minimum without max() / min()'''
# l=[5,3,5,86,4,6,6,645,6,52,3,3]
# max_ele = l[0]
# min_ele = l[0]
# for i in l:
#     if i>max_ele:
#         max_ele=i
#     elif i<min_ele:
#         min_ele=i
# print(f"max_element {max_ele}")
# print(f"min_element {min_ele}")


'''Find second largest element'''
# l=[5,3,5,86,4,6,6,645,6,52,3,3]
# largest = 0
# se_largest = 0
# for i in l:
#     if i>largest:
#         se_largest = largest
#         largest = i
#     elif i>se_largest and i!=largest:
#         se_largest=i
# print(se_largest)

'''19. Find second smallest element'''
# l=[5,3,5,86,4,6,6,645,6,52,3,3]
# small = l[0]
# se_small = l[0]
# for i in l:
#     if i<small:
#         se_small=small
#         small=i
#     elif i<se_small and i!=small:
#         se_small=i
# print(se_small)

'''Separate even and odd numbers'''
'''Two Pointer Approach'''
# l=[1,2,3,4,5,6,7,8,9,10]
# left = 0
# for right in range(len(l)):
#     if l[right]%2!=0:
#         l[left],l[right]=l[right],l[left]
#         left+=1
# print(l)

'''Core Python'''
# l=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd+even)


'''Count even and odd numbers'''
# l=[1,2,3,4,5,6,7,8,9]
# even_count = 0
# odd_count = 0
# for i in l:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print({'even_count':even_count,'odd_count':odd_count})

'''Move all zeroes to the end'''
# l=[1,0,2,0,3,0,4,0]
# zeroes = []
# non_zeroes = []
# for i in l:
#     if i==0:
#         zeroes.append(i)
#     else:
#         non_zeroes.append(i)
# print(non_zeroes+zeroes)

'''25. Rotate a list by K positions'''  '''{LEft}'''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi = l[0]
#     for i in range(len(l)-1):
#         l[i] = l[i+1]
#     l[-1] = fi
# print(l)

'''25. Rotate a list by K positions'''  '''{RIGht}'''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     lv = l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i] = l[i-1]
#     l[0] = lv
# print(l)

'''Create a frequency dictionary from a list'''
# l = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''27. Find the key having maximum value'''
# d = {
#     "A": 10,
#     "B": 25,
#     "C": 15,
#     "D": 30
# }
# max_value = 0
# for i in d:
#     if d[i]>max_value:
#         max_value=d[i]
#         ans=i
# print(ans)
# print(max_value)

'''Sort a dictionary by values ascending '''
# d = {"A": 40, "B": 10, "C": 30, "D": 20}
# l = list(d.items())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i][1]>l[j][1]:
#             l[i],l[j]=l[j],l[i]
# ans = dict(l)
# print(ans)
        
# ans = dict(sorted(d.items(), key=lambda x: x[1]))
# print(ans)

'''Sort a dictionary by values descending '''
# d = {"A": 40, "B": 10, "C": 30, "D": 20}
# l = list(d.items())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i][1]<l[j][1]:
#             l[i],l[j]=l[j],l[i]
# ans = dict(l)
# print(ans)

# ans = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
# print(ans)

'''Merge two dictionaries'''
# d1 = {"a": 10, "b": 20}
# d2 = {"c": 30, "d": 40}
# l1 = list(d1.items())
# l2 = list(d2.items())
# ans = l1+l2
# d = dict(ans)
# print(d)

# d1 = {"a": 10, "b": 20}
# d2 = {"c": 30, "d": 40}
# merge_dict = d1|d2
# print(merge_dict)

''' without built in method'''
# d1 = {"a": 10, "b": 20}
# d2 = {"c": 30, "d": 40}
# d={}
# for i in d1:
#     if i not in d:
#         d[i] = d1[i]
# for j in d2:
#     if j not in d:
#         d[j]=d2[j]
# print(d)

'''D1 priority:
if j not in d:
    d[j] = d2[j]
D2 priority:
d[j] = d2[j]'''


'''Find common keys between two dictionaries'''
# d1 = {"a": 10, "b": 20,'f':78}
# d2 = {"c": 30, "a": 40,'f':34}
# for i in d1:
#     if i in d2:
#         print(f"The common keys are {i}")


'''Find keys having duplicate values'''
# d1 = {"a": 10, "b": 30,'g':78}
# d2 = {"c": 30, "a": 40,'f':10}
# for i in d1:
#     for j in d2:
#         if d1[i] == d2[j]:
#             print((i,j))


'''Invert a dictionary'''
# d = {"a": 1, "b": 2}
# new_dict = {}
# for i in d:
#     new_dict[d[i]] = i
# print(new_dict)

'''33.Group words according to their length'''
# l = ["cat","dog","apple","bat"]
# d={}
# for i in l:
#     length = len(i)
#     if length not in d:
#         d[length] = []
#     d[length].append(i)
# print(d)          


'''Replace Zero With One '''
# n = 2007
# new = 0
# while n>0:
#     digit = n%10
#     if digit == 0:
#         digit = 1
#     n=n//10
#     new = new*10+digit
# rev = 0
# while new>0:
#     digit=new%10
#     rev = rev*10+digit
#     new=new//10
# print(rev)


        
'''Count frequency of words in a sentence'''
# s = '"I am learning Python and I am learning Django"'
# l = s.split()
# d = {}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)


'''35. Convert two lists into a dictionary'''
# keys = ["a","b","c"]
# values = [1,2,3]
# d={}
# for i in range(len(keys)):
#     if keys[i] not in d:
#         d[keys[i]] = values[i]
# print(d)

'''2. Different length — shorter list tak'''
# keys = ["a", "b", "c", "d"]
# values = [1, 2, 3]
# d = {}
# for i in range(min(len(keys), len(values))):
#     d[keys[i]] = values[i]
# print(d)


'''Create list of squares using list comprehension'''
# l = [1,2,3,4,5,6,7,8]
# ans = [i**2 for i in l]
# print(ans)

'''Create list of even numbers using comprehension'''
# l = [1,2,3,4,5,6,7,8]
# ans = [i for i in l if i%2==0 ]
# print(ans)

'''Create list of odd numbers using comprehension'''
# l = [1,2,3,4,5,6,7,8]
# ans = [i for i in l if i%2!=0]
# print(ans)

'''Convert a list of strings to uppercase using comprehension'''
# l=["python", "django", "sql", "rest"]
# ans = [i.upper() for i in l]
# print(ans)

'''Extract numbers greater than 10'''
# l = [1,2,45,6,78,7,57,9,8]
# ans = [i for i in l if i>10]
# print(ans)

'''Create dictionary using dictionary comprehension'''
# l = [1, 2, 3, 4, 5]
# ans = {i:i**2 for i in l}
# print(ans)

'''Create a dictionary containing only even numbers and their squares.'''
# l = [1, 2, 3, 4, 5, 6]
# ans = {i:i**2 for  i in l if i%2==0}
# print(ans)

'''Using dictionary comprehension, create a dictionary containing only numbers greater than 5, 
where the number is the key and its cube is the value.'''
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ans = {i:i**3 for i in l if i>5}
# print(ans)
'''{ key : value  for item in iterable  if condition }
   ↓      ↓          ↓                   ↓
   i     i**3       i in l              i > 5'''


'''List ke numbers ko dictionary mein rakho. Agar number even hai toh value "Even" ho, warna "Odd"'''
# l = [1, 2, 3, 4]
# ans = {i:'even' if i%2==0 else 'odd' for i in l}
# print(ans)


'''Dictionary comprehension use karke dictionary banao jisme:
Sirf even numbers include hon.
Number key ho.
Uski square value ho.
Lekin agar square 200 se greater ho, toh us number ko dictionary mein include mat karo.'''
# l = [12, 5, 8, 21, 16, 7, 30, 11]
# ans = {i:i**2 for i in l if i%2==0 and i**2<=200}
# print(ans)


'''Dictionary comprehension use karke dictionary banao jisme:
Sirf odd numbers include hon.
Number key ho.
Uski cube value ho.
Lekin cube 3000 se greater ho toh exclude kar do.'''
# l = [5, 12, 7, 20, 15, 8, 25, 10]
# ans = {i:i**3 for i in l if i%2!=0 and i**3<=3000}
# print(ans)

'''Flatten a nested list using comprehension'''
# l = [ [1, 2], [3, 4], [5, 6] ]
# ans = [j for i in l for j in i]
# print(ans)
'''Normal loop:

for i in l:
    for j in i:
        print(j)'''

# comphernsion
'''[j      for i in l      for j in i]
 ↑           ↑               ↑
kya       outer loop      inner loop
store
karna'''

# =================================================================
'''FUNCTIONS'''
'''Write a function using default arguments'''
# def default(name,city='bhopal'):
#     return f'hello {name} welcome to {city}'
# ans1 = default('piyush')
# print(ans1)
# ans2 = default('piyush','indore')
# print(ans2)

'''Write a function using *args'''
# def test(name,*marks):
#     return f'{name}:{marks}'
# ans1 = ('piyush',67,89,34)
# print(ans1)

# def sum_all(*l):
#     total = 0
#     for i in l:
#         total+=i
#     return total
# x = sum_all(1,2,3,4,5)
# print(x)

'''Write a function using **kwargs'''
# def test(name,**kwargs):
#         print("UserName :", name)
#         for key,value in kwargs.items():
#                 print(key, ':' ,value)
# test('piyush',age=22,city="indore",role="django devloper")

'''Write a function that accepts both *args and **kwargs'''
# def stu_details(name,*marks,**details):
#     print("Student Name: ", name)
#     print("--- Marks ---")
#     for subject, score in marks:
#         print(subject, ":", score)
#     print("--- Details ---")
#     for key,value in details.items():
#         print(key , ':' ,value)
# stu_details('Piyush',('Maths', 98), ('Physics', 92), ('Chemistry', 90), ('English', 86), ('CS', 77),
#             age=22, city='bhopal', status='pass'
# )

'''Write a lambda function to square a number'''
# sq = lambda x:x**2
# print(sq(5))

'''49. Sort a list of tuples using lambda
[(1,3), (2,1), (4,2)]'''
# students = [
#     ("Rahul", 22),
#     ("Aman", 19),
#     ("Priya", 25),
#     ("Neha", 21)
# ]
# x = sorted(students,key=lambda x:x[1])
# print(x)

# l = [(1,3), (2,1), (4,2)]
# x = sorted(l,key=lambda x:x[1])
# print(x)

'''Use map() to square all numbers'''
# l =[1,2,3,4,5]
# ans = list(map(lambda x:x**2,l))
# print(ans)

'''Use filter() to get even numbers'''
# l = [1,2,3,4,5,6,7,8,9]
# ans = list(filter(lambda x:x%2==0,l))
# print(ans)

'''Use reduce() to calculate product of numbers'''
# from functools import reduce
# l = [1,2,3,4,5,6,7,8,9]
# ans = reduce(lambda x,y:x*y,l)
# print(ans)



# Ab recursion ka skeleton dekh

# Har basic recursion question mein ye structure dekhna:

# def function(n):

#     if STOP_CONDITION:
#         return

#     # current kaam

#     function(smaller_problem)


'''Write recursive sum of digits'''
# def sum_digits(n):
#     if n==0:
#         return 0
#     digit = n%10
#     return digit+sum_digits(n//10)
# print(sum_digits(1234))

'''Write a recursive factorial function'''
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))  

'''54. Write recursive Fibonacci'''
# def fibonaaci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonaaci(n-1)+fibonaaci(n-2)
# print(fibonaaci(5))

# def count(n):
#     if n==0:
#         return 0
#     count(n-1)
#     print(n)
# count(5)


# ===================================
'''generator'''
# basic syntax of generator
# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6
# res = numbers()
# for i in res:
#     print(i)

# def generator(n):
#     yield n
# res = generator(5)
# for i in res:
#     print(i)

# def test():
#     yield 1
#     yield 2
#     yield 3
# g = test()
# print(next(g))
# print(next(g))

'''56. Create a generator that yields numbers from 1 to N'''
# def num(n):
#     for i in range(1,n+1):
#         yield i
# res = num(20)
# for j in res:
#     print(j)

'''57. Create a generator for even numbers'''
# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i
# ans = even(20)
# for j in ans:
#     print(j)

''' generator expression'''
'''Basic syntax
(expression for item in iterable)
Condition ke saath:
(expression for item in iterable if condition)
Example:
g = (i for i in range(1, 11) if i % 2 == 0)'''
'''Generator function
    ↓
yield
    ↓
one value at a time

Generator expression
    ↓
(expression for item in iterable)
    ↓
one value at a time

next()
    ↓
next value maango

for loop
    ↓
generator ko automatically consume karta hai'''

# l = [1, 2, 3, 4, 5, 6]
# n = (i for i in l if i%2==0)
# for i in n:
#     print(i)

'''Create a generator for Fibonacci numbers'''
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         yield a
#         a, b = b,a + b
# ans = fibonacci(5)
# for j in ans:
#     print(j)

'''Create a generator that reads a large file line-by-line'''

# def read(file):
#     for i in file:
#         yield i
# ans = read( open('Django path.txt','r',encoding='utf-8'))
# for j in ans:
#     print(j)

''' using with open '''
# def read(file):
#     for i in file:
#         yield i
# with open('Django path.txt','r',encoding='utf-8') as file:
#     ans = file
#     for j in ans:
#         print(j)

'''60. Write a generator and compare it with a normal list-returning function'''

'''| Normal List                      | Generator                         |
| -------------------------------- | --------------------------------- |
| Saari values ek saath banata hai | One-by-one value deta hai         |
| Memory zyada use kar sakta hai   | Memory efficient                  |
| List return karta hai            | Generator object return karta hai |
| Data immediately available       | Data lazily generate hota hai     |
| Small data ke liye convenient    | Large data ke liye useful         |

Interview mein agar pooche "When would you prefer generator?"
Bolna:
"I would prefer a generator when I need to process a large amount of data sequentially
 and don't need all values in memory at the same time."

Aur ek important nuance: generator hamesha faster nahi hota. Uska primary advantage memory 
efficiency/lazy evaluation hai.

Code:-
'''
# def normal(n):
#     ans = []
#     for i in range(1,n+1):
#         ans.append(i)
#     return ans
# print(normal(5))

# def generator(n):
#     for i in range(1,n+1):
#         yield i
# for j in generator(5):
#     print(j)

'''"Why did you use yield instead of return in the generator?"
Ans:-
"Because yield allows the function to produce values one at a time and pause its execution, 
whereas return terminates the function and returns the complete result. Since the purpose of a 
generator is lazy evaluation and memory-efficient processing, we use yield."'''

'''"Can you use return i instead?"
Ans:- 
"Technically yes, but it would not work as a generator for producing multiple values. 
return terminates the function at the first return, while yield allows multiple values 
to be produced over multiple iterations."'''

'''61. Create a generator that yields squares of numbers from 1 to N.'''
# def square(n):
#     for i in range(1,n+1):
#         yield i**2
# for j in square(10):
#     print(j)
# ===============================================
'''Decorator'''
'''61. Create a simple decorator that prints before and after a function'''
# def decorator(func):
#     def wrapper():
#         print('starting')
#         func()
#         print('ending')
#     return wrapper

# @decorator
# def greet():
#     print('hello')
# greet()

'''error'''
# def decorator(func):
#     print('s')
#     func()
#     print('s')

# @decorator
# def greet():
#     print('h')
# greet()

'''|                                         | Without wrapper         | With wrapper            |
| --------------------------------------- | ----------------------- | ----------------------- |
| `starting/ending` kab chale?            | Decorator apply hote hi | `greet()` call hone par |
| `greet()` baad mein kaam karega?        | ❌                       | ✅                       |
| Original function ko replace kar sakte? | ❌                       | ✅                       |
| Decorator ka standard pattern?          | ❌                       | ✅                       |
'''

# def sum(func):
#     def wrapper(a):
#         total=0
#         while a>0:
#             digit=a%10
#             total+=digit
#             a=a//10
#         print(total)
#         func(9,8)
#     return wrapper
# @sum
# def addition(a,b):
#     print(a+b)
# addition(56)


# def decorator(func):
#     def wrapper(*args):
#         print('starting of sum')
#         func(*args)
#         print('ending of sum')
#     return wrapper
# @decorator
# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     print(total)
# add(2,4,5,67,4)

'''62. Create a decorator that calculates execution time'''
# import time
# def timer(func):
#     def wrapper():
#         starting_time = time.time()
#         func()
#         end_time = time.time()
#         execution_time  = end_time-starting_time
#         print(execution_time)
#     return wrapper

# @timer
# def check():
#     print('cheking time execution')
# check()

'''63. Create a decorator that checks whether a user/function argument is valid'''
# def age_checker(func):
#     def wrapper(age):
#         if age>=18:
#             print('you are allowed to enter')
#             func()
#         else:
#             print('you are not allowed to enter')
#     return wrapper
# @age_checker
# def check():
#     print('welcome')
# check(17)

# def login(func):
#     def wrapper(username,password):
#         create_username = input("create your username: ")
#         create_password = int(input('create your password: '))
#         if create_username==username and create_password==password:
#             print('sucessfully login')
#             func()
#         else:
#             print('invalid credintials')
#     return wrapper
# @login
# def welcome():
#     print('welcome to login')
# welcome('piyush',1234)

'''64. Create a decorator that accepts arguments'''
# def decorator(message):
#     def actual_decorator(func):
#         def wrapper():
#             print(message)
#             func()
#         return wrapper
#     return actual_decorator

# @decorator('starting_function')
# def greet():
#     print('hello')
# greet()

# ==========================================
'''OOPS'''
'''🧠 OOP Roadmap
Hum is order mein chalenge:
                    Class kya hai?
                    Object kya hai?
                    Class vs Object
                    __init__() constructor
COMPLETED -->        self
                    Instance variables
                    Instance methods
                    Class variables
                    Class methods
                    Static methods
                    Inheritance
                    Method overriding
                    super()
                    Encapsulation
                    Public / Protected / Private
                    Polymorphism
                    Abstraction
                    Abstract class / ABC
@property
Practical OOP interview questions'''

'''Create a class Student with name and marks'''
# class Student:
#     def info(name,marks):
#         print(name,marks)
# Student.info('piyush',90)

'''Create a class with constructor __init__()'''
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
# s1 = Student('piyush',90)
# print(s1.name)
# print(s1.marks)

'''class variable'''
# class Student:
#     college = 'sage'
#     def __init__(self,name):
#         self.name = name
# s1 = Student('piyush')
# print(s1.name,'-',s1.college)

'''local variable'''
# class check:
#     def __init__(self,mess):
#         self.mess = mess
#     def show(self):
#         msg = 'hello'
#         print(msg)
# s1 = check('hi')
# print(s1.mess)
# s1.show()

'''instaNCE method'''
# class Student:
#     def  __init__(self,name,marks):
#         self.n,self.r=name,marks
#     def display(self):
#         print(self.n,self.r)
# s1 = Student("Piyush", 90)
# s1.display()
        
''' class variable ko modify/call karna '''
# class Students:
#     college = 'lnct'
#     def __init__(self,name):
#         self.n=name
# s1  = Students('piyush')
# s2  = Students('rahul')
# Students.college = 'sage'
# print(s1.n,s1.college)
        
''' class method 
Create a class with @classmethod'''
# class Students:
#     college = 'lnct'
#     @classmethod
#     def change(cls,new_college):
#         cls.college = new_college
# Students.change('sage')
# print(Students.college)

''' static method
Create a class with @staticmethod'''
# class Calculator:
#     @staticmethod
#     def add(*args):
#         total=0
#         for i in args:
#             total+=i
#         return total
# print(Calculator.add(10,20))

# -------------------------------------------------
'''inheritance
Inheritance is an OOP mechanism where a child class acquires the attributes and methods 
of a parent class, mainly providing code reusability.
'''
''' types of inheritance'''
'''Inheritance
Single inheritance is a type of inheritance where a child class inherits attributes
 and methods from a single parent class.
Create a parent and child class demonstrating inheritance
single - level - inheritance'''
# class Animal:
#     def eat(self):
#         print('eating')
# class Dog(Animal):
#     def bark(self):
#         print('barking')
# d=Dog()
# d.eat()
# d.bark()   

''' multiple inheritance
Multiple inheritance is a type of inheritance where a single 
child class inherits from two or more parent classes.'''     
# class Father:
#     def property1(self):
#         print('property from father')
# class Mother:
#     def property2(self):
#         print('property from mother')
# class Child(Father,Mother):
#     pass
# c=Child()
# c.property1()
# c.property2()

'''multi-level-inheritance
Multilevel inheritance is a type of inheritance where a class inherits from another 
derived class, forming a chain of inheritance.'''
# class A:
#     def classA(self):
#         print('hello from class A')
# class B(A):
#     def classB(self):
#         print('hello from class B')
# class C(B):
#     def classC(self):
#         print('hello from class C ')
# child = C()
# child.classA()
# child.classB()
# child.classC()

'''Hierarchical Inheritance.
Hierarchical inheritance is a type of inheritance where multiple
child classes inherit from a single parent class.'''
# class Parent:
#     def property(self):
#         print('child 1 you get 60% property child 2 you get 40% property')
# class Child1(Parent):
#     def get_property(self):
#         print('getting parents 60% property ')
# class Child2(Parent):
#     def get_property2(self):
#         print('getting parents 40% property')
# c1 = Child1()
# c1.property()
# c1.get_property()

# c2 = Child2()
# c2.property()
# c2.get_property2()

'''hybrid inheritance
Ismein Hierarchical + Multiple inheritance combine ho rahe hain.
A → B and A → C = Hierarchical
D(B, C) = Multiple
Dono combine = Hybrid
Hybrid inheritance is a combination of multiple inheritance types, 
such as multiple, multilevel, or hierarchical inheritance.'''
# class A:
#     def show_a(self):
#         print('A')
# class B(A):
#     def show_b(self):
#         print('B')
# class C(A):
#     def show_c(self):
#         print('C')
# class D(B,C):
#     def show_d(self):
#         print('D')
# d = D()
# d.show_a()
# d.show_b()
# d.show_c()
# d.show_d()
                    # '''Inheritance ke 5 types — COMPLETE ✅
                    # Single → 1 parent → 1 child
                    # Multiple → multiple parents → 1 child
                    # Multilevel → inheritance ki chain
                    # Hierarchical → 1 parent → multiple children
                    # Hybrid → 2+ inheritance types ka combination'''


''' Method Overriding 
Method overriding occurs when a child class provides its own implementation of a method 
that is already defined in the parent class.'''
# class Animal:
#     def sound(self):
#         print("animal sounds coming....")
# class Dog(Animal):
#     def sound(self):
#         print('dog barks')

''' super() method
Parameter lena pad sakta hai → parent ko value pass karne ke liye.
Attribute banana dobara nahi padta → parent already bana raha hai. ✅'''
# class Animal:
#     def show(self):
#         print('animal')
# class Dog(Animal):
#     def show(self):
#         super().show()
#         print('dog')
# d = Dog()
# d.show()
'''super() is used in a child class to access or call methods and the constructor of its parent class, 
especially when extending or overriding parent-class functionality.
Short version:
super() allows a child class to call the parent class's methods or constructor.'''
'''with init '''
# class Student:
#     def __init__(self,name):
#         self.name = name
# class Profile(Student):
#     def __init__(self, name,rollno):
#         super().__init__(name)  
#         self.rollno = rollno
# p=Profile('piyush',123)
# print(p.name,p.rollno)

''' ENCAPSULATION 
Encapsulation is the process of bundling data and methods into a single class and 
restricting or controlling direct access to the data.'''

# class Student:
#     def __init__(self,name,city):
#         self.name = name
#         self.city = city
#     def display(self):
#         print(self.name,self.city)
# s1 = Student('piyush','bhopal')
# s1.display()
# s2 = Student('rohit','indore')
# s2.display()

''' public vaRIable
A public variable is a variable that can be directly accessed and modified from outside the class. 
In Python, variables without a leading underscore are public by default. '''

# class Student:
#     def __init__(self,name,marks):
#        self.name,self.marks = name,marks
#     def display(self):
#         print(self.name,self.marks)
# p = Student('piyush',78)
# p.marks = 97
# p.display()

''' protected variable
A protected variable in Python is represented by a single leading underscore and is intended for 
internal use within the class and its subclasses. It can still be accessed from outside because 
Python does not enforce strict access restrictions.'''
# class Students:
#     def __init__(self,name,marks):
#         self.name = name
#         self._marks = marks
# s = Students('piyush',45)
# s._marks = 90
# print(s.name,s._marks)
'''_marks protected convention hai, strictly private nahi. 
Python technically outside access ko prevent nahi karta.
Python's protected variables are not strictly enforced; 
a single underscore indicates that the attribute is intended for internal use.'''
'''internal usage example'''
# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
#     def deposit(self, amount):
#         self._balance += amount
#         print("Balance:", self._balance)
#     def show_balance(self):
#         print("Balance:", self._balance)
# a = BankAccount(1000)
# a.deposit(500)
# a.show_balance()

'''private variable
A private variable is an attribute prefixed with double underscores (__). 
Python applies name mangling to it, making direct access from outside the class 
difficult and helping protect internal class data.'''

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def show_balance(self):
#         print(self.__balance)
# a=BankAccount(5000)
# a.show_balance()
# print(dir(a))  --> this is name mangling using magic dinder method 
# we can see the calling name and call __private method
# Lekin dir() se object ke attributes/methods ki list dekh sakte ho:
# print(a._BankAccount__balance) --> this is name mangling method

'''Coding Question 🔥
Ek BankAccount class banao:
__balance private variable ho.
deposit(amount) method ho jo balance mein amount add kare.
show_balance() method current balance print kare.
Object mein initial balance 1000 rakho.
deposit(500) call karo.
Phir show_balance() call karo.'''
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def show_balance(self):
#         print(self.__balance)
# p = BankAccount(1000)
# p.deposit(500)
# p.show_balance() 
        
''' Polymorphism 
Polymorphism is an OOP concept where the same method or interface 
can have different implementations or behaviors depending on the object.
Jo humne Method Overriding padha tha, woh polymorphism achieve karne ka ek common way hai.'''

# class Dog:
#     def sound(self):
#         print('bark')
# class Cat:
#     def sound(self):
#         print('meow')
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()

''' Abstraction. 
Abstraction is the process of hiding implementation details and exposing 
only the essential functionality to the user. In Python, abstraction can be implemented 
using abstract classes and abstract methods from the abc module.
Abstract method = parent mein requirement define, child mein actual implementation. 🔥

Bas ye distinction yaad rakhna: abstract method ka purpose “hume implementation nahi 
pata” se zyada “child classes ko ye method implement karna mandatory hai” hai.'''
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print('barks')
# d=Dog()
# d.sound()

'''Q: Shape naam ki abstract class banao.
ABC aur abstractmethod use karo.
area() naam ka abstract method banao.
Rectangle class Shape se inherit kare.
Rectangle mein area() implement karo.
Length = 10, breadth = 5
Area print karo.'''
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#     def area(self):
#         print('the area of rectangle is',self.l*self.b)
# a = Rectangle(10,5)
# a = a.area()

''' @property 
@property is a decorator that allows a method to be accessed like an attribute, 
without explicitly calling it with parentheses. It is commonly used for controlled 
access to object data.
@property allows a method to be accessed like an attribute, 
while @property_name.setter allows controlled modification of that property.'''
# class Student:
#     def __init__(self,name):
#         self._name = name
#     @property
#     def name(self):
#         return self._name
# s = Student('piyush')
# print(s.name)
'''Employee class banao jisme salary property ho. Salary 0 se kam set nahi honi chahiye. 
Tum code likho, main interview-style review karunga. 💪'''
# class Employee:
#     def __init__(self,salary):
#         self._salary = salary
#     @property
#     def salary(self):
#         return self._salary
#     @salary.setter
#     def salary (self,check_salary):
#         if check_salary<0:
#             print('salary cannot be negative')
#         else:
#             self._salary=check_salary
# s = Employee(20000)
# print(s.salary)
# s.salary = 80000
# print(s.salary)
# s.salary = -42356
# print(s.salary)

'''__str__()'''    
'''"__str__() is a special method in Python that returns 
a human-readable string representation of an object. 
It is commonly used when an object is passed to print()."'''
# class Students:
#     def __init__(self,name,marks):
#         self.name,self.marks = name,marks
#     def __str__(self):
#         return self.name+" "+self.marks
# s = Students('piyush','98')
# print(s)

'''75. Implement __len__() in a custom class'''
# class Students:
#     def __init__(self,students):
#         self.students = students
#     def __len__(self):
#         return len(self.students)
# s = Students(["Piyush", "Rahul", "Aman"])
# print(len(s))

'''76. Create a class that keeps track of how many objects have been created'''
# class Student:
#     count = 0
#     def __init__(self,name):
#         self.n = name
#         Student.count+=1
# s1 = Student("Piyush")
# s2 = Student("Rahul")
# s3 = Student("Aman")
# print(Student.count)
# ==================================================================================== oops ended

# ==============================
''' EXCEPTION HANDLING '''
'''Exception kya hota hai?
Error vs Exception
try
except
else
finally
Multiple except
Specific exceptions (ValueError, TypeError, ZeroDivisionError, etc.)
raise
Custom Exception
Practical coding questions'''

'''what is exception
An exception is a runtime error that interrupts the normal flow of program execution.'''

''' error vs exception
| Error                                                             | Exception                                                              |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Usually serious problem hoti hai                                  | Runtime par aane wali problem hoti hai                                 |
| Program ko recover karna generally difficult hota hai             | Exception ko `try-except` se handle kar sakte hain                     |
| Examples: `SyntaxError`, `IndentationError`                       | Examples: `ValueError`, `TypeError`, `ZeroDivisionError`, `IndexError` |
| Mostly code/program structure se related errors bhi ho sakte hain | Mostly program execute hote waqt unexpected situation                  |
An error is a problem in a program that can prevent it from executing correctly, while an exception is a runtime problem that can usually be handled 
using exception-handling mechanisms like try-except.
'''

''' try-except 
try-except is used to handle exceptions and prevent the program from terminating unexpected'''
'''86. Write code using try-except for division by zero'''
# n = int(input(" enter number to divide "))
# try:
#      print(10/n)
# except ZeroDivisionError:
#     print('Cannot divide by zero')

'''Specific exceptions should be handled instead of using a bare except, because it makes error 
handling more precise and avoids hiding unexpected problems.'''
'''87. Handle invalid integer input
   
'''
# try:
#     n = int(input(" enter your number "))
#     m = int(input(" enter your number "))
#     print(n/m)
# except ZeroDivisionError:
#     print(' cannot divide by zero ')
# except ValueError:
#     print(' invalid value ')

''' else 
else block runs only when the try block executes successfully without raising an exception.'''
'''89. Use else with try-except'''
# try:
#     n = int(input(" enter your number "))
#     m = int(input(" enter your number "))
#     print(n/m)
# except ZeroDivisionError:
#     print('cannot divide by zero ')
# else:
#     print('division succesfull')


'''90. Use finally
finally is a block that executes regardless of whether an exception occurs or not,
 and it is commonly used for cleanup operations.'''
# try:
#     age = int(input('Age: '))
#     print(age)
# except ValueError:
#     print(' invalid age ')
# finally:
#     print('Input process completed')

'''  multiple except 
88. Use multiple except blocks
Ek try block ke saath multiple except laga sakte hain, taaki different 
exceptions ko separately handle kar sakein.'''
# try:
#     l = [10,20,30]
#     n = int(input(" enter your number: "))
#     print(l[n])
# except ValueError:
#     print(' invalid number ')
# except IndexError:
#     print(" invalid index ")

''' raise 
raise is used to explicitly raise an exception when a specific condition is not valid.
raise = manually exception generate karna.'''
# try:
#     age = int(input("enter your age: "))
#     if age<0:
#         raise ValueError('age cannot be negative ')
# except ValueError:
#     print(' age cannot be negative ')


'''Ek BankAccount class banao:
balance input lo.
Agar balance negative diya gaya → manually ValueError raise karo.
Agar valid hai → balance print karo.
except mein error handle karo.'''
# class BankAccount:
#     def __init__(self,balance):
#         self.b = balance
#         if self.b<0:
#             raise ValueError('balance cannot be negative ')
# try:
#     c = BankAccount(-4000)
#     print(c.b)
# except ValueError as e:
#     print(e)
       

''' custom exception
A custom exception is a user-defined exception created by
 inheriting from Python's Exception class. 
'''
# class InsufficientBalanceError(Exception):
#     pass
# class BankAccount:
#     def __init__(self,balance):
#         self.b = balance
#     def withdraw(self,amount):
#         if amount>self.b:
#             raise InsufficientBalanceError('Insufficient Balance')
#         self.b-=amount
#         print('Withdrawal successful','Balance Left:-',self.b)
# account = BankAccount(500)
# try:
#     account.withdraw(1000)
# except InsufficientBalanceError as e:
#     print(e)


'''91. Create your own custom exception'''
# class AgeError(Exception):
#     pass
# class Age:
#     def __init__(self,age):
#         self.a = age
#     def age_check(self):
#         if type(self.a)!=int or self.a<0 :
#             raise AgeError('Invalid Age')
#         print(self.a)
# try:
#     c = Age('-78')
#     c.age_check()
# except AgeError as e:
#     print(e)

# try:
#     n = int(input(" enter your number: "))
#     m = int(input(" enter your number: "))
#     divide = n/m
# except ValueError:
#     print("Please enter valid numbers")
# except ZeroDivisionError:
#     print(' cannot divide by zero ')
# else:
#     print(divide)
# finally:
#     print("Calculation completed")

# ==================================================================
'''✅ Completed
File Handling introduction
open() function
File modes: r, w, a, x, b (overview)
read()
readline()
readlines()
with open() / Context Manager
write()
Write vs Append
writelines()
File ko for loop se line-by-line read karna'''

'''📌 Remaining Topics
Next
seek() and tell()
read() vs line-by-line reading — practical differences
File existence and basic file operations (os / pathlib)
Exception handling with files
CSV file handling
JSON file handling
File Handling interview coding questions'''


''' File Handling '''  
'''File handling ka use Python mein files ko create, read,
 write aur update karne ke liye hota hai.
1️⃣ open() Function
Python mein file open karne ke liye open() use hota hai.
"data.txt" → file ka naam
"r" → read mode
Important File Modes
Mode
Meaning
r Read
w Write (purana content overwrite)
a Append (end mein add)
x New file create
b Binary mode'''
# file = open('django_topics.txt','r')      
# content = file.read()
# print(content)
# file.close()
'''read(), readline() aur readlines()'''
# 1️⃣ read() — Puri File Read
# 2️⃣ readline() — Ek Time Par Ek Line
# 3️⃣ readlines() — Saari Lines as List

'''readline'''
# file = open('django_topics.txt','r')  
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()
''' readlines()'''
# file = open('django_topics.txt','r')
# lines = file.readlines()
# print(lines)
# file.close()

''' with open()
"with open() is a context manager used for file handling. It automatically closes the file after
 the block completes, helping manage resources safely."'''
# with open('django_topics.txt','r') as file:
#     content = file.read()
#     print(content)
'''🧠 Iska flow
open() file open karta hai.
as file file object ko variable deta hai.
Indented block mein file operations hote hain.
Block complete hone par file automatically close ho jaati hai—even agar exception aaye.'''

''' write() method 
write() is a file object method used to write a single string into a file. 
It returns the number of characters written.'''
# with open('django_topics.txt','w') as file:
#     file.write('Hello Django')
# with open('django_topics.txt','r') as file:
#     content = file.read()
#     print(content)

''' append() method 
Append mode ("a") is used to add new content at the end of an existing file
without overwriting its existing content.
Existing content preserve rahega.
New content file ke end mein add hoga.
File exist nahi karti ho toh generally create ho jaati hai.
New line automatically add nahi hoti; zaroorat ho toh \n manually dena padta hai.'''
# with open('django_topics.txt','a') as file:
#     file.write("\npython")
# with open('django_topics.txt','r') as file:
#     content = file.read()
#     print(content)

'''Ek Python program likh bhai jo:
students.txt file mein "Piyush" write kare using w.
Same file mein "Rahul" append kare using a.
File read karke final content print kare.
with open() use karna hai. 👊'''

# with open('student.txt','w') as file:
#     file.write('piyush')
# with open('student.txt','a') as file:
#     file.write('\nrahul')
# with open('student.txt','r') as file:
#     content = file.read()
#     print(content)

''' for loop for reading lines-by-lines'''
# with open('django_topics.txt','r') as file:
#     for line in file:
#         print(line.strip())

'''write() vs writelines()
write() ek string file mein likhta hai.
writelines() strings ki list (ya iterable) ko file mein write karta hai.
✅ Newline khud dena padega:'''
# writelines
# students = ["Python\n", "Django\n", "SQL\n"]
# with open('student.txt','w') as file :
#     file.writelines(students)
# with open('student.txt','r') as file:
#     content = file.read()
#     print(content)

'''92. Read a text file and count lines'''
# with open('django_topics.txt','r') as file:
#     count = 0
#     for line in file:
#         count+=1
# print(count)

'''93. Count words in a file'''
# with open('django_topics.txt','r') as  file:
#     count=0
#     for line in file:
#       words = line.split()
#       count+=len(words)
# print(count)
   
''' tell() 
tell() returns the current position of the file pointer in the file.'''
# with open('student.txt','r') as file:
#     print(file.tell())
#     content = file.read(5)
#     print(content)
#     print(file.tell())
'''Agar file mein Hello Python hai:
Starting position → 0
read(5) → Hello
After reading 5 characters → position 5'''

'''seek()
seek() changes the file pointer to a specified position in the file.'''
# with open('student.txt','r') as file :
#     print(file.read(5))
#     file.seek(0)
#     print(file.read(6))
'''🔍 Dry Run
Initially pointer position 0 par hai.
read(5) → Hello read hua, pointer 5 par chala gaya.
seek(0) → Pointer wapas beginning par aa gaya.
Dobara read(5) → Hello read hua.'''

# with open('student.txt','rb') as file :
#     print(file.read(6))
#     file.seek(0)
#     print(file.read(6))
#     print(file.tell())
'''🔍 Aisa kyun ho raha hai?

Text mode mein Python tell() ka value hamesha simple character count nahi hota. Ye ek opaque position value hoti hai, jo text decoding aur newline handling ko track karne ke liye use hoti hai.

Tumhare case mein:

"rb" (binary mode) → 6 aa raha hai, kyunki binary stream bytes count karta hai.

"r" (text mode) → bada number aa raha hai, kyunki text stream ka internal position representation different ho sakta hai.

🎯 Interview mein kya yaad rakhna hai?

tell() returns the current stream position. In binary mode, it generally represents a byte position. In text mode, it can return an opaque position value, so it should not always be treated as a simple character count.

Aur seek(0) se beginning par jaana bilkul valid hai.

Tumhara code sahi hai bhai. Bas tell() ke behavior ka ye technical difference samajh lo.'''

'''File Existence Checking

Method 1: os.path.exists()
Kabhi-kabhi file open karne se pehle check karna hota hai ki file exist karti hai ya nahi.'''
# import os
# if os.path.exists('student.txt'):
#     print(True)
# else:
#     print(False)
'''Explanation:
import os → Python ka built-in module.
os.path.exists() → File ya directory exist karti hai ya nahi check karta hai.
Return value True ya False hoti hai.'''

'''Method 2: pathlib (Modern Approach)'''
# from pathlib import Path
# file_path = Path('student.txt')
# if file_path.exists:
#     print(True)
# else:
#     print(False)

'''File handling mein exceptions—FileNotFoundError
"FileNotFoundError occurs when we try to access a file that does not exist. 
We can handle it using a specific except FileNotFoundError block."'''
# try:
#     with open('data.txt','r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(' file doesnt exists ')

''' CSV File Handling
CSV file mein data rows aur columns ke format mein store hota hai.
Python mein CSV handle karne ke liye built-in csv module use karte hain.
"csv.reader() reads CSV data row by row and returns each row as a list."'''
# import csv
# with open('pizzas.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
'''import csv → CSV module import karta hai.
csv.reader(file) → CSV data read karta hai.
for row in reader → Har row ko list ke form mein deta hai.
Har value initially string hoti hai.'''

''''''




        
        
        