'''Python questions using only the map() function

1. Convert a list of integers into their squares using map().
Input: [1, 2, 3, 4] → Output: [1, 4, 9, 16]

2. Convert all strings in a list to uppercase using map().
Input: ["python", "map", "function"] → Output: ["PYTHON", "MAP", "FUNCTION"]

3. Convert a list of integers to strings using map().
Input: [1, 2, 3] → Output: ["1", "2", "3"]

4. Find the length of each word in a list using map().
Input: ["apple", "banana", "kiwi"] → Output: [5, 6, 4]

5. Double all numbers in a list using map().
Input: [3, 6, 9] → Output: [6, 12, 18]

6. Add 10 to every number in a list using map().
Input: [1, 2, 3] → Output: [11, 12, 13]

7. Convert temperatures from Celsius to Fahrenheit using map().
Formula: (C * 9/5) + 32
Input: [0, 20, 30] → Output: [32.0, 68.0, 86.0]

8. Extract the first character of each word using map().
Input: ["apple", "banana", "cherry"] → Output: ["a", "b", "c"]

9. Check if each number in a list is even or odd using map().
Input: [1, 2, 3, 4] → Output: ["Odd", "Even", "Odd", "Even"]

10. Convert a list of binary strings to integers using map().
Input: ["101", "111", "1001"] → Output: [5, 7, 9]

11. Combine two lists element-wise by summing them using map().
Input: [1, 2, 3], [4, 5, 6] → Output: [5, 7, 9]

12. Capitalize the first letter of each name in a list using map().
Input: ["raj", "wohit", "python"] → Output: ["Mahesh", "Soni", "Python"]

13. Remove spaces from each string using map().
Input: ["a p p l e", "b a n a n a"] → Output: ["apple", "banana"]

14. Given a list of numbers, return their cubes if they are even, else square them using map().
Input: [1, 2, 3, 4] → Output: [1, 8, 9, 64]

15. Convert a list of tuples (name, age) into formatted strings using map().
Input: [("Raj", 22), ("rahul", 21)]
Output: ["Raj is 22 years old", " rahul is 21 years old"]'''

# l=[1,2,3,4]
# res=map(lambda x:x**2,l)
# print(list(res))

# l= ["python", "map", "function"]
# res=list(map(lambda x: x.upper(),l))
# print(res)

# l=[1, 2, 3]
# res=list(map(lambda x: str(x),l))
# print(res)

# l= ["apple", "banana", "kiwi"]
# res=list(map(lambda x: len(x),l))
# print(res)

# l=[3, 6, 9]
# res=list(map(lambda x: x*2,l))
# print(res)

# l=[1, 2, 3]
# res=list(map(lambda x:x+10,l))
# print(res)

# l=[0, 20, 30]
# res=list(map(lambda x:(x*9/5)+32,l))
# print(res)

# l= ["apple", "banana", "cherry"]
# res=list(map(lambda x:x[0],l))
# print(res)

# l=[1, 2, 3, 4]
# res=list(map(lambda x:'even'if x%2==0 else 'odd',l))
# print(res)

# l=["101", "111", "1001"]
# res=list(map(lambda x: int(x,2),l))
# print(res)

# l1=[1, 2, 3]
# l2=[4,5,6]
# res=list(map(lambda x,y:x+y,l1,l2))
# print(res)

# l=["raj", "wohit", "python"]
# res=list(map(lambda x:x.capitalize(),l))
# print(res)

# l=["a p p l e", "b a n a n a"]
# res=list(map(lambda x:x.replace(" ",""),l))
# print(res)

# l=[1, 2, 3, 4]
# res=list(map(lambda x:x**3 if x%2==0 else x**2,l))
# print(res)

# l=[("Raj", 22), ("rahul", 21)]
# res=list(map(lambda x:f"{x[0]} is {x[1]} years old",l))
# print(res)

'''Extract last character of each word'''
# l=['python','java','javascript','mernstack']
# res=list(map(lambda x:x[-1],l))
# print(res)

'''Convert characters to ASCII values give list'''
# l=['a', 'B', 'c', 'D', '1']
# res=list(map(lambda x:ord(x),l))
# print(res)

