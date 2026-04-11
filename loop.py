# '''Loops in python
# Loops in Python allow us to execute a block of code multiple 
# times without rewriting it
# Ok lets do one thing go to your VS code and print “hello 
# world” 100 times
# Manually printing will take 100 code lines to print it. but using 
# loops we need only 2 lines to print 100 times, thats the 
# power of loops'''

# '''in loops we run our code multiple times
# types of loop there are 2 types of loops in python
# 1-for loop
# 2-while loop
# both work multiple times for execution (kisi bhi task ko baar baar perform karane ko bolte hai loop)'''
# #for loop
# '''for loop works on number basis,range basis task example-python can you remove only 4 items from box yaha pe usko pata hai ki kitne items he has to remove''' 
# #while loop
# '''it works on condition basis to task example - remove all the elements from this box until the box is empty the 2 one is condition yaha pe condition  hai ki until box is empty jab tak loop chalao'''

# #for loop
# # range()a range func accepts 3 things sss-start,stop,steps we use it in for loop
# '''for&while loop is a control flow statement so we have to follow indentations'''
# # a=range(1,20,2) # it stops 1 step before
# # for i in a:
# #     print(i)
# # for i in range (21):
# #     print(i)
# # range has defualt starting and ending points 0,1
# #in is something me ksisi cheez ke andar jana chahta hu
# '''i is a vartiable which is iterated'''
# #ques
# # for i in range(16,0,-1):
# #     print(i)

# # for i in range(20,51,1):
# #     print(i)

# # for i in range (-3,-16,-1):
# #     print(i)

# '''table of 5'''

# # for i in range (5,51,5):
# #     print(i)

# '''print table take input from user'''

# # n=int(input("enter your table "))
# # for i in range(n,(n*10)+1,n):
# #     print(i)

# '''working for loop for strings'''
# '''Loops for strings
# Loops for strings work slightly differently. You can iterate 
# through a string in two ways
# Using index values
# Iterating directly over the string
# Iterating using the index values, Now we know that index 
# values are numbers and for numbers we again have to use 
# range function.'''
# a="sheriyans" #in this i know it has index values 0-8 indexing values
# for i in range (0,9):
#     print(a[i]) # it prints num
#     """we applied indexing []-> sunscript operator
#     but will i count everytime how many words are there answer is no so we use length func"""
# b="hello sir my name is piyush moolchandani"
# for i in range(len(b)):
#     print(b[i])
# #len func already has plus one 
# '''like len(sher) comes out 4 beacuse it is counted from 1 only and range works
# 1 step before indexing wise'''
# # this is for using indexing values now we will se using
# '''iterating directly over the string'''

# a="sheryians is cool" # not using indexing value in this but we use char values directly in this
# # means we are not accesing indexing in it we directly accessing char in this
# for i in a:
#     print(i)

# '''Break continue else
# Things written above are very important for loops
# Lets say you have this race track 
# and you have to complete 20 laps 
# but when you were completing the 
# 16th laps and it started raining now
# you cannot complete the rounds
# The above example simulate the example of your break 
# statement.
# The break statement in Python is used to exit a loop 
# prematurely when a certain condition is met. Once break is 
# encountered, the loop stops immediately, and control moves 
# to the next statement after the loop
# The Continue statement skips one of the iteration and rest of 
# the iterations will run for understanding lets say you will not 
# run the 16th lap but all other lap will be there.
# You have seen the else statement used with if, but it can also 
# be used with loops. When else is used with a loop, it only 
# executes if the loop completes without encountering a break 
# statement. If break is executed, the else block will not run.'''

# # for i in range (1,20):
# #     if i==15:
# #         continue
# #     else:
# #         print(i)

# '''for loop ques'''
# # n=int(input("enter your number "))
# # for i in range(n):
# #     print("hello world")

# # n=int(input("enter your number "))
# # for i in range(1,n+1):
# #     print(i)

# # n=int(input("enter your number "))
# # for i in range(n,0,-1):
# #     print(i)

# # n=int(input("enter your number "))
# # for i in range (1,11):
# #     print(f"{n} * {i} = {n*i}")

# # n=int(input("enter your number "))
# # sum=0
# # for i in range(1,n+1):
# #     sum=sum+i
# # print(sum)

