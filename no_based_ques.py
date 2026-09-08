''' 1.	Reverse a number  '''
# n=int(input("enter your number "))
# rev = 0
# while n>0:
#     digit = n%10
#     rev = rev*10 + digit
#     n = n//10
# print(rev)

'''3.	Fibonacci '''
# n = int(input("enter your number "))
# fi = 0
# se = 1
# for i in range(n):
#     nx = fi+se
#     print(fi,end=',')
#     fi=se
#     se=nx

'''4.	Factorial '''
# n = int(input("enter your number "))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(f'the factorial of {n} is {fact}')

'''5.	Prime number '''
# n = int(input("enter your number "))
# pr_count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         pr_count+=1
# if pr_count==2:
#     print('prime')
# else:
#     print('Not prime')

'''6.	Armstrong number '''
# n = int(input("enter your number "))
# ch = n
# power = len(str(n))
# digit_sum=0
# while n>0:
#     digit = n%10
#     digit_sum+=digit**power
#     n=n//10
# if digit_sum == ch:
#     print('Armstrong')
# else:
#     print('Not Armstrong')

'''9.	GCD '''
# num1 = int(input("enter your number "))
# num2 = int(input("enter your number "))
# fact1 = []
# fact2 = []
# for i in range(1,num1+1):
#     if num1%i==0:
#         fact1.append(i)
# for j in range(1,num2+1):
#     if num2%j==0:
#         fact2.append(j)
# common = []
# for x in fact1:
#     if x in fact2:
#         common.append(x)
# z = max(common)
# print("the gcd is", z)

'''euclidiean algorithm'''
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# while num2!=0:
#     num1,num2 = num2,num1%num2
# print("the gcd is", num1)

'''11.	Perfect number '''
# n = int(input("enter your number: "))
# total = 0
# for i in range(1,n):
#     if n%i==0:
#         total+=i
# if total == n:
#     print('perfect number')
# else:
#     print('not perfect number ')

'''12.	Happy number '''
# n = int(input("Enter your number: "))
# seen = set()
# while n!=1:
#     if n in seen:
#         break
#     seen.add(n)
#     digit_sum = 0
#     while n>0:
#         digit = n%10
#         digit_sum+=digit**2
#         n=n//10
#     n = digit_sum
# if n == 1:
#     print(" happy number ")
# else:
#     print(" not happy number ")

'''13.	Swap two numbers '''
# a = 4
# b = 9
# a,b=b,a
# print(  a,b)
'''with third variable'''
# a = 4
# b = 9
# temp = a
# a=b
# b=temp
# print(a,b)

'''14.	Decimal ↔ binary basic conversion '''
# n = 10
# binary = ""
# while n>0:
#     remain = n%2
#     n = n//2
#     binary = str(remain)+binary
# print(binary)

    