'''Convert list of strings to lengths'''
# l=['python','java','javascript','mernstack']
# res=list(map(lambda x:len(x),l))
# print(res)

'''Add index to each element (use enumerate)'''
# l=['a','b','c','d']
# res=list(map(lambda x:(x[0],x[1]),enumerate(l)))
# print(res)

'''add 2'''
# l=[1, 2, 3] 
# res=list(map(lambda x:x+2,l))
# print(res)

'''2.	Multiply each number by 5'''
# l=[1, 2, 3, 4, 5, 6, 7, 8]
# res=list(map(lambda x:x*5,l))
# print(res) 

'''3.	Subtract 1 from each element'''
# l=[1, 2, 3, 4, 5, 6, 7, 8]
# res=list(map(lambda x:x-1,l))
# print(res)

'''5.	Convert integers to floats'''
# l=[1, 2, 3, 4, 5, 6, 7, 8]
# res=list(map(lambda x:float(x),l))
# print(res)

'''10.	Convert booleans to integers'''
# l=[True,False]
# res=list(map(lambda x:int(x),l))
# print(res)

'''11.	Reverse each string'''
# l=['python','java','html','javascript']
# res=list(map(lambda x:x[::-1],l))
# print(res)

'''12.	Add "ing" to each word'''
# l=['surf','jogg','run']
# res=list(map(lambda x:x+'ing',l))
# print(res)

'''15.	Repeat each string twice'''
# l=['python','java','html','javascript']
# res=list(map(lambda x:x*2,l))
# print(res)

'''16.	Remove vowels from each string'''
# l=['piyush','apple','eel']
# result = list(map(
#     lambda x: ''.join(filter(lambda ch: ch not in "aeiou", x)),
#     l
# ))
# print(result)

'''17.	Replace "a" with "@" in each string'''
# l=['apple','harsh','raga']
# res=list(map(lambda x:x.replace('a','@'),l))
# print(res)

'''18.	Add prefix "Mr." to each name'''
# l=['piyush','harsh','annirudh']
# res=list(map(lambda x:'mr.'+x,l))
# print(res)

'''19.	Add suffix ".com" to each string'''
# l=['python','java','html','javascript']
# res=list(map(lambda x:x+".com",l))
# print(res)

'''20.	Convert each string to its length'''
# l=['python','java','html','javascript']
# res=list(map(lambda x:len(x),l))
# print(res)

'''21.	Square only even numbers, keep others same'''
# l=[1,2,3,4,5,6,7,8,9,10]
# res=list(map(lambda x:x**2 if x%2==0 else x,l))
# print(res)

'''23.	Replace negative numbers with 0'''
# l=[-23,5,-7,8,-45,-5,67,89,-12]
# res=list(map(lambda x:0 if x<0 else x,l))
# print(res)

'''nvert numbers > 10 to "High", else "Low"'''
# l=[5,34,6,78,4,32,4,12]
# res=list(map(lambda x:'high'if x>10 else 'low',l))
# print(res)

'''25.	Return "Pass" if marks ≥ 40 else "Fail"'''
# l=[23,56,34,78]
# res=list(map(lambda x:"pass" if x>40 else 'fail',l))
# print(res)

'''27.	Add 100 to numbers less than 50'''
# l=[12,67,34,89,45,88]
# res=list(map(lambda x:x+100 if x<50 else x,l))
# print(res)

'''28.	Multiply by 2 if divisible by 3'''
# l=[6,4,15,14,12,21,9,5]
# res=list(map(lambda x:x*2 if x%3==0 else x,l))
# print(res)

'''29.	Return True if number is positive else False'''
# l=[-23,5,-7,8,-45,-5,67,89,-12]
# res=list(map(lambda x:True if x>0 else False,l))
# print(res)

'''30.	Convert numbers to their sign ("+", "-")'''
# l=[-23,5,-7,8,-45,-5,67,89,-12]
# res=list(map(lambda x:"+" if x>0 else "-",l))
# print(res)

'''34.	Combine two lists into strings'''
# l=[1,2,3,4]
# l2=['a','b','c','d']
# res=list(map(lambda x,y:str(str(x)+y),l,l2))
# print(res)