# # n=int(input("enter your number "))
# # fact=1
# # for i in range (1,n+1):
# #     fact=fact*i
# # print(fact)

# # n=int(input("enter your number "))
# # even=0
# # odd=0
# # for i in range(1,n+1):
# #    if i%2==0:
# #        print(i)
# #        even=even+i
# #    else:
# #        odd=odd+i
# # print(even,odd)

# # n=int(input("enter your number "))
# # for i in range (1,n+1):
# #     if n%i==0:
# #         print(f"the factors are {i}")

# # n=int(input("enter your number"))
# # sum=0
# # for i in range (1,n):
# #     if n%i==0:
# #         sum=sum+i
# # if sum==n:
# #     print("the number you entered is a perfect number")
# # else:
# #     print("it's not a perfect number")

# # n=int(input("enter your number"))
# # count=0
# # for i in range (1,n+1):
# #     if n%i==0:
# #         count=count+1
# # if count==2:
# #     print("prime")
# # else:
# #     print("not prime")

# # n="python"
# # m=""
# # for i in range(len(n)-1,-1,-1):
# #   m=m+n[i]
# # print(m)

# for i in range(1,11,1):
#     print(i)

# for i in range (10,0,-1):
#     print(i)
    
# for i in range (2,21,2):
#     print(i)

# for i in range (1,21,1):
#     if i%2==0:
#         print(i)

# for i in range (1,21,2):
#     print(i)

# for i in range (1,21):
#     if i%2!=0:
#         print(i)

# for i in range(5,16,1):
#     print(i)

# n=int(input("enter your table "))
# for i in range (n,(n*10)+1,n):
#     print(i)

# for i in range (1,101,5):
#     print(i)

# for i in range(1,31):
#     if i%3==0:
#         print(i)
        

# count=0
# for i in range(1,100):
#     count=count+1
# print(i)
 
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)

# count=0
# for i in range(1,101):
#     if i%2==0:
#          count=count+1
# print(count)

# li=[2,6,10,5,9,45,66,7]
# count=0
# for i in li:
#     if i%2==0:
#         count=count+1
# print(count)
   
# n=int(input("enter a number "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# sum=0
# for i in range(1,11):
#     sq=i**2
#     sum=sum+sq
# print(sum)

# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum/10)

# ==================================================
'''list ques'''
# li=[2,4,7,8,93,5]
# for i in li:
#     print(i)

# li=[2,4,7,8,93,5]
# sum=0
# for i in li:
#     sum=sum+i
# print(sum)

# li=[2,4,7,8,93,5]
# max=4
# for i in li:
#     if i>max:
#         max=i
# print(max)

# li = [
#     12, 45, 3, 89, 23, 67, 1, 90, 34, 56,
#     78, 5, 102, 9, 43, 65, 87, 210, 14, 6,
#     98, 76, 54, 32, 11, 150, 199, 8, 27, 61,
#     73, 4, 16, 84, 120, 39, 92, 7, 18, 55,
#     300, 25, 66, 41, 88, 10, 170, 2, 95, 400
# ]

# max=li[0]
# min=li[0]
# for i in li:
#     if i>max:
#         max=i
# print(max)                      '''without function'''

# for i in li:
#     if i<min:
#         min=i
# print(min)

# def max():
#     max=li[0]
#     for i in li:
#         if i>max:                 '''with function'''
#             max=i
#     return max
# print(max())

# def r_li():
#    count=0
#    for i in li:
#          count=count+1
#    return count
# print(r_li())

'''factorial'''

# fact=1
# n=int(input("enter your number "))
# for i in range (1,n+1):
#     fact=fact*i
# print(fact)

'''Print only positive numbers from a list.'''
# li=[-45,67,-5,7,8,4,-6,0]
# for i in li:
#     if i>0:
#         print(i)

'''Create a new list containing only even numbers from an existing list.'''
# li=[2,7,14,5,89,44,6,10,11]
# li2=[]
# for i in li:
#     if i%2==0:
#      li2.append(i)
# print(li2)good

'''Print list elements along with their index.'''
# li=[2,7,14,5,89,44,6,10,11]
# count=0
# for i in li:
#     print(count,"-",i)
#     count=count+1












    
    



    

    
   
        

    
    
  
    
        
   
        
    
    
    
    
        


