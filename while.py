# While loop 
# You have previously taken the information of loops and you 
# also know conditional statements it is going to be easy for 
# you to understand this now
# The while loop repeats a block of code as long as a condition 
# is True. It is useful when the number of iterations is unknown 
# before execution
# So there is not much that you have to understand about 
# while loop it also have break, continue and else.
# Now you just have to find out which loop will be used on 
# what questions. 
# a=1
# while a<=30:
#     print(a)
#     a=a+1
'''ques of while loop'''
# a=int(input("enter your number"))
# rev=0
# # while a>0:
# #     print(a%10)
# #     a=a//10
# while a>0:
#     digit=a%10
#     rev=rev*10+digit
#     a=a//10
# print(rev)

# n=int(input("enter your number "))
# x=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if rev==x:
#     print('pallindrome')
# else:
#     print('not pallindrome')

'''created a random number guessing game with python.'''
import random
num=random.randint(1,100)
tries=0
while True:
    GUESS=int(input("please guess your number between 1 to 100:- "))
    if GUESS==num:
        tries+=1
        print(f"you are right you guessed the number in {tries} tries")
        break
    elif num>GUESS:
        tries+=1
        print("go a liitle higher")
    elif num<GUESS:
        tries+=1
        print("go a little lower")
    else:
        tries+=1
        print("sorry you are wrong")

# infinite
# while True:
#     print("hello") ctrl++c to break terminal

# finite
# n=int(input("enter "))
# x=1
# while x<=n:
#     print(x)
#     x=x+1

#natural numbers from 1 to 10 using while loop
'''to remove plus from last'''
# n=int(input("enter "))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     i=i+1
# print(sum)

#product(factorial)
# n=int(input("enter "))
# i=1
# product=1
# while i<=n:
#     product=product*i
#     if i<n:
#         print(i,end="*")
#     else:
#         print(i,end="=")
#     i=i+1
# print(product)

# n=int(input("enter your number "))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     if i<n:
#         print(2*i,end="+")
#     else:
#         print(2*i,end="=")
#     i=i+1
# print(sum)

# a=10
# b=20
# print(a,b,sep=",")


'''reverse'''
# n=int(input("enter your number"))
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)

'''pallindrome'''
# n=int(input("enter your number"))
# x=n
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if rev==x:
#     print(f"given no {x} is pallindrome")
# else:
#     print(f"given no {x} is not a pallindrome")

'''armstrong'''
# n=int(input("enter your number"))
# y=x=n
# td=0
# while n>0:
#     td=td+1
#     n=n//10
# sum=0
# while x>0:
#     ld=x%10
#     sum=sum+ld**td
#     x=x//10
# if y==sum:
#     print(f"the given number {y} is armstrong ")
# else:
#     print(f"the given number {y} is not armstrong")

'''square pattern'''
# n=int(input("enter "))
# i=1
# while i<=n:
#     print("*"*n)
#     i=i+1

'''triangle pattern 1'''
# n=int(input("enter "))
# i=1
# while i<=n:
#     print("*"*i+" "*(n-i))
#     i=i+1

'''triangle pattern 2'''
# n=int(input("enter "))
# i=1
# while i<=n:
#     print(" "*(n-i)+"*"*i)
#     i=i+1

'''triangle pattern 3'''
# n=5
# i=1
# while i<=n:
#     print(" "*(n-i)+'* '*i)
#     i=i+1

'''triangle pattern 4'''
# n=5
# i=0
# while i<n:
#     print("*"*(n-i)+' '*i)
#     i=i+1

'''triangle pattern 5'''
# n=5
# i=0
# while i<n:
#     print(i*' '+(n-i)*'*')
#     print(" "*i+"*"*(n-i))
#     i=i+1

'''triangle pattern 6'''
# n=5
# i=0
# while i<n:
#     print(i*' '+(n-i)*'* ')
#     i=i+1

'''triangle pattern 7'''
# n=5
# i=0
# while i<=n:
#     print('*'*i+" "*(n-i))
#     i=i+1
# i=i-2
# while i>0:
#     print('*'*i+" "*(n-i))
#     i=i-1

'''triangle pattern 8'''
# n=5
# i=0
# while i<=n:
#     print(' '*(n-i)+"*"*i)
#     i=i+1
# i=i-2
# while i>0:
#     print(' '*(n-i)+"*"*i)
 
#     i=i-1

'''triangle pattern 9'''
# n=5
# i=0
# while i<=n:
#     print(' '*(n-i)+"* "*i)
#     i=i+1
# i=i-2
# while i>0:
#     print(' '*(n-i)+"* "*i)
 
#     i=i-1

''''''
    