'''33.	Subtract second list from first'''
# l=[1,2,3,4]
# l2=[5,6,7,8]
# res=list(map(lambda x,y:y-x,l,l2))
# print(res)

'''35.	Compare elements of two lists (greater one)'''
# l=[45,67,8,9,43,89]
# l2=[56,78,4,2,7,99]
# res=list(map(lambda x,y:x if x>y else y,l,l2))
# print(res)

'''38.	Join two string lists with space'''
# l=['python','java','html','javascript']
# l2=['language','language','language','language']
# res=list(map(lambda x,y:x+ ' ' +y,l,l2))
# print(res)


'''39.	Create tuples from two lists'''
# l=[1,2,3]
# l2=[4,5,6]
# res=list(map(lambda x,y:(x,y),l,l2))
# print(res)

'''41.	Convert Celsius list to Kelvin'''
# l=[0, 10, 25, 30, 37, 100]
# res=list(map(lambda x:x+273.15,l))
# print(res)

'''47.	Format numbers as "Value: x"'''
# l=[10,20,30]
# res=list(map(lambda x:'value :'+ str(x),l))
# print(res)

'''48.	Convert list of tuples into sums'''
# l=[(1, 2), (3, 4), (5, 6), (7, 8)]
# res=list(map(lambda x:x[0]+x[1],l))
# print(res)

'''50.	Convert list of strings to reversed uppercase'''
# l=['python','java','html','javascript']
# res=list(map(lambda x:x.upper()[::-1],l))
# print(res)




# # -----------------------------------------------------------------------------------------------------
                                        #  filter

'''Python questions using only the Filter() function

Filter even numbers from a list.
Input: [1, 2, 3, 4, 5, 6] → Output: [2, 4, 6]

Filter odd numbers from a list.
Input: [10, 15, 20, 25, 30] → Output: [15, 25]

Filter numbers greater than 50.
Input: [10, 60, 45, 70, 30] → Output: [60, 70]

Filter strings with length greater than 4.
Input: ["apple", "bat", "ball", "hi"] → Output: ["apple", "ball"]

Filter positive numbers.
Input: [-2, 0, 5, 9, -7, 3] → Output: [5, 9, 3]

Filter words that start with the letter 'a'.
Input: ["apple", "banana", "avocado", "cherry"] → Output: ["apple", "avocado"]

Filter palindrome words.
Input: ["madam", "python", "level", "wow", "cat"] → Output: ["madam", "level", "wow"]

Filter vowels from a list of characters.
Input: ['a', 'b', 'e', 'i', 'o', 'p', 'u'] → Output: ['a', 'e', 'i', 'o', 'u']

1 Filter numbers divisible by both 3 and 5.
Input: [10, 15, 30, 42, 60, 70] → Output: [15, 30, 60]

1 Filter names that contain the letter 'a' or 'A'.
Input: ["Rahul", "Raj", "Python", "Code"] → Output: ["Rahul", "Raj"]

1 Filter numbers whose square is greater than 50.
Input: [2, 4, 6, 8, 10] → Output: [8, 10]

1 Filter words ending with 'ing'.
Input: ["running", "play", "eating", "dance"] → Output: ["running", "eating"]

1 Filter elements that are strings from a mixed list.
Input: [1, "apple", 3.5, "banana", True, "cherry"] → Output: ["apple", "banana", "cherry"]

1 Filter employees older than 25 from a list of tuples (name, age).
Input: [("Rohit", 22), ("Rahul", 26), ("Raj", 30)]
Output: [("Rahul", 26), ("Raj", 30)]'''

# l=[1, 2, 3, 4, 5, 6]
# res=list(filter(lambda x:x%2==0,l))
# print(res)

# l=[10, 15, 20, 25, 30]
# res=list(filter(lambda x:x%2!=0,l))
# print(res)

# l= [10, 60, 45, 70, 30]
# res=list(filter(lambda x:x>50,l))
# print(res)

# l=["apple", "bat", "ball", "hi"]
# res=list(filter(lambda x:len(x)>=4,l))
# print(res)

# l=[-2, 0, 5, 9, -7, 3]
# res=list(filter(lambda x:x>0,l))
# print(res)

# l=["apple", "banana", "avocado", "cherry"]
# res=list(filter(lambda x:x[0]=='a',l))
# print(res)

# l= ["madam", "python", "level", "wow", "cat"]
# res=list(filter(lambda x:x[::-1]==x,l))
# print(res)

# l=['a', 'b', 'e', 'i', 'o', 'p', 'u']
# res=list(filter(lambda x:x in "aeiou",l))
# print(res)

# l=[10, 15, 30, 42, 60, 70]
# res=list(filter(lambda x:x%3==0 and x%5==0,l))
# print(res)

# l=["Rahul", "Raj", "Python", "Code"]
# res=list(filter(lambda x:'a'in x,l))
# print(res)

# l=[2, 4, 6, 8, 10]
# res=list(filter(lambda x:x**2>50,l))
# print(res)

# l=["running", "play", "eating", "dance"]
# res=list(filter(lambda x:x.endswith("ing"),l))
# print(res)

# l= [1, "apple", 3.5, "banana", True, "cherry"]
# res=list(filter(lambda x:isinstance(x, str),l))
# print(res)

# l=[("Rohit", 22), ("Rahul", 26), ("Raj", 30)]
# res=list(filter(lambda x:x[1]>25,l))
# print(res) (brilliant)

'''even'''
# l=[1,2,3,4,5,6,7,8,9,10]
# res=list(filter(lambda x:x%2==0,l))
# print(res)

'''50 se uppar right pe neeche left pe'''
# l=[23,56,4,3,7,8,5,67,89,67,45,21,88,99,34,100]
# res=list(filter(lambda x:x<50,l))
# res2=list(filter(lambda x:x>50,l))
# out=res+res2
# print(out)

'''21.	Keep numbers greater than average '''
# from functools import reduce
# l=[2, 4, 6, 8, 10]
# res=reduce(lambda x,y:x+y,l)
# avg=res/5
# res2=list(filter(lambda x:x>int(avg),l))
# print(res2)

'''23.	Keep numbers equal to a given value '''
# n=int(input("enter your number "))
# l=[1,2,34,8,9,8,7,4,8]
# res=list(filter(lambda x:x==n,l))
# print(res)

'''24.	Remove duplicates (hint: condition logic) '''
# l=[2,3,4,6,7,6,9,8,0,8]
# seen=set()
# res=list(filter(lambda x:not(x in seen or seen.add(x)),l))
# print(res)

'''prime number'''
# l=[1,2,3,4,5,6,7]
# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     return count==2
# res=list(filter(lambda x:prime(x),l))
# print(res)

'''perfect'''
# l=[1,2,3,4,5,6,7]
# def perfect(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     return count>2
# res=list(filter(lambda x:perfect(x),l))
# print(res)

'''26.	Keep perfect squares '''
# l=[23,25,78,16]
# def root(n):
#     y=n**0.5
#     return y.is_integer()
# res=list(filter(lambda x:root(x),l))
# print(res)

'''11.	Keep strings with length > 3 '''
# l=['ok','hello','piyush','hi']
# res=list(filter(lambda x:len(x)>3,l))
# print(res)

'''27.	Keep numbers whose square > 50 '''
# l=[23,56,4,3,7,8,5,67,89,67,45,21,88,99,34,100]
# res=list(filter(lambda x:x**2>50,l))
# print(res)

# '''28.	Keep numbers with even digits '''
# l=[12, 24, 135, 68, 91, 246]
# def even(n):
#     while n>0:
#         digit=n%10
#         if digit%2!=0:
#             return False
#         n=n//10
#     return True
# res=list(filter(lambda x:even(x),l))
# print(res)        

'''29.	Keep numbers with odd digits '''
# l=[12, 24, 135, 68, 91, 246]
# def odd(n):
#     while n>0:
#         digit=n%10
#         if digit%2==0:
#             return False
#         n=n//10
#     return True
# res=list(filter(lambda x:odd(x),l))
# print(res)
    
'''30.	Keep numbers ending in 5 '''
# l=[23,135,64,785,55,68,95,105]
# res=list(filter(lambda x:x%10==5,l))
# print(res)

'''31.	Keep even numbers > 10 '''
# l=[5, 8, 10, 12, 15, 18]
# res=list(filter(lambda x:x%2==0 and x>10,l))
# print(res)

'''32.	Keep odd numbers < 20 '''
# l=[3,12,55,24,7,53]
# res=list(filter(lambda x:x%2!=0 and x<20,l))
# print(res)

'''35.	Keep numbers greater than 10 but less than 100 '''
# l=[2,78,5,44,3,98,1,99,567]
# res=list(filter(lambda x:x>10 and x<100,l))
# print(res)

'''36.	Keep strings starting with 'a' and length > 3 '''
# l=['apple','hi','ok','aeroplane','bus','cat','killer','ai']
# res=list(filter(lambda x:x[0]=='a' and len(x)>3,l))
# print(res)

'''37.	Keep strings ending with 'y' or 'e' '''
# l=["apple", "sky", "banana", "blue", "try", "cat", "happy"]
# res=list(filter(lambda x:x[-1]=='y' or x[-1]=='e',l))
# print(res)

'''38.	Keep numbers that are multiples of 4 but not 8 '''
# l=[4, 8, 12, 16, 20, 24, 28, 32]
# res=list(filter(lambda x:x%4==0 and x%8!=0,l))
# print(res)

'''39.	Keep strings containing both 'a' and 'e' '''
# l=['apple','aeroplane','bat','ship','heart']
# res=list(filter(lambda x:'a'and 'e'in x,l))
# print(res)

'''40.	Keep numbers whose cube < 1000 '''
# l=[2, 5, 7, 9, 10, 3, 4]
# res=list(filter(lambda x:x**3<1000,l))
# print(res)

'''41.	Keep pairs where sum > 10 '''
# l=[(2, 5), (6, 7), (3, 4), (10, 2), (1, 8)]
# res=list(filter(lambda x:x[0]+x[1]>10,l))
# print(res)

'''42.	Keep pairs where first > second '''
# l=[(2, 5), (6, 7), (3, 4), (10, 2), (1, 8)]
# res=list(filter(lambda x:x[0]>x[1],l))
# print(res)

'''43.	Keep pairs where both numbers are even '''
# l=[(2, 4), (3, 6), (8, 10), (5, 7), (12, 14), (9, 2)]
# res=list(filter(lambda x:x[0]%2==0 and x[1]%2==0,l))
# print(res)

'''71.	Keep numbers whose factorial < 100 '''
# l=[2,4,5,1,6,8,9,45]
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# res=list(filter(lambda x:factorial(x)<100,l))
# print(res)

'''77.	Keep strings where first and last character same '''
# l=['alla','helllo','dad','parrot']
# res=list(filter(lambda x:x[0]==x[-1],l))
# print(res)

'''81.	Keep elements where sum of two lists > 10 '''
# l=[3,6,7,34,65,9]
# l2=[23,4,1,7,0,1]
# pair=list(zip(l,l2))
# res=list(filter(lambda x:x[0]+x[1]>10,pair))
# print(res)

'''83.	Keep elements where product is even '''
# l=[(2, 3), (4, 5), (7, 9), (6, 2), (3, 3), (8, 1)]
# res=list(filter(lambda x:x[0]*x[1]%2==0,l))
# print(res)

'''84.	Keep pairs where one is even and other odd '''
# l=[(2, 3), (4, 6), (7, 8), (9, 5), (10, 11), (12, 14)]
# res = list(filter(lambda x: (x[0] % 2 == 0 and x[1] % 2 != 0) or (x[0] % 2 != 0 and x[1] % 2 == 0), l))
# print(res)

'''85.	Keep pairs where both are multiples of 3 '''
# l=[(3, 6), (4, 9), (9, 12), (5, 7), (15, 18), (8, 3)]
# res=list(filter(lambda x:x[0]%3==0 and x[1]%3==0,l))
# print(res)

'''86.	Keep elements where x > y '''
# l=[(5, 3), (2, 4), (10, 7), (6, 6), (9, 1), (3, 8)]
# res=list(filter(lambda x: x[0]>x[1],l))
# print(res)

'''89.	Keep elements where x + y is odd '''
# l=[(2, 3), (4, 6), (7, 8), (5, 5), (9, 2), (10, 11)]
# res=list(filter(lambda x:(x[0]+x[1])%2!=0,l))
# print(res)

'''91.	Keep numbers whose binary has more 1s '''
# l=[3, 5, 7, 8, 10, 15, 2, 9]
# res=list(filter(lambda x:bin(x).count('1')>bin(x).count('0')-1,l))
# print(res)

'''92.	Keep numbers with unique digits '''
# l=[121, 234, 455, 789, 112, 908, 333]
# def unique(n):
#     y=n
#     rem=n
#     while n>0:
#         digit=n%10
#         x=rem
#         count=0
#         while x>0:
#             d2=x%10
#             if digit==d2:
#                 count=count+1
#             x=x//10
#         if count>1:
#            return False
#         n=n//10
#     return True
# res=list(filter(lambda x:unique(x),l))
# print(res)


'''93.	Keep numbers with repeated digits '''
# l=[121, 234, 455, 789, 112, 908, 333]
# def repeat(n):
#     rem=n
#     while n>0:
#         digit=n%10
#         x=rem
#         count=0
#         while x>0:
#             d2=x%10
#             if digit==d2:
#                 count=count+1
#             x=x//10
#         if count>1:
#             return True
#         n=n//10
#     return False
# res=list(filter(lambda x:repeat(x),l))
# print(res)

'''94.	Keep numbers whose sum of digits is even '''
# l=[121, 234, 455, 789, 112, 908, 333]
# def even_sum(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n=n//10
#     if sum%2==0:
#         return True
# res=list(filter(lambda x:even_sum(x),l))
# print(res)

'''96.	Keep strings with alternating characters '''
# l = ["abab", "aabb", "abc", "aab", "xyz", "xxy", "1212", "1122"]
# def alternate(n):
#     i=0
#     while i<len(n)-1:
#         if n[i]==n[i+1]:
#             return False
#         i=i+1
#     return True
# res=list(filter(lambda x:alternate(x),l))
# print(res)

'''97.	Keep strings with all unique characters '''
# l=["abab", "aabb", "abc", "aab", "xyz", "xxy", "1212", "1122"]
# def unique(n):
#     i=0
#     while i<len(n):
#         count=0
#         j=0
#         while j<len(n):
#             if n[i]==n[j]:
#                 count=count+1
#             j=j+1
#         if count>1:
#             return False
#         i=i+1
#         return True
# res=list(filter(lambda x:unique(x),l))
# print(res)
  
'''98.	Keep strings with at least one uppercase '''
# l = ["abc", "Abc", "xyz", "HELLO", "test", "PyThon", "java"]
# def upper(n):
#     i=0
#     while i<len(n):
#        if n[i].isupper():
#            return True
#        i=i+1
#     return False
# res=list(filter(lambda x:upper(x),l))
# print(res)

'''99.	Keep strings with no spaces '''
# l=["abc", "hello world", "python", "data science", "AI", "no space", "code"]
# def space(n):
#     i=0
#     while i<len(n):
#         if n[i]==' ':
#             return False
#         i=i+1
#     return True
# res=list(filter(lambda x:space(x),l))
# print(res)

'''100.	Keep strings with exactly 3 characters '''
# l=["abc", "Abc", "xyz", "HELLO", "test", "PyThon", "java"]
# res=list(filter(lambda x:len(x)==3,l))
# print(res)

'''seprate 0 on right side and digits on left side from a given list'''
# l=[1,0,2,0,3,0,4,0,5,0]
# r1=list(filter(lambda x:x!=0,l))
# r2=list(filter(lambda x:x==0,l))
# res=r1+r2
# print(res)

'''seprate even on left side and odd on right side from a given list '''
# l=[1,2,3,4,5,6,7,8,9,10]
# r1=list(filter(lambda x:x%2==0,l))
# r2=list(filter(lambda x:x%2!=0,l))
# res=r1+r2
# print(res)



# --------------------------------------------------------------------------------------------------------
                                       #  reduce
'''1 Find the sum of all numbers in a list using reduce().
Input: [1, 2, 3, 4, 5] → Output: 15

2 Find the product of all numbers in a list.
Input: [1, 2, 3, 4] → Output: 24

3 Find the largest number in a list.
Input: [5, 3, 8, 6, 2] → Output: 8

4 Find the smallest number in a list.
Input: [5, 3, 8, 6, 2] → Output: 2

5 Find the sum of squares of all numbers.
Input: [1, 2, 3, 4] → Output: 30

6 Find the sum of even numbers in a list.
Input: [1, 2, 3, 4, 5, 6] → Output: 12

7 Count how many elements are positive numbers.
Input: [-2, 5, -7, 9, 3, -1] → Output: 3

8 Find factorial of a number using reduce().
Input: 5 → Output: 120

9 Find the longest word in a list using reduce().
Input: ["apple", "banana", "cherry", "kiwi"] → Output: "banana"'''

# from functools import reduce
# l=[1, 2, 3, 4, 5]
# res=reduce(lambda x,y:x+y,l)
# print(res)

# l= [1, 2, 3, 4]
# res=reduce(lambda x,y:x*y,l)
# print(res)

# l=[5, 3, 8, 6, 2]
# res=reduce(lambda x,y:x if x>y else y,l)
# print(res)

# l=[5, 3, 8, 6, 2]
# res=reduce(lambda x,y:x if x<y else y,l)
# print(res)

# l=[1, 2, 3, 4]
# res1=list(map(lambda x:x**2,l))
# l2=res1
# res2=reduce(lambda x,y:x+y,l2)
# print(res2)

# l=[1, 2, 3, 4, 5, 6]
# res=reduce(lambda x,y:x+y,filter(lambda x:x%2==0,l))
# print(res)

# l=[-2, 5, -7, 9, 3, -1]
# count = reduce(lambda acc, x: acc + (1 if x > 0 else 0), l, 0)
# print(count)

# n=int(input("enter your number "))
# res=reduce(lambda x,y:x*y,range(1,n+1))
# print(res)

# l=["apple", "banana", "cherry", "kiwi"]
# res=reduce(lambda x,y:x if len(x)>=len(y)else y,l)
# print(res)

'''5.	Count total elements '''
# l=[4,5,6,3,2,5,6]
# count=reduce(lambda acc,x:acc+1,l,0)
# print(count)

'''6.	Count even numbers '''
# l=[4,5,6,3,2,5,6]
# count=reduce(lambda acc,x:acc+1 if x%2==0 else acc,l,0)
# print(count)

'''count odd'''
# l=[4,5,6,3,2,5,6]
# count=reduce(lambda acc,x:acc+1 if x%2!=0 else acc,l,0 )
# print(count)

'''8.	Sum of even numbers '''
# l=[4,5,6,3,2,5,6]
# sum=reduce(lambda acc,x:x+acc if x%2==0 else acc,l,0 )
# print(sum)

'''10.	Multiply all even numbers ''' 
# l=[4,5,6,3,2,5,6]
# mul=reduce(lambda acc,x:acc*x if x%2==0 else acc,l)
# print(mul)

# '''11.	Sum of squares of numbers '''
# l=[4,5,6,3,2,5,6]
# sum=reduce(lambda acc,x:acc+x**2,l,0)
# print(sum)

from functools import reduce 
'''15.	Sum of digits of all numbers '''
# l=[12, 34, 5, 101 ,78]
# def sumi(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n=n//10
#     return sum
# res=list(map(lambda x:sumi(x),l))
# l2=res
# ans=reduce(lambda x,y:x+y,l2)
# print(ans)

'''18.	Sum numbers divisible by 3 '''
# l=[3, 5, 6, 9, 10, 12, 14, 15]
# res=reduce(lambda acc,x:acc+x if x%3==0 else acc,l)
# print(res)

'''16.	Count numbers greater than 10 '''
# l=[3, 5, 6, 9, 10, 12, 14, 15]
# count=reduce(lambda acc,x:acc+1 if x>10 else acc,l,0)
# print(count)

'''18.	Sum numbers divisible by 3 '''
# l=[3, 5, 6, 9, 10, 12, 14, 15]
# res=reduce(lambda acc,x:acc+x if x%3==0 else acc,l)
# print(res)

'''19.	Product of numbers divisible by 5 '''
# l=[3, 5, 6, 9, 10, 12, 14, 15]
# res=reduce(lambda acc,x:acc*x if x%5==0 else acc,l)
# print(res)
