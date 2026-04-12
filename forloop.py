'''
Print numbers from 1 to 50 using a for loop.
Print numbers from 50 to 1 using a for loop.
Print all numbers divisible by 4 between 1 and 40.
Print all numbers divisible by 7 between 1 and 70.
Print numbers from 1 to 30 except multiples of 5.
Print the first 20 natural numbers.
Print numbers from 10 to 100 with a step of 10.
Print numbers between 1 and 100 that end with digit 0.
Print numbers between 1 and 50 that are divisible by both 2 and 5.
Print numbers between 1 and 100 that are odd.
'''
# for i in range(1,51):
#     print(i)

# for i in range(50,0,-1):
#     print(i)

# for i in range(1,41):
#     if i%4==0:
#         print(i)

# for i in range(7,71,7):
#     print(i)

# for i in range(1,31):
#     if i%5!=0:
#         print(i)

# for i in range(1,21):
#     print(i)

# for i in range(10,101,10):
#     print(i)

# for i in range(1,101):
#     if i%10==0:
#         print(i)

# for i in range(1,51):
#     if i%2==0 and i%5==0:
#         print(i)

# for i in range(1,101):
#     if i%2!=0:
#         print(i)

'''Find the sum of numbers from 1 to 20.
Find the sum of numbers from 10 to 50.
Find the sum of numbers divisible by 3 between 1 and 30.
Find the sum of numbers divisible by 5 between 1 and 50.
Count how many numbers are divisible by 3 between 1 and 100.
Count how many numbers are divisible by 5 between 1 and 100.
Count how many odd numbers are between 1 and 50.
Count how many even numbers are between 1 and 50.
Find the sum of numbers between 1 and 100 that are even.
Find the sum of numbers between 1 and 100 that are odd.
Find the sum of squares of numbers from 1 to 5.
Find the sum of cubes of numbers from 1 to 5.
Find the average of numbers from 1 to 20.
Print the running sum from 1 to 20.
Print the running sum of even numbers from 1 to 20.
'''
'''composite number'''
# n=int(input("enter your number"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1

# if count>2:
#     print("the number you enter is composite")
# else:
#     print("the number is not composite")very good 1 loop ques made by myself

# sum=0
# for i in range(1,21):
#     sum=sum+i
# print(sum)

# sum=0
# for i in range(1,31):
#     
#     if i%3==0:
#         sum=sum+i
# print(sum)

# sum=0
# for i in range(10,51):
#    sum=sum+i
# print(sum)

# sum=0
# for i in range(1,51):
#     if i%5==0:
#         sum=sum+i
# print(sum)

# count=0
# for i in range(1,101):
#     if i%3==0:
#         count=count+1
# print(count)

# count=0
# for i in range(1,101):
#     if i%5==0:
#         count=count+1
# print(count)


# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum=sum+i
# print(sum)

# sum=0
# for i in range(1,6):
#     sq=i**2
#     sum=sum+sq
# print(sum)


# sum=0
# for i in range(1,6):
#     cube=i**3
#     sum=sum+cube
# print(cube)

# sum=0
# for i in range(1,21):
#     sum=sum+i
# print(sum/10)

'''running sum in a list'''
# sum=0
# li=[]
# for i in range(1,21):
#     sum=sum+i
#     li.append(sum)
# print(li)

'''even running sum in a list'''
# sum=0
# li=[]
# for i in range(1,21):
#     if i%2==0:
#         sum=sum+i
#         li.append(sum)
# print(li)


'''Print all elements of a list in reverse order.

Count how many elements are in a list using a for loop.

Count how many even numbers are in a list.

Count how many odd numbers are in a list.

Find the sum of even numbers in a list.

Find the sum of odd numbers in a list.

Print numbers in a list that are greater than 10.

Print numbers in a list that are less than 0.

Find the average of elements in a list.

Find the difference between the largest and smallest number in a list.

Print only numbers divisible by 3 from a list.

Print only numbers divisible by 5 from a list.

Print each element of a list multiplied by 2.

Create a new list containing squares of elements of a list.

Create a new list containing odd numbers from a list.

Count how many positive numbers are in a list.

Count how many negative numbers are in a list.

Print list elements at even index positions.

Print list elements at odd index positions.

Print index and element in the format: Index: value.'''


# li=[2,4,6,8,9]
# li2=[]
# for i in range(len(li)-1,-1,-1):
#     li2.append(li[i])
# print(li2)

# count=0
# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     count=count+1
# print(count)

# count=0
# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     if i%2==0:
#         count=count+1
# print(count)

# count=0
# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     if i%2!=0:
#         count=count+1
# print(count)

# sum=0
# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     if i%2==0:
#         sum=sum+i
# print(sum)

# sum=0
# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     if i%2!=0:
#         sum=sum+i
# print(sum)


# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     if i>10:
#         print(i)

# li = [2, 7, 14, 5, 89, 44, 6, 10, 11,-11]
# for i in li:
#     if i<0:
#         print(i)

# sum=0
# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     sum=sum+i
# print(sum/9)


# Find the difference between the largest and smallest number in a list.
# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# large=li[0]
# small=li[0]
# for i in li:
#     if i>large:
#         large=i
# if i<small:
#     small=i
# print(f"difference between the largest and smallest number in a list is {large-small}")


# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     if i%3==0:
#         print(i)

# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in li:
#     mul=i*2
#     print(mul)


# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# li2=[]
# for i in li:
#     sq=i**2
#     li2.append(sq)
# print(li2)


# li = [2, 7, 14, 5, 89, 44, 6, 10, 11]
# for i in range(len(li)):
#     if i % 2 == 0:
#         print(li[i])


'''check whether a number is prime.
Print all prime numbers between 1 and 100.
Check whether a number is perfect.
Print all factors of a given number.
Count how many factors a number has.
Check whether a number is Armstrong.
Print all Armstrong numbers between 1 and 500.
Reverse a number using a loop.
Find the sum of digits of a number.
Check whether a number is a palindrome.
# Print Fibonacci series up to n terms.(left for doing afterwards)
Find the largest digit in a number.
Count the number of digits in a number.
Print multiplication tables from 1 to 10.
Find HCF of two numbers using loop logic.'''

'''prime'''
# count=0
# n=int(input("enter your number"))
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("the number you enter is prime")
# else:
#     print("the number is not prime")

'''prime numbers between 1 to 100'''
# for num in range(2, 101):   
#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count + 1

#     if count == 2:
#         print(num)


'''perfect number'''
# sum=0
# n=int(input("enter your number "))
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("The number you entered is a perfect number")
# else:
#     print("The number is not a perfect number")

'''factors of a given number'''

# n=int(input("enter your number "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

'''count how many factors number have'''

# n=int(input("enter your number "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# print(count)

'''sum '''

# n=input("enter your number ")
# sum=0
# for  i in n:
#     sum=sum+int(i)
# print(sum)

'''armstrong'''
# n=input("enter your number ")
# power=len(n)
# sum=0
# for i in n:
#     sum=sum+int(i)**power
# if sum==int(n):
#     print("The number you entered is a armstrong number")
# else:
#     print("The number is not armstrong number")

'''armstrong between 1 to 500'''
# for num in range(1,501):
#     sum=0
#     power=len(str(num))
    
#     for i in str(num):
#         sum=sum+int(i)**power

#         if sum==num:
#             print(num)


'''reverse a number '''
# a=int(input("enter your number "))
# rev=0
# for i in range(len(str(a))):
#     digit=a%10
#     rev=rev*10+digit
#     a=a//10
# print(rev)

'''pallindrome'''

# n=int(input("enter your number "))
# rev=0
# original=n
# for i in range(len(str(n))):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if rev==original:
#     print("pallindrome")
# else:
#     print("not pallindrome")



'''largest in a number'''

# a=input("enter your number")
# largest="0"
# for i in a:
#     if i>largest:
#         largest=i
# print(largest)

''' largest with integer'''
# a = int(input("Enter your number: "))
# largest = 0

# for i in range(len(str(a))):
#     digit = a % 10
#     if digit > largest:
#         largest = digit
#     a = a // 10

# print("Largest digit is:", largest)

'''count number of digits in a number'''
# a=int(input("enter your number"))
# count=0
# for i in range(len(str(a))):
#     count=count+1
# print(count)
    
'''table from 1 to 10'''

# for num in range(1, 11):   
#     print("Table of", num)
    
#     for i in range(1, 11):   
#         print(num, "x", i, "=", num * i)
    
#     print()   

'''hcf'''

# n=int(input("enter your number "))
# a=int(input("enter your number "))
# small=min(n,a)
# hcf=1
# for i in range(1,small+1):
#    if n%i==0 and a%i==0:
#       hcf=i
# print(hcf)

'''spy number'''

# a=input("enter your number ")
# sum=0
# product=1
# for i in a:
#     sum=sum+int(i)
#     product=product*int(i)
# if sum==product:
#     print("the number you entered is a spy number")
# else:
#     print("it's not a spy number")

'''composite number'''

# n=int(input("enter your number "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count>2:
#     print("the number you enter is composite")
# else:
#     print("the number is not composite")

'''Find the sum of all factors of a number.'''

# n=int(input("enter your number "))
# sum=0
# for i in range(1,n+1):
#       if n%i==0:
#             sum=sum+i
# print(sum)

'''sum of odd and even and their difference upto n'''
# n=int(input("enter your range "))
# sum=0
# sum2=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i
# for i in range(1,n+1):
#     if i%2!=0:
#         sum2=sum2+i
# diff=sum-sum2
# print(diff)

'''	Print all composite numbers between 1 and 100.'''
# for num in range(2, 101):   
#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count + 1

#     if count > 2:
#         print(num)

'''Print common factors of two numbers'''
# a=int(input("enter your number"))
# b=int(input("enter your number"))
# fact=min(a,b)
# for i in range(1,fact+1):
#     if a%i==0 and b%i==0:
#         fact2=i
#         print(fact2)

'''lcm'''
# a=int(input("enter your number"))
# b=int(input("enter your number"))
# c=min(a,b)
# hcf=1
# for i in range(1,c+1):
#     if a%i==0 and b%i==0:
#         hcf=i
# lcm=(a*b)//hcf
# print(lcm)

'''lcm using another way'''
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# big = max(a, b)
# for i in range(big, a * b + 1):
#     if i % a == 0 and i % b == 0:
#         print("LCM is:", i)
#         break

'''twin prime'''
# for num in range(2, 99):   # up to 98 because we check num + 2
#     count1 = 0
#     count2 = 0

#     # Check if num is prime
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count1 += 1

#     # Check if num + 2 is prime
#     for j in range(1, num + 3):
#         if (num + 2) % j == 0:
#             count2 += 1

#     if count1 == 2 and count2 == 2:
#         print((num, num + 2))


'''Find the smallest factor of a number greater than 1'''
# n=int(input("enter your number"))
# small=0
# for i in range(1,n+1):
#     if n%i==0:
#         fact=i

'''	Find the smallest digit in a number.'''

# n=int(input("enter your number"))
# small=9
# for i in range(len(str(n))):
#     dig=n%10
#     if dig<small:
#      small=dig
#     n=n//10
# print(small)

'''find the largest digit in a number'''
# a=int(input("enter your number"))
# large=0
# for i in range(len(str(a))):
#     digit=a%10
#     if digit>large:
#         large=digit
#     a=a//10
# print(large)

'''	Find the second largest digit in a number.'''
# n=int(input("enter your number "))
# large=0
# second=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>large:
#         second=large
#         large=digit
#     elif digit > second and digit != large:
#         second = digit
#     n=n//10
# print(second)

'''Count how many even digits are in a number.'''
# n=int(input("enter your number"))
# count=0
# while n>0:
#     digit=n%10
#     if n%2==0:
#         count=count+1
#     n=n//10
# print(count) 1 oues till now solved by myself not bad

'''	Count how many odd digits are in a number.'''
# a=int(input("enter your number "))
# count=0
# for i in range(len(str(a))):
#     dig=a%10
#     if a%2!=0:
#         count=count+1
#     a=a//10
# print(count)

'''Print digits of a number in reverse order (one by one).'''
# n=int(input("enter your number "))
# rev=0
# for i in range(len(str(n))):
#     digit=n%10
#     print(digit)
#     n=n//10

'''Check whether a number contains the digit 0.'''
# n=int(input("enter your digit "))
# check=0
# for i in range(len(str(n))):
#     digit=n%10
#     if check==digit:
#         print("yes ")
#         break
#     n=n//10
# else:
#     print("no") almost cracked good .5

'''Check whether all digits in a number are unique.'''
# n=int(input("enter your number "))
# rem=n
# flag=1
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count>1:
#         flag=1
#     n=n//10
# if flag==0:
#     print('unique')
# else:
#     print('not unique')




'''	Find the difference between largest and smallest digit.'''
# n=int(input("enter your number "))
# largest=0
# smallest=9
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>largest:
#         largest=digit
#     if digit<smallest:
#         smallest=digit
#     n=n//10
# diff=largest-smallest
# print(diff)
    
'''Check whether sum of digits is even or odd.'''
# n=input("enter your number ")
# sum=0
# for i in n:
#     sum=sum+int(i)
# if sum%2==0:
#     print("sum of digits is even")
# else:
#     print("sum of digits is odd")

'''Check whether a number is a strong number.(sum of factorial should be same as number )'''
# n=int(input("enter your number "))
# x=n
# sum=0
# for i in range(len(str(n))):
#     fact=1
#     digit=n%10
#     for i in range(1,digit+1):
#         fact=fact*i
#     n=n//10
#     sum=sum+fact
# if sum==x:
#     print('The number you entered is a strong number')
# else:
#     print('its not a strong number') solved by purely myself excellent work piyush so proud of your
        
'''neon number'''
# n=9
# sq=n**2
# sum=0
# for i in range(len(str(sq))):
#     digit=sq%10
#     sum=sum+digit
#     sq=sq//10
# if sum==n:
#     print("the number is neon number")
# else:
#     print("the number is not neon number")

'''every digit is unique digit'''
# n = int(input("Enter a number: "))
# original = n
# count = 0
# for i in range(len(str(original))):
#     digit = n % 10
#     remaining = n // 10

#     for j in range(len(str(remaining))):
#         if digit == remaining % 10:
#             count = count + 1
#         remaining = remaining // 10

#     n = n // 10

# if count == 0:
#     print("All digits are unique")
# else:
#     print("Digits are not unique")

'''duck number'''
# n=int(input("enter your number"))
# for i in range(len(str(n))):
#     digit=n%10
#     if digit==0:
#         print('the number you entered is a duck number')
#         break
#     n=n//10
# else:
#     print("it's not a duck number")

'''harshad number'''
# n=input('enter your number')
# x=n
# sum=0
# for i in n:
#     sum=sum+int(i)
# if int(x)%sum==0:
#     print('the number is a harshad number')
# else:
#     print("it,s not an harshad number")

'''neon number in function'''
# def neon(x):
#     return (x**2)
# n=int(input("enter your number "))
# sum=0
# for i in range(len(str(n))):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# result=neon(sum)
# print(result)

'''Print all strong numbers between 1 and 500.'''
# for num in range(1,501):
#     sum=0
#     n=num
#     for j in range(len(str(n))):
#         digit=n%10
#         fact=1
#         for i in range(1,digit+1):
#             fact=fact*i
#         sum=sum+fact
#         n=n//10
#     if sum==num:
#         print(num)

'''Count how many numbers between 1 and 100 are divisible by both 3 and 5.'''
# count=0
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         count=count+1
# print(count)

'''Check whether a number is automorphic.'''
# n = int(input("Enter your number: "))
# sq = n * n
# temp = n
# count = 0
# while temp > 0:
#     if temp % 10 == sq % 10:
#         count = count + 1
#     temp = temp // 10
#     sq = sq // 10
# if count == len(str(n)):
#     print("Automorphic number")
# else:
#     print("Not an automorphic number")


'''using forloop'''
# n = int(input("Enter your number: "))
# sq = n * n
# count = 0
# temp = n
# for i in range(len(str(n))):
#     if temp % 10 == sq % 10:
#         count = count + 1
#     temp = temp // 10
#     sq = sq // 10
# if count == len(str(n)):
#     print("Automorphic number")
# else:
#     print("Not an automorphic number")

'''sunny number '''
# n=int(input("enter your number"))
# check=n+1
# perfect_square=int(check**0.5)
# square=perfect_square**2
# if check==square:
#     print('sunny number')
# else:
#     print('not a sunny number')

'''Find the largest digit in a number'''
# n=int(input("enter your number "))
# largest=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>largest:
#         largest=digit
#     n=n//10
# print(largest)

'''Check whether a number is Armstrong.'''
# n=int(input("enter "))
# x=n
# power=len(str(n))
# total=0
# for i in range(len(str(n))):
#     digit=n%10
#     total=total+digit**power
#     n=n//10
# if total==x:
#     print('armstrong')
# else:
#     print('not armstrong')

'''check whether a digit contains 9'''
# n=int(input("enter your number"))
# for i in range(len(str(n))):
#     digit=n%10
#     if digit==9:
#         print("it contains 9")
#         break
#     n=n//10
# else:
#     print("it doesnt contain 9")

'''hcf prime factorization method'''
# count=0
# n=int(input("enter "))
# m=int(input("enter "))
# for i in range(2,n+1):
#     if n%i==0:
#         print(i)

# window func takes same no of input rows and in output it provides same no of ouput rows
# it takes multiple input rows but in output it provides the output for each row

'''Count how many digits are greater than 5.'''
# n=int(input("enter "))
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>5:
#         count=count+1
#     n=n//10
# print(count)
'''Count repeated digits.'''
# n = int(input("enter "))
# count = 0
# temp = n

# for i in range(len(str(n))):
#     digit = temp % 10
#     remaining = temp // 10

#     for j in range(len(str(remaining))):
#         another_digit = remaining % 10
#         if digit == another_digit:
#             count = count + 1
#         remaining = remaining // 10

#     temp = temp // 10

# print(count)

'''Print factorial of each digit.'''
# n=int(input("enter your number "))
# x=n
# for i in range(len(str(n))):
#     fact=1
#     digit=n%10
#     for j in range(1,digit+1):
#         fact=fact*j
#     print(fact)
#     n=n//10

'''Count how many zeros are in a number.'''
# n=int(input("enter "))
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit==0:
#         count=count+1
#     n=n//10
# print(count)

'''Find the average of digits.'''
# n=int(input("enter "))
# sum=0
# average=len(str(n))
# for i in range(len(str(n))):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# avg_digits=sum/average
# print(avg_digits)

'''33.	Print sum of squares of digits.'''
# n=int(input("enter "))
# sum=0
# for i in range(len(str(n))):
#     digit=n%10
#     sq=digit**2
#     n=n//10
#     sum=sum+sq
# print(sum)

'''36.	Count prime digits in a number.'''
# n=int(input("enter "))
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     for j in range(1,digit+1):
#        if j%digit==0:
#            count=count+1
#            if count==2:
#                print('prime digits in number ')
#            else:
#                print('no prime')
#     n=n//10

'''print string index values but negative  '''
'''open cv code'''
'''show minus indexing '''
# a=input("enter your string ")
# b=a[::-1]
# index=-1
# for i in b:
#     print(i,index)
#     index=index+(-1)

'''41.	Check if first and last digit are same.'''
# n=int(input("enter your number"))
# last=n%10
# x=n
# for i in range(len(str(n))-1):
#     x=x//10
#     first=x
# if first==last:
#     print('the digits are same ')
# else:
#     print('the digits are not same')

'''Perfect digit sum number'''
# n=int(input("enter your digits"))
# sum=0
# for i in range(len(str(n))):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# a=sum
# sum2=0
# for j in range(1,a):
#     if a%j==0:
#         sum2=sum2+j
# if a==sum2:
#     print("the number you entered is a Perfect digit sum number")
# else:
#     print("the number you entered is not a Perfect digit sum number")

# ----------------------------------new questions--------------------------------------------------

'''Check if sum of digits is prime'''
# n=int(input("enter your number"))
# sum=0
# for i in range(len(str(n))):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# a=sum
# count=0
# for j in range(1,a+1):
#     if a%j==0:
#         count=count+1
# if count==2:
#     print("sum of digits is prime")
# else:
#     print("sum of digits is not prime")

'''Check if product of digits is prime.'''
# n=int(input("enter your number"))
# product=1
# while n>0:
#     digit=n%10
#     product=product*digit
#     n=n//10
# prime=product
# count=0
# for i in range(1,prime+1):
#     if prime%i==0:
#         count=count+1
# if count==2:
#     print("the products of digits is prime")
# else:
#     print("the products of digits is not prime")

'''Check if sum of digits is Armstrong.'''
# n=int(input("enter your number"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# x=sum
# a=b=x
# power=0
# while x>0:
#     digit=x%10
#     power=power+1
#     x=x//10
# sum2=0
# while b>0:
#     ld=b%10
#     sum2=sum2+ld**power
#     b=b//10
# if a==sum2:
#     print("the sum of digits is armstrong")
# else:
#     print("the sum of digits is not armstrong")

'''Check if digit sum is Harshad.'''
# n = int(input("enter your number "))
# temp = n
# total = 0
# while temp > 0:
#     digit = temp % 10
#     total = total + digit
#     temp = temp // 10
# x = total
# sum2 = 0
# temp2 = x
# for i in range(len(str(x))):
#     digit = temp2 % 10
#     sum2 = sum2 + digit
#     temp2 = temp2 // 10
# if x % sum2 == 0:
#     print("the sum of digits is harshad")
# else:
#     print("the sum of digits is not harshad")

'''Check if digit product is perfect number.'''
# n=int(input("enter your number "))
# prod=1
# for i in range(len(str(n))):
#     digit=n%10
#     prod=prod*digit
#     n=n//10
# sum=0
# for j in range(1,prod):
#     if prod%j==0:
#         sum=sum+j
# if prod==sum:
#     print("product of digits is perfect")
# else:
#     print("products of digits is not perfect")

'''Count how many digits are prime'''
# n=int(input("enter your number "))
# count=0
# for num in range(len(str(n))):
#     digit=n%10
#     count2=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count2=count2+1
#     if count2==2:
#         count=count+1
#     n=n//10
# print(f"there are {count} prime number in your digit")

'''Count how many digits are composite.'''
# n=int(input("enter your number"))
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     count2=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count2=count2+1
#     if count2>2:
#         count=count+1
#     n=n//10
# print(f"there are {count} number of composite digits")

'''Print only prime digits.'''
# n=int(input("enter your digits"))
# for i in range(len(str(n))):
#     digit=n%10
#     count=0
#     for j in range(1,digit+1):
#         if digit%j==0:
#             count=count+1
#     if count==2:
#         print(digit,end=' ')
#     n=n//10
        
'''Print only composite digits'''
# n=int(input("enter your digits "))
# for i in range(len(str(n))):
#     digit=n%10
#     count=0
#     for j in range(1,digit+1):
#         if digit%j==0:
#             count=count+1
#     if count>2:
#         print(digit)
#     n=n//10

'''Check if number contains more even digits than odd digits.'''
# n=int(input("enter your number "))
# x=n
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2==0:
#         count=count+1
#     n=n//10
# count2=0
# for j in range(len(str(x))):
#     digit=x%10
#     if digit%2!=0:
#         count2=count2+1
#     x=x//10
# if count>count2:
#     print("the number contains more even digits than odd digits.")
# else:
#      print("the number does not contains more even digits than odd digits.")

'''take prime and composite from digits then find their difference and check whether there 
difference is even or odd'''

'''Check if first digit is greater than last digit.'''
# n=int(input("enter your number"))
# last=n%10
# x=n
# for i in range(len(str(n))-1):
#     x=x//10
#     first=x
# if first>last:
#     print('the first digit is greater than last digit  ')
# else:
#     print('the first digit is not greater than last digit')

'''Find difference between sum of even and odd digits.'''
# n=int(input("enter your number"))
# x=n
# sum=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2==0:
#         sum=sum+digit
#     n=n//10  
# sum2=0
# for j in range(len(str(x))):
#     digits=x%10
#     if digits%2!=0:
#         sum2=sum2+digits
#     x=x//10
# difference=sum-sum2
# print(f"the difference between even and odd digits is {abs(difference)}")

'''Check if number is Krishnamurthy.'''
# n=int(input("enter your number"))
# x=n
# sum=0
# for i in range(len(str(n))):
#     digit=n%10
#     prod=1
#     for j in range(1,digit+1):
#         prod=prod*j
#     sum=sum+prod
#     n=n//10
# if x==sum:
#     print(" Krishnamurthy ")
# else:
#     print( "not Krishnamurthy ")

'''Check if reverse of number is prime'''
# n=int(input("enter your number "))
# rev=0
# for i in range(len(str(n))):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
#     count=0
#     for j in range(1,rev+1):
#         if rev%j==0:
#             count=count+1
# if count==2:
#     print("the rev of number is prime")
# else:
#     print("the rev of number is not prime")

'''Check if sum of first half digits equals second half digits.'''
# n=int(input("enter your digits "))
# x=n
# count=0
# for i in range(len(str(n))):
#     count=count+1
# if count%2!=0:
#     print("Number does not have even number")
# else:
#     half=count//2
#     sum=0
#     sum2=0
#     for i in range(half):
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     for j in range(half):
#         digit=x%10
#         sum2=sum2+digit
#         x=x//10
# if sum==sum2:
#     print("sum of first half digits equals second half digits")
# else:
#     print("sum of first half digits is not equals to second half digits")

'''Check if all digits are same.'''
# n=int(input("enter your number "))
# for i in range(len(str(n))):
#     digit=n%10
#     remaining=n//10
#     for j in range(len(str(remaining))):
#         digits=remaining%10
# if digit==digits:
#     print(digit,digits)
# else:
#     print("all are not same")
#     remaining=remaining//10
#     n=n//10                     not understood logic

'''40.	Check if number becomes palindrome after reversing once.'''
# n=int(input("enter your number "))
# rev=0
# for i in range(len(str(n))):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# check_pallindrome=rev
# revrse=0
# x=check_pallindrome
# for i in range(len(str(check_pallindrome))):
#     digit2=check_pallindrome%10
#     revrse=revrse*10+digit2
#     check_pallindrome//10
# if x==check_pallindrome:
#     print("the number becomes palindrome after reversing once")
# else:
#     print("the number becomes not palindrome after reversing once")

'''38.	Replace all 0 digits with 1 and print a new number.'''
# n=int(input("enterr your number:- "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit==0:
#         digit=1
#     new=new*10+digit
#     n=n//10
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)                  #very brriliant


'''36.	Check if number is Magic number.'''   
# n=int(input("enter your number"))
# sum=0
# check=1
# for i in range(len(str(n))):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# a=sum
# sum2=0
# for i in range(len(str(a))):
#     digit=a%10
#     sum2=sum2+digit
#     a=a//10
# if sum2==check:
#     print("the number you entered is a magic number")
# else:
#     print("the number is not a magic number")

'''37.	Remove all even digits and print new number'''
# n=int(input("enter "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2!=0:
#         new=new*10+digit
#     n=n//10
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)             #brilliant work 


'''Count digits that divide the number completely.'''
# n=int(input("enter your number"))
# x=n
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     if x%digit==0:
#         count=count+1
#     n=n//10
# print(count) good almost cracked 

'''Count digits greater than 5.'''
# n=int(input("enter your number "))
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>5:
#         count=count+1
#     n=n//10
# print(count)

'''6.	Print digits greater than average of digits.'''
# n=int(input("enter "))
# sum=0
# avg=len(str(n))
# for i in range(len(str(n))):
#     digit=n%10
#     x=digit
#     sum=sum+digit
#     out=sum//avg
#     if x>out:
#         print(x)
#     n=n//10

'''29.	Find most frequent digit.'''
# n=int(input("enter your number "))
# x=n
# max_count=0
# result=0
# count=0
# for i in range(len(str(n))):
#     digit=x%10
#     remaining=n
#     count=0
#     for j in range(len(str(remaining))):
#         dig=remaining%10
#         if dig==digit:
#             count=count+1
#         remaining=remaining//10
#     if count>max_count:
#         max_count=count
#         result=digit
#     x=x//10
# print("the most frequent digit is",result)

'''find least frequent digit'''
# n=int(input("enter "))
# max_count=9
# result=0
# x=n
# for i in range(len(str(n))):
#     digit=x%10
#     remaining=n
#     count=0
#     for j in range(len(str(remaining))):
#         dig=remaining%10
#         if dig==digit:
#             count=count+1
#         remaining=remaining//10
#     if count<max_count:
#         max_count=count
#         result=digit
#     x=x//10
# print("the least frequent digit is ",result)  touchwood 

'''Find the difference between largest and smallest digit.'''
# n=int(input("enter your number "))
# x=n
# large=0
# small=9
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>large:
#         large=digit
#     n=n//10
# for i in range(len(str(x))):
#     digit=x%10
#     if digit<small:
#         small=digit
#     x=x//10
# difference=large-small
# print(abs(difference))

'''Print digits that are multiples of 3.'''
# n=int(input("enter your number "))
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%3==0:
#         print(digit)
#     n=n//10

'''	Check if the number contains digit 0.'''
# n=int(input("enter your number "))
# for i in range(len(str(n))):
#     digit=n%10
#     if digit==0:
#         print("yes the digit contains zero")
#         break
#     n=n//10
# else:
#     print("the number doesnt have zero")

'''16.	Count how many digits are smaller than the last digit.'''
# n=int(input("enter your number "))
# count=0
# ld=n%10
# for i in range(len(str(n))):
#     digit=n%10
#     if digit<ld:
#         count=count+1
#     n=n//10
# print(count)

'''	Print digits at even positions.'''
# n=int(input("enter your number "))
# position=1
# for i in range(len(str(n))):
#     digit=n%10
#     if position%2==0:
#         print(digit)
#     n=n//10
#     position=position+1

'''Print digits at odd positions.'''
# n=int(input("enter your number"))
# position=1
# for i in range(len(str(n))):
#     digit=n%10
#     if position%2!=0:
#         print(digit)
#     n=n//10
#     position=position+1

'''Print double of each digit.'''
# n=int(input("enter your number "))
# for i in range(len(str(n))):
#     digit=n%10
#     print(digit*2)
#     n=n//10

'''Check if the last digit is the largest digit.'''
# n=int(input("enter your number "))
# ld=n%10
# x=n
# for i in range(len(str(x))):
#     digit=x%10
#     if digit>ld:
#         print("the last digit is the largest digit.")
#     x=x//10
# else:
#     print("the last digit is not the largest digit.")

'''	Count digits equal to 1.'''
# n=int(input("enter your number"))
# count=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit==1:
#         count=count+1
#     n=n//10
# print("there are",count,"digits equal to 1")

'''Print the sum of squares of digits.'''
# n=int(input("enter your number"))
# sum=0
# for i in range(len(str(n))):
#     digit=n%10
#     sq=digit**2
#     n=n//10
#     sum=sum+sq
# print(sum)

'''26.	Check if the number is palindrome.'''
# n=int(input("enter your no "))
# x=n
# rev=0
# for i in range(len(str(n))):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if rev==x:
#     print("pallindrome")
# else:
#     print("not pallindrome")

'''Replace each digit with digit + 1.'''
# n=int(input("enter your number"))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     digit+=1
#     n=n//10
#     new=new*10+digit
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''Replace each digit with 1 if even, 0 if odd.'''
# n=int(input("enter your number"))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2==0:
#         digit=1
#     else:
#         digit=0
#     n=n//10
#     new=new*10+digit
# print(new)

'''Replace digits equal to 1 with product of digits.'''
# n=int(input("enter your digit"))
# y=n
# prod=1
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     prod=prod*digit
#     n=n//10
# x=prod
# for j in range(len(str(y))):
#     digit=y%10
#     if digit==1:
#         digit=x
#     y=y//10
#     new=new*10+digit
# result=0
# for j in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''Replace digits greater than 5 with 9.'''
# n=int(input("enter "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>5:
#         digit=9
#     n=n//10
#     new=new*10+digit
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''Print a number containing only prime digits.'''
# n=int(input("enter your number "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     count=0
#     for j in range(1,digit+1):
#         if digit%j==0:
#             count=count+1
#     if count==2:
#         new=new*10+digit
#     n=n//10
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''23.	Remove all 0 digits.'''
# n=int(input("enter your digit"))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit!=0:
#         new=new*10+digit
#     n=n//10
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)
        
'''28.	Remove digits divisible by 3.'''
# n=int(input("enter your digit"))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%3!=0:
#         new=new*10+digit
#     n=n//10
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''	Remove digits smaller than previous digit.'''
# n=int(input("enter your digit"))
# for i in range(len(str(n))):
#     digit=n%10
#     remaining=n
#     for i in range(len(str(remaining))):

'''Replace digits less than 5 with digit + 3.'''
# n=int(input("enter your number"))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit<5:
#         digit+=3
#     n=n//10
#     new=new*10+digit
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''Reverse digits but remove even digits.'''
# n=int(input("enter your number "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2!=0:
#         new=new*10+digit
#     n=n//10
# print(new)

'''Replace digits greater than average with average digit.'''
# n=int(input("enter your number "))
# x=n
# sum=0
# avg=len(str(n))
# for i in range(len(str(n))):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# result=sum//avg
# y=result
# new=0
# for i in range(len(str(x))):
#     digit=x%10
#     if digit>result:
#         digit=result
#     new=new*10+digit
#     x=x//10
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''81.	Double every odd digit, keep even digits same.'''
# n=int(input("enter your digit"))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2!=0:
#         digit*=2
#     n=n//10
#     new=new*10+digit
# result=0
# for i in range(len(str(new))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''83.	Replace even digits with next odd digit.'''
# n=int(input("enter your number "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2==0:
#         digit+=1
#     n=n//10
#     new=new*10+digit
# x=0
# for i in range(len(str(new))):
#     digit=new%10
#     x=x*10+digit
#     new=new//10
# print(x)

'''86.	Replace digits greater than 7 with their half.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     if digit>7:
#         digit*=0.5
#     n=n//10
#     new=new*10+digit
#     x=abs(new)
# result=0
# while x>0:
#     digit=x%10
#     result=result*10+digit
#     x=x//10
# print(result)

'''Replace every digit with digit + position.'''
# n = int(input("Enter a number: "))
# temp = n
# count = 0

# # count digits
# while temp > 0:
#     count += 1
#     temp //= 10

# pos = count
# new = 0

# while n > 0:
#     digit = n % 10
#     digit = digit + pos
#     new = new * 10 + digit
#     n //= 10
#     pos -= 1

# # reverse result
# x = 0
# while new > 0:
#     digit = new % 10
#     x = x * 10 + digit
#     new //= 10

# print(x)

'''Replace digits equal to last digit with 9.'''
# n=int(input("enter your number "))
# ld=n%10
# new=0
# while n>0:
#     digit=n%10
#     if digit==ld:
#         digit=9
#     n=n//10
#     new=new*10+digit
# x=0
# while new>0:
#     digit=new%10
#     x=x*10+digit
#     new=new//10
# print(x)

'''Replace digits divisible by both 2 and 3 with 6.'''
# n=int(input("enter your number"))
# new=0
# while n>0:
#     digit=n%10
#     if digit%2==0 and digit%3==0:
#         digit=6
#     n=n//10
#     new=new*10+digit
# x=0
# while new>0:
#     digit=new%10
#     x=x*10+digit
#     new=new//10
# print(x)


'''febonnaci'''
# num=int(input("enter a number "))
# fi=0
# se=1
# print(fi,se,end=" ")
# for i in range (num-2):
#     nx=fi+se
#     print(nx,end=" ")
#     fi = se
#     se = nx 

# n=int(input("enter your number "))
# a=0
# b=1
# i=0
# while i < n:
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c
#     i=i+1

# n=int(input("enter your number "))
# fi=0
# se=1
# for i in range(n):
#     print(fi,end=' ')
#     nx=fi+se
#     fi=se
#     se=nx

'''Replace 0 with 9 and 9 with 0.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     if digit==0:
#         digit=9
#     new=new*10+digit
#     n=n//10
# x=new
# y=0
# while x>0:
#     digit=x%10
#     if digit==9:
#         digit=0
#     y=y*10+digit
#     x=x//10
# print(y)


'''Replace digits equal to 0 with sum of digits.'''
# n=int(input("enter your number "))
# x=n
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# y=sum
# new=0
# while x>0:
#     digit=x%10
#     if digit==0:
#         digit=y
#     x=x//10
#     new=new*10+digit
# result=0
# while new>0:
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)


'''74.	Replace each digit with digit squared mod 10..'''
# n=int(input("enter your number "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     digit=(digit**2)%10
#     n=n//10
#     new=new*10+digit
# result=0
# for i in range(len(str(n))):
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''61.	Replace each digit with digit + 1.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     digit+=1
#     n=n//10
#     new=new*10+digit
# result=0
# while new>0:
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)


'''64.	Replace each digit with digit × digit.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     digit=digit**2
#     n=n//10
#     new=new*10+digit
# print(new)

'''65.	Replace each digit with digit factorial (0–9).'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     fact=1
#     for i in range(1,digit+1):
#         fact=fact*i
#     digit=fact
#     n=n//10
#     new=new*10+digit
# result=0
# while new>0:
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)


'''66.	Replace each digit with sum of its factors.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     sum=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             sum=sum+i
#     digit=sum
#     new=new*10+digit
#     n=n//10
# result=0
# while new>0:
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''68.	Replace each digit with 0 if even, 1 if odd.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         digit=0
#     else:
#         digit=1
#     n=n//10
#     new=new*10+digit
# result=0
# while new>0:
#     digit=new%10
#     result=result*10+digit
#     new=new//10
# print(result)

'''73.	Replace each digit with difference between digit and 5.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     diff=digit-5
#     digit=diff
#     n=n//10
#     new=new*10+digit
# x=0
# while new>0:
#     digit=new%10
#     x=x*10+digit
#     new=new//10
# print(abs(x))

'''77.	Replace digits equal to 1 with product of digits.'''
# n=int(input("enter your digit "))
# x=n
# prod=1
# new=0
# while n>0:
#     digit=n%10
#     prod=prod*digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit==1:
#         digit=prod
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''Replace digits whose square > 50 with 5'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     sq=digit**2
#     if sq>50:
#         digit=5
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''Replace each digit with 1 if composite else 0.'''
# n=int(input("enter your number "))
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count=count+1
#     if count>2:
#          digit=1
#     else:
#         digit=0
#     n=n//10

'''max and min from a list'''
# l=[56,4,7,8,3,4,5,6,4,56,78,34,90,45,3,6,1,5,4,6]
# max=4
# for i in l:
#     if i>max:
#         max=i
# print(max)

# l=[56,4,7,8,3,4,5,6,4,56,78,34,90,45,3,6,1,5,4,6]
# min=5
# for i in l:
#     if i<min:
#         min=i
# print(min)

# frequecy
# l = [56,4,7,8,3,4,5,6,4,56,78,34,90,45,3,6,1,5,4,6]

# freq = {}

# for i in l:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)
    
'''Write a Python program to find the sum of even number from a list.'''
# l=[2,39,40,5,60]
# sum=0
# for i in l:
#     if i%2==0:
#         sum=sum+i
# print(sum)

# Q.1(b)Write a Python program to count the total number of digits in a number
# n=int(input("enter "))
# count=0
# for i in range(len(str(n))):
#     count=count+1
# print(count)

'''Q.2(b)Write a program to count occurrences of all characters within a string'''
# def count(s,ch):
#     count=0
#     for i in s:
#         if i==ch:
#             count=count+1
#     print(count)
# a=input("enter ")
# b=input("ch ")
# count(a,b)

'''Write a program to check whether a number is prime or not,using user define function.'''
# def prime():
#     n=int(input("enter "))
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     if count==2:
#         print("the number is prime")
#     else:
#         print("not prime")
# prime()


# l=['cricket','hockey','tennis','football','hockey']
# count=0
# for i in l:
#     if i=='hockey':
#         count=count+1
# print(count)

# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]

# for i in list1:
#     if i in list2:
#         print(i)


'''Q.1(a) Write a Python program to find the factorial of any number.'''
# n=int(input("enter "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

'''Replace every digit with its double if odd, otherwise keep same.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     if n%2!=0:
#         digit*=2
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''Replace digits between 3 and 7 with 1..'''
# n=int(input("enter your number "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit>3 and digit<7:
#         digit=1
#     n=n//10
#     new=new*10+digit
# res=0
# for i in range(len(str(new))):
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''Replace digits divisible by position index with 1.'''
# n=int(input("enter your number "))
# new=0
# y=n
# pos=len(str(n))
# while y>0:
#     digit=y%10
#     if digit%pos==0:
#         digit=1
#     y=y//10
#     new=new*10+digit
#     pos=pos-1
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''Remove digits equal to sum of first and last digit.'''
# n=int(input("enter your number "))
# new=0
# x=n
# ld=n%10
# while n>=10:
#     n=n//10
# fd=n
# sum=fd+ld
# while x>0:
#     digit=x%10
#     if digit!=sum:
#         new=new*10+digit
#     x=x//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''129.	Remove digits equal to maximum digit.'''
# n=int(input("enter your number "))
# x=n
# max=0
# while n>0:
#     digit=n%10
#     if digit>max:
#         max=digit
#     n=n//10
# a=max
# new=0
# while x>0:
#     digit=x%10
#     if digit!=a:
#         new=new*10+digit
#     x=x//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''145.	Keep digits greater than first digit.'''
# n=int(input("enter your number "))
# x=n
# while n>=10:
#     n=n//10
# fd=n
# new=0
# while x>0:
#     digit=x%10
#     if digit>fd:
#         new=new*10+digit
#     x=x//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''159.	Keep digits forming palindrome pattern.'''
# n=int(input("enter your number "))
# x=n
# rev=0
# new=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# while x>0:
#     d1=x%10
#     d2=rev%10
#     if d1==d2:
#         new=new*10+d1
#     x=x//10
#     rev=rev//10
# print(new)

'''158.	Keep digits that appear more than once.'''
# n = int(input("enter your number "))
# temp = n
# new = 0
# while n > 0:
#     digit = n % 10
#     remain = temp
#     count = 0
#     while remain > 0:
#         d = remain % 10
#         if d == digit:
#             count = count + 1
#         remain = remain // 10
#     if count > 1:
#         new = new * 10 + digit
#     n = n // 10
# print(new)

'''Keep digits equal to sum of first and last digit.'''
# n=int(input("enter your number "))
# x=n
# new=0
# ld=n%10
# while n>=10:
#     n=n//10
# fd=n
# sum=ld+fd
# while x>0:
#     digit=x%10
#     if digit==sum:
#         new=new*10+digit
#     x=x//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''Replace each digit with digit + position.'''
# n=int(input("enter your number "))
# x=n
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     digit=digit+pos
#     n=n//10
#     new=new*10+digit
#     pos=pos-1
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''163.	Replace each digit with digit × position.'''
# n=int(input("enter your number "))
# x=n
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     digit=digit*pos
#     n=n//10
#     new=new*10+digit
#     pos=pos-1
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''170.	Replace each digit with 1 if prime else 0.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count=count+1
#     if count==2:
#         digit=1
#     else:
#         digit=0
#     new=new*10+digit
#     n=n//10
# print(new)
 

'''176.	Replace each digit with digit + largest digit.'''
# n=int(input("enter your number "))
# new=0
# x=n
# large=0
# while n>0:
#     digit=n%10
#     if digit>large:
#         large=digit
#     n=n//10
# y=large
# while x>0:
#     digit=x%10
#     digit=digit+y
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''Replace each digit with digit × first digit.'''
# n=int(input("enter your number "))
# x=n
# new=0
# while n>=10:
#     n=n//10
# fd=n
# while x>0:
#     digit=x%10
#     digit=digit*fd
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''181.	Double even digits, triple odd digits.'''
# n=int(input("enter your number "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit%2==0:
#         digit=digit*2
#     else:
#         digit=digit*3
#     n=n//10
#     new=new*10+digit
# res=0
# for i in range(len(str(new))):
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''185.	Reverse digits and square each digit.'''
# n=int(input("enter your number "))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10


'''191.	Replace digits equal to first digit with position index.'''
# n=int(input("enter your number "))
# x=n
# pos=len(str(n))
# new=0
# while n>=10:
#     n=n//10
# fd=n
# while x>0:
#     digit=x%10
#     if digit==fd:
#         digit=pos
#     x=x//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''199.	Replace digits forming symmetric positions with 0'''
# n = int(input("enter your number "))
# x = n
# rev = 0
# new = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# while x > 0:
#     d1 = x % 10
#     d2 = rev % 10

#     if d1 == d2:
#         digit = 0
#     else:
#         digit = d1

#     new = new * 10 + digit

#     x = x // 10
#     rev = rev // 10
# res = 0
# while new > 0:
#     digit = new % 10
#     res = res * 10 + digit
#     new = new // 10

# print(res)

'''191.	Replace digits equal to first digit with position index.'''
# n=int(input("enter your number "))
# x=n
# pos=len(str(x))
# new=0
# while n>=10:
#     n=n//10
# fd=n
# while x>0:
#     digit=x%10
#     if digit==fd:
#         digit=pos
#     x=x//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''241.	Remove digits whose square is greater than sum of digits.'''
# n=int(input("enter your number "))
# sum=0
# x=n
# new=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit**2>sum:
#         new=new*10+digit
#     x=x//10
# print(new)

'''226.	Replace digits whose index is prime with 4'''
# n=int(input("enter your number "))
# new=0
# count=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             count=count+1
#     if count==2:
#         digit=4
#     new=new*10+digit
#     n=n//10
#     pos=pos-1
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''228.	Replace digits equal to digit sum with 4.'''
# n=int(input("enter your number "))
# sum=0
# x=n
# new=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit==sum:
#         digit=4
#     x=x//10
#     new=new*10+digit
# print(new)

'''241.	Remove digits whose square is greater than sum of digits.'''
# n=int(input("enter your number "))
# new=0
# x=n
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit**2<=sum:
#         new=new*10+digit
#     x=x//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''219.	Replace digits whose square > 50 with 5.'''
# n=int(input("enter your number "))
# new=0
# for i in range(len(str(n))):
#     digit=n%10
#     if digit**2>50:
#         digit=5
#     n=n//10
#     new=new*10+digit
# res=0
# for i in range(len(str(new))):
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''222.	Replace digits appearing exactly twice with 1.'''
# n=int(input("enter your number "))
# x=n
# new=0
# while n>0:
#     digit=n%10
#     rem=x
#     count=0
#     while rem>0:
#         d2=rem%10
#         if digit==d2:
#             count=count+1
#         rem=rem//10
#     if count==2:
#         digit=1
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''221.	Replace digits appearing more than twice with 0.'''
# n=int(input("enter your number "))
# new=0
# x=n
# while n>0:
#     digit=n%10
#     rem=x
#     count=0
#     while rem>0:
#         d2=rem%10
#         if digit==d2:
#             count=count+1
#         rem=rem//10
#     if count>2:
#         digit=0
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''224.	Replace digits forming prime numbers with 7.'''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count=count+1
#     if count==2:
#         digit=7
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''225.	Replace digits forming Fibonacci positions with 8.'''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     fi=0
#     se=1
#     flag=0
#     while fi<=pos:
#         if fi==pos:
#             flag=1
#         nx=fi+se
#         fi=se
#         se=nx
#     if flag==1:
#         digit=8
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)
    
'''236.	Replace digits greater than variance with 7.'''
# n=int(input("enter your number "))
# y=n
# x=n
# lent=len(str(n))
# sum=0
# new=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# mean=sum/lent
# sum2=0
# while x>0:
#     digit=x%10
#     sum2=sum2+(digit-mean)**2
#     x=x//10
# var=sum2/lent
# while y>n:
#     digit=y%10
#     if digit>var:
#         digit=7
#     y=y//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''237.	Replace digits less than variance with 8.'''
# n=int(input("enter your number "))
# y=n
# x=n
# lent=len(str(n))
# sum=0
# new=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# mean=sum/lent
# sum2=0
# while x>0:
#     digit=x%10
#     sum2=sum2+(digit-mean)**2
#     x=x//10
# var=sum2/lent
# while y>0:
#     digit=y%10
#     if digit<var:
#         digit=8
#     y=y//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''239.	Replace digits forming increasing pairs with 4.'''
# n = int(input("enter your number "))
# new = 0
# prev = n % 10
# n = n // 10
# new = prev
# while n > 0:
#     digit = n % 10
#     if prev > digit:
#         new = new * 10 + 4
#     else:
#         new = new * 10 + digit
#     prev = digit
#     n = n // 10
# res = 0
# while new > 0:
#     d = new % 10
#     res = res * 10 + d
#     new = new // 10
# print(res)

'''252.	Remove digits greater than next digit.'''
'''344.	Replace each digit with sum of prime digits.'''
# n=int(input("enter your number "))
# x=n
# sum=0
# new=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count=count+1
#     if count==2:
#         sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     digit=sum
#     x=x//10
#     new=new*10+digit
# print(new)

'''252.	Remove digits greater than next digit.'''
# n=int(input("enter your number "))
# new=0
# next_digit=n%10
# n=n//10
# new=next_digit
# while n>0:
#     digit=n%10
#     if digit>next_digit:
#         pass
#     else:
#         new=new*10+digit
#     next_digit=digit
#     n=n//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''263.	Remove digits greater than average of neighbors.'''
'''296.	Keep digits whose square equals sum of digits.'''
# n=int(input("enter your number "))
# x=n
# sum=0
# new=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit**2==sum:
#         new=new*10+digit
#     x=x//10
# print(new)

'''neighbour number sum'''
# 201. Replace digits equal to sum of neighbors with 7
# n = int(input("enter number: "))
# prev = -1
# curr = n % 10
# n = n // 10
# new = curr   
# while n > 0:
#     next_d = n % 10   
#     if prev == -1:
#         s = next_d
#     else:
#         s = prev + next_d
#     if curr == s:
#         digit = 7
#     else:
#         digit = curr
#     new = new * 10 + digit
#     prev = curr
#     curr = next_d
#     n = n // 10
# if prev != -1:
#     if curr == prev:
#         new = new * 10 + 7
#     else:
#         new = new * 10 + curr
# res = 0
# while new > 0:
#     d = new % 10
#     res = res * 10 + d
#     new = new // 10
# print(res)


'''51.	Replace digits equal to 0 with sum of digits. '''
# n=int(input("enter your number "))
# x=n
# new=0
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit==0:
#         digit=sum
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''53.	Replace digits greater than previous digit with 5. '''
# n=int(input("enter your number "))
# new=0
# prev=n%10
# n=n//10
# new=prev
# while n>0:
#     digit=n%10
#     orig=digit
#     if prev>digit:
#         digit=5
#     new=new*10+digit
#     prev=orig
#     n=n//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''54.	Replace digits less than previous digit with 2. '''












'''59.	Replace digits divisible by position index with 7. '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     if digit%pos==0:
#         digit=7
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''if indexing is prime replace it with 0'''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             count=count+1
#     if count==2:
#         digit=0
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''131.	Reverse number and replace even digits with 0. '''
# n=int(input("enter your number "))
# rev=0
# new=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# x=rev
# while x>0:
#     digit=x%10
#     if digit%2==0:
#         digit=0
#     x=x//10
#     new=new*10+digit
# print(new)



'''148.	Replace digits whose index is square number with 9. '''
# n = int(input("enter your number "))
# new = 0
# pos = len(str(n))
# while n > 0:
#     digit = n % 10
#     root = pos ** 0.5
#     sq = int(root) ** 2
#     if pos == sq:
#         digit = 9
#     n = n // 10
#     pos = pos - 1
#     new = new * 10 + digit
# res = 0
# while new > 0:
#     d = new % 10
#     res = res * 10 + d
#     new = new // 10
# print(res)

'''143.	Replace digits whose index is composite with 4. '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             count=count+1
#     if count>2:
#         digit=4
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

''''''
'''find sum of hcf and lcm of 12,21,15
output-423'''

'''Replace first and last digit if their sum is prime.'''
'''1.	Replace digits at odd positions with 0. '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     if pos%2!=0:
#         digit=0
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''8.	Replace digits at positions ending in 5 (5,15,25...) with 6. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if pos%10==5:
#         digit=6
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

# 9.	Replace digits at first and last position with 0. 
# n=int(input("enter your number "))
# new=0
# ld=n%10
# while n>0:
#     digit=n%10
#     if digit==ld:
#         digit=0
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''5.	Replace digits at square positions with 7. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     root=pos**0.5
#     sq=int(root)**2
#     if pos==sq:
#         digit=7
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''27.	Replace digits where position is even AND digit is odd with 8. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if pos%2==0 and digit%2!=0:
#         digit=8
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)'''

'''39.	Reverse number and replace digits ending in 5 or 0 with 7. '''
# n=int(input("enter your number "))
# rev=0
# new=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# while rev>0:
#     ld=rev%10
#     if ld==5 or ld==0:
#         ld=7
#     rev=rev//10
#     new=new*10+ld
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''73.	Replace digits at square positions with digit + position. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     root=pos**0.5
#     sq=root**2
#     if pos==sq:
#         digit=digit+pos
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''51.	Replace each digit with sum of its proper divisors. '''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     sum=0
#     for i in range(1,digit):
#         if digit%i==0:
#             sum=sum+i
#     digit=sum
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''53.	Replace each digit with count of its prime factors. '''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     x=digit
#     c2=0
#     for i in range(2,digit+1):
#         count=0
#         for j in range(1,i+1):
#                 if i%j==0:
#                     count=count+1
#         if count==2:
#             while x%i==0:
#                  c2=c2+1
#                  x=x//i
#     digit=c2
#     n=n//10
#     new=new*10+digit
# print(new)


'''54.	Replace each digit with next Fibonacci number. '''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     fi=0
#     se=1
#     while se<=digit:
#         nx=fi+se
#         fi=se
#         se=nx
#     digit=se
#     n=n//10
#     new=new*10+digit   
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res) 

'''55.	Replace each digit with previous Fibonacci number. '''
# n = int(input("enter your number "))
# new = 0
# while n > 0:
#     digit = n % 10
#     if digit <= 1:
#         digit = digit
#     else:
#         fi = 0
#         se = 1
#         while se < digit:
#             nx = fi + se
#             fi = se
#             se = nx
#         digit = fi
#     n = n // 10
#     new = new * 10 + digit
# res = 0
# while new > 0:
#     d = new % 10
#     res = res * 10 + d
#     new = new // 10
# print(res)

'''58.	Replace each digit with difference between max digit and itself. '''
# n=int(input("enter your number "))
# new=0
# x=n
# max=0
# while n>0:
#     digit=n%10
#     if digit>max:
#         max=digit
#     n=n//10
# while x>0:
#     digit=x%10
#     diff=max-digit
#     digit=diff
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''56.	Replace each digit with nearest multiple of 3. '''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     r=digit%3
#     if r==0:
#         digit=digit
#     elif r==1:
#         digit=digit-1
#     else: 
#         digit=digit+1
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''57.	Replace each digit with nearest multiple of 5. '''
# n=int(input("enter your number "))
# new=0
# while n>0:
#     digit=n%10
#     r=digit%5
#     if r==0:
#         digit=digit
#     elif r==1:
#         digit=digit-1
#     else:
#         digit=digit+1
#     n=n//10
#     new=new*10+digit
# print(new)


'''60.	Replace each digit with sum of digits greater than it in number. '''
# for each digit:
#     compare with all digits
#     take only bigger ones
#     add them
# n=int(input("enter your digit "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     sum=0
#     while x>0:
#         d2=x%10
#         if d2>digit:
#             sum=sum+d2
#         x=x//10
#     digit=sum
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''61.	Replace each digit with sum of digits smaller than it in number. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     sum=0
#     while x>0:
#         d2=x%10
#         if d2<digit:
#             sum=sum+d2
#         x=x//10
#     digit=sum
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''62.	Replace each digit with count of digits equal to it. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         d2=x%10
#         if digit==d2:
#             count=count+1
#         x=x//10
#     digit=count
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''63.	Replace each digit with number of distinct digits. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         d2=x%10
#         if d2!=digit:
#             count=count+1
#         x=x//10
#     digit=count
#     n=n//10
#     new=new*10+digit
# print(new)

'''64.	Replace each digit with sum of digits at even positions. '''
# n=int(input("enter your number "))
# x=n
# pos=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     if pos%2==0:
#         sum=sum+digit
#     digit=sum
#     n=n//10
#     pos=pos-1
# new=0
# while x>0:
#     digit=sum
#     x=x//10
#     new=new*10+digit
# print(new)

'''65.	Replace each digit with sum of digits at odd positions'''
# n=int(input("enter your number "))
# pos=len(str(n))
# x=n
# sum=0
# while n>0:
#     digit=n%10
#     if pos%2!=0:
#         sum=sum+digit
#     n=n//10
#     pos=pos-1
# new=0
# while x>0:
#     digit=sum
#     x=x//10
#     new=new*10+digit
# print(new)

'''66.	Replace each digit with absolute difference from average digit. '''
# n=int(input("enter your number "))
# x=n
# new=0
# div=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# avg=sum//div
# while x>0:
#     digit=x%10
#     digit=abs(digit-avg)
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''67.	Replace each digit with remainder when divided by total digits'''
# n=int(input("enter your number "))
# new=0
# x=n
# td=0
# while n>0:
#     digit=n%10
#     td=td+1
#     n=n//10
# while x>0:
#     digit=x%10
#     r=digit%td
#     digit=r
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''68.	Replace each digit with number of digits greater than it. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit2>digit:
#             count=count+1
#         x=x//10
#     digit=count
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''69.	Replace each digit with number of digits smaller than it. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit2<digit:
#             count=count+1
#         x=x//10
#     digit=count
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''70.	Replace each digit with square of position index. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     sq=pos**2
#     digit=sq
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''71.	Replace digits at prime positions with square of digit. '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             count=count+1
#     if count==2:
#         digit=digit**2
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''72.	Replace digits at composite positions with cube of digit. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             count=count+1
#     if count>2:
#         digit=digit**3
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''73.	Replace digits at square positions with digit + position. '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     root=pos**0.5
#     sq=root**2
#     if pos==sq:
#         digit=digit+pos
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''74.	Replace digits at Fibonacci positions with digit × position. '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     fi=0
#     se=1
#     flag=0
#     while fi<=pos:
#         if fi==pos:
#             flag=1
#         nx=fi+se
#         fi=se
#         se=nx
#     if flag==1:
#         digit=digit*pos
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''75.	Replace digits at triangular positions with digit % position. '''
'''leave'''

'''76.	Replace digits at positions divisible by 3 with digit². '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     if pos%3==0:
#         digit=digit**2
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''78.	Replace digits at even positions with factorial of digit. '''
# n=int(input("enter your number "))
# new=0
# pos=len(str(n))
# while n>0:
#     digit=n%10
#     if pos%2==0:
#         fact=1
#         for i in range(1,digit+1):
#             fact=fact*i
#         digit=fact
#     else:
#         digit=digit
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''79.	Replace digits at odd positions with sum of its factors. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if pos%2!=0:
#         sum=0
#         for i in range(1,digit+1):
#             if digit%i==0:
#                 sum=sum+i
#         digit=sum
#     else:
#         digit=digit
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''80.	Replace digits at positions multiple of 5 with digit reversed (self mapping). '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if pos%5==0:
#         digit=digit
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''81.	Replace digits at positions equal to digit value with 0. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if pos==digit:
#         digit=0
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''82.	Replace digits where position equals count of digits with 9. '''
# n=int(input("enter your number "))
# x=n
# pos=len(str(n))
# new=0
# count=0
# while x>0:
#     digit=x%10
#     count=count+1
#     x=x//10
# while n>0:
#     digit=n%10
#     if pos==count:
#         digit=9
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''83.	Replace digits where position > average position with 7. '''
# n=int(input("enter your number "))
# x=n
# td=0
# pos=len(str(n))
# new=0
# while x>0:
#     digit=x%10
#     td=td+1
#     x=x//10
# while n>0:
#     digit=n%10
#     avg=(td+1)/2
#     if pos>avg:
#         digit=7
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''85.	Replace digits where position is palindrome index with 1. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     rev=0
#     ch=pos
#     temp=pos
#     while temp>0:
#         digit2=temp%10
#         rev=rev*10+digit2
#         temp=temp//10
#         if rev==ch:
#             digit=1
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''84.	Replace digits where position < average position with 2. '''
# n=int(input("enter your number "))
# x=n
# pos=len(str(n))
# new=0
# td=0
# while x>0:
#     digit=x%10
#     td=td+1
#     x=x//10
# while n>0:
#     digit=n%10
#     avg=(td+1)/2
#     if pos<avg:
#         digit=2
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

    
'''90.	Replace digits where digit × position is divisible by 2 with 4.  '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if digit*pos%2==0:
#         digit=4
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''91.	Replace digits appearing once with 0. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==1:
#         digit=0
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''92.	Replace digits appearing twice with 1. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         d2=x%10
#         if digit==d2:
#             count=count+1
#         x=x//10
#     if count==2:
#         digit=1
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''93.	Replace digits appearing more than twice with 9. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count>2:
#         digit=9
#     n=n//10
#     new=new*10+digit
# print(new)

'''94.	Replace digits appearing even number of times with 5. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count%2==0:
#         digit=5
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''95.	Replace digits appearing odd number of times with 7. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count%2!=0:
#         digit=7
#     n=n//10
#     new=new*10+digit
# print(new)

'''96.	Replace digits whose frequency equals digit value with 3. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if digit!=0 and count==digit:
#         digit=3
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''97.	Replace digits whose frequency is prime with 6. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     c2=0
#     for i in range(1,count+1):
#         if count%i==0:
#             c2=c2+1
#     if c2==2:
#         digit=6
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''98.	Replace digits whose frequency is composite with 8. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     c2=0
#     for i in range(1,count+1):
#         if count%i==0:
#             c2=c2+1
#     if c2>2:
#         digit=8
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''99.	Replace digits whose frequency equals total digits with 2. '''
# n=int(input("enter your number "))
# td=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==td:
#         digit=2
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''frequency == prime number AND equals position replace with 0'''
# n=int(input("enter your number "))
# rem=n
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     c2=0
#     for i in range(1,count+1):
#         if count%i==0:
#             c2=c2+1
#     if c2==2 and count==pos:
#         digit=0
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)
            
'''100.	Replace digits whose frequency is maximum with 4. '''
# n = int(input("enter your number "))
# rem = n
# temp = rem
# maxf = 0
# while temp > 0:
#     digit = temp % 10
#     x = rem
#     count = 0
#     while x > 0:
#         if digit == x % 10:
#             count = count + 1
#         x = x // 10
#     if count > maxf:
#         maxf = count
#     temp = temp // 10
# new = 0
# while n > 0:
#     digit = n % 10
#     x = rem
#     count = 0
#     while x > 0:
#         if digit == x % 10:
#             count = count + 1
#         x = x // 10
#     if count == maxf:
#         digit = 4
#     new = new * 10 + digit
#     n = n // 10
# res = 0
# while new > 0:
#     d = new % 10
#     res = res * 10 + d
#     new = new // 10
# print(res)


'''105.	Replace digits whose frequency divides total digits with 3. '''
# n=int(input("enter your digit "))
# td=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if td%count==0:
#         digit=3
#     else:
#         digit=digit
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''106.	Replace digits whose frequency is square number with 5. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     root=count**0.5
#     sq=root**2
#     if sq==count:
#         digit=5
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)
  

'''107.	Replace digits whose frequency is Fibonacci number with 6. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     fi=0
#     se=1
#     flag=0
#     while fi<=count:
#         if fi==count:
#             flag=1
#         nx=fi+se
#         fi=se
#         se=nx
#     if flag==1:
#         digit=6
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''109.	Replace digits whose frequency is even and digit is odd with 1. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count%2==0 and digit%2!=0:
#         digit=1
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''111.	Replace digits where digit² > sum of digits with 0. '''
# n=int(input("enter your number "))
# x=n
# new=0
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit**2>sum:
#         digit=0
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''113.	Replace digits where digit × sum of digits is even with 7'''
# n=int(input("enter your number "))
# new=0
# x=n
# sum=0
# while x>0:
#     digit=x%10
#     sum=sum+digit
#     x=x//10
# while n>0:
#     digit=n%10
#     if digit*sum%2==0:
#         digit=7
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)
    
'''114.	Replace digits where digit + product of digits is odd with 5. '''
# n=int(input("enter your number "))
# x=n
# new=0
# prod=1
# while x>0:
#     digit=x%10
#     prod=prod*digit
#     x=x//10
# while n>0:
#     digit=n%10
#     if digit+prod%2!=0:
#         digit=5
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''115.	Replace digits where digit divides sum of digits with 3. '''
# n=int(input("enter your number "))
# x=n
# new=0
# sum=0
# while x>0:
#     digit=x%10
#     sum=sum+digit
#     x=x//10
# while n>0:
#     digit=n%10
#     if sum%digit==0:
#         digit=3
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''117.	Replace digits where digit equals number of digits with 4. '''
# n=int(input("enter your number "))
# td=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if digit==td:
#         digit=4
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''118.	Replace digits where digit equals count of even digits with 2. '''
# n=int(input("enter your number "))
# x=n
# count=0
# new=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         count=count+1
#     n=n//10
# while x>0:
#     digit=x%10
#     if count==digit:
#         digit=2
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''120.	Replace digits where digit equals sum of squares of digits % 10 with 1. '''
# n=int(input("enter your number "))
# x=n
# new=0
# sum=0
# while n>0:
#     digit=n%10
#     sq=digit**2
#     while sq>0:
#         d2=sq%10
#         sum=sum+d2
#         sq=sq//10
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit==sum%10:
#         digit=1
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''121.	Replace digits where digit equals cube of sum of digits % 10 with 9. '''
# n=int(input("enter your number "))
# x=n
# new=0
# sum=0
# while x>0:
#     digit=x%10
#     sum=sum+digit
#     x=x//10
# while n>0:
#     digit=n%10
#     if digit==(sum**3)%10:
#         digit=9
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''122.	Replace digits where digit equals reversed number’s last digit with 7. '''
# n=int(input("enter your number "))
# x=n
# new=0
# rev=0
# while x>0:
#     digit=x%10
#     rev=rev*10+digit
#     x=x//10
# ld=rev%10
# while n>0:
#     digit=n%10
#     if digit==ld:
#         digit=7
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''123.	Replace digits where digit equals max digit + min digit with 5. '''
# n=int(input("enter your number "))
# x=n
# new=0
# max=0
# min=9
# while n>0:
#     digit=n%10
#     if digit>max:
#         max=digit
#     elif digit<min:
#         min=digit
#     n=n//10
# add=max+min
# while x>0:
#     digit=x%10
#     if digit==add:
#         digit=5
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''125.	Replace digits where digit equals average digit (integer) with 6. '''
# n=int(input("enter your number "))
# x=n
# new=0
# td=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# avg=sum/td
# while x>0:
#     digit=x%10
#     if digit==(int(avg)):
#         digit=6
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''128.	Replace digits where digit equals sum of digits at prime positions with 9. '''
# n=int(input("enter your number "))
# x=n
# new=0
# pos=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             count=count+1
#     if count==2:
#         sum=sum+digit
#     n=n//10
#     pos=pos-1
# while x>0:
#     digit=x%10
#     if digit==sum:
#         digit=9
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''129.	Replace digits where digit equals product of digits at even positions with 4. '''
# n=int(input("enter your number "))
# x=n
# new=0
# pos=len(str(n))
# prod=1
# while n>0:
#     digit=n%10
#     if pos%2==0:
#         prod=prod*digit
#     n=n//10
#     pos=pos-1
# while x>0:
#     digit=x%10
#     if digit==prod:
#         digit=4
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''130.	Replace digits where digit equals count of prime digits with 7. '''
# n=int(input("enter your number " ))
# x=n
# new=0
# c2=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count=count+1
#     if count==2:
#         c2=c2+1
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit==c2:
#         digit=7
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''131.	Replace digits forming arithmetic progression with 1'''
# n = int(input("enter your number "))
# x = n          # store original number
# rev = 0
# count = 0
# # Step 1: reverse the number and count digits
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit   # building reverse number
#     count += 1               # counting digits
#     n //= 10
# # Step 2: check if digits form AP
# temp = rev
# d = 0        # will store common difference
# c = 0        # position counter
# prev = 0
# curr = 0
# while temp > 0:
#     digit = temp % 10
#     if c == 0:
#         prev = digit         # first digit
#     elif c == 1:
#         curr = digit         # second digit
#         d = curr - prev      # find difference
#     else:
#         # check if difference is same
#         if digit - curr != d:
#             d = 999          # mark as NOT AP
#         prev = curr
#         curr = digit
#     temp //= 10
#     c += 1
# # Step 3: build result
# new = 0
# if d != 999:
#     # digits form AP → replace all with 1
#     i = 0
#     while i < count:
#         new = new * 10 + 1
#         i += 1
# else:
#     # not AP → keep original number
#     new = x
# print(new)

'''151.	Replace digits whose position equals their frequency with 9. '''
# n=int(input("enter your number "))
# rem=n
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==pos:
#         digit=9
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''152.	Replace digits whose position is prime AND frequency is even with 1. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     c2=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             c2=c2+1
#     if c2==2 and count%2==0:
#         digit=1
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''153.	Replace digits whose position is composite AND frequency is odd with 2. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     count2=0
#     for i in range(1,pos+1):
#         if pos%i==0:
#             count2=count2+1
#     if count2>2 and count%2!=0:
#         digit=2
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''154.	Replace digits whose frequency equals position² with 3. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==pos**2:
#         digit=3
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)
    
'''155.	Replace digits whose frequency is greater than position with 4. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count>pos:
#         digit=4
#     n=n//10
#     pos=pos=1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''157.	Replace digits whose frequency divides position with 6. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count%pos==0:
#         digit=6
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)
    

'''158.	Replace digits whose position divides frequency with 7. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if pos%digit==0:
#         digit=7
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''159.	Replace digits whose frequency equals sum of digits with 8. '''
# n=int(input("enter your number "))
# z=n
# rem=n
# new=0
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while z>0:
#     digit=z%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==sum:
#         digit=8
#     z=z//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)
    

'''161.	Replace digits whose frequency equals count of prime digits with 2. '''
# n=int(input("enter your number "))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     count2=0
#     for i in range(1,digit+1):
#         if digit%i==0:
#             count2=count2+1
#     if count2==2 and count==count2:
#         digit=2
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''211.	Replace digits where digit > average AND position is prime with 1. '''
# n=int(input("enter your number "))
# x=n
# td=len(str(n))
# new=0
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# avg=sum/td
# while x>0:
#     digit=x%10
#     count=0
#     for i in range(1,td+1):
#         if td%i==0:
#             count=count+1
#     if count==2 and digit>avg:
#         digit=1
#     x=x//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''171.	Replace digits where digit² + position is prime with 1. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     pr=digit**2+pos
#     count=0
#     for i in range(1,pr+1):
#         if pr%i==0:
#             count=count+1
#     if count==2:
#         digit=1
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''172.	Replace digits where digit³ − position is even with 2. '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     cb=digit**3-pos
#     if cb%2==0:
#         digit=2
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(new)

'''173.	Replace digits where digit × position > sum of digits with 3. '''
# n=int(input("enter your number "))
# x=n
# pos=len(str(n))
# new=0
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# while x>0:
#     digit=x%10
#     if digit*pos>sum:
#         digit=3
#     x=x//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''👉 Replace digits where
digit factorial + position is prime with 1
'''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     fact=1
#     for i in range(1,digit+1):
#         fact=fact*i
#     pr=fact+pos
#     count=0
#     for j in range(1,pr+1):
#         if pr%j==0:
#             count=count+1
#     if count==2:
#         digit=1
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''👉 Replace digits where
(sum of digits till that position + current digit) is prime with 7
'''
# n=input("enter your number ")
# sum=0
# new=""
# for i in n:
#     digit=int(i)
#     check=sum+digit
#     count=0
#     for i in range(1,check+1):
#         if check%i==0:
#             count=count+1
#     if count==2:
#         new+="7"
#     else:
#         new+=str(digit)
#     sum=sum+digit
# print(new)
        
'''🧠 Conditions

For each digit (LEFT → RIGHT):

1️⃣ Frequency Condition
Find frequency of current digit in the number
2️⃣ Position Condition
Position starts from 1 (left side)
3️⃣ Compute Value
value = (digit² + position + frequency)
4️⃣ Final Condition

👉 If:

value is PRIME

➡️ Replace digit with 7

👉 Else if:

value is EVEN

➡️ Replace digit with 2

👉 Else:
➡️ Keep digit as it is'''

# n=int(input("enter your number "))
# pos=len(str(n))
# rem=n
# new=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#         value=digit**2+pos+count
#         count=0
#         for i in range(1,value+1):
#             if value%i==0:
#                 count=count+1
#         if count==2:
#             digit=7
#         elif value%2==0:
#             digit=2                             ----> { MY CODE X}
#         else:
#             digit=digit
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

''' correct code '''
# n = input("enter your number ")
# rem = n
# new = ""
# pos = 1

# for d in n:
#     digit = int(d)

#     # frequency
#     freq = 0
#     for x in rem:
#         if int(x) == digit:
#             freq += 1

#     value = digit**2 + pos + freq

#     # check prime
#     count = 0
#     for i in range(1, value+1):           ---> {SIR'S CODE R}
#         if value % i == 0:
#             count += 1

#     if count == 2:
#         new += "7"
#     elif value % 2 == 0:
#         new += "2"
#     else:
#         new += d

#     pos += 1

# print(new)
    
'''174.	Replace digits where digit × position < average digit with 4. '''
# def check(n):
#     x=n
#     pos=len(str(n))
#     new=0
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n=n//10
#     avg=sum/pos
#     while x>0:
#         digit=x%10
#         if digit*pos<avg:
#             digit=4
#         x=x//10
#         pos=pos-1
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# a=int(input("enter your number "))
# result=check(a)
# print(result)

'''175.	Replace digits where digit + position is divisible by 3 with 5. '''
# def check(n):
#     pos=len(str(n))
#     new=0
#     while n>0:
#         digit=n%10
#         if (digit+pos)%3==0:
#             digit=5
#         n=n//10
#         pos=pos-1
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# a=int(input("enter your number "))
# result=check(a)
# print(result)

'''177.	Replace digits where digit % position == digit with 7. '''
# def check(n):
#     pos=len(str(n))
#     new=0
#     while n>0:
#         digit=n%10
#         if digit%pos==digit:
#             digit=7
#         n=n//10
#         pos=pos-1
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# a=int(input("enter your number "))
# result=check(a)
# print(result)
    

'''179.	Replace digits where digit equals factorial of position % 10 with 9. '''
# def check(n):
#     pos=len(str(n))
#     new=0
#     while n>0:
#         digit=n%10
#         fact=1
#         for i in range(1,pos+1):
#             fact=fact*i
#         if fact%10==digit:
#             digit=9
#         n=n//10
#         pos=pos-1
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# a=int(input("enter your number "))
# result=check(a)
# print(result)
        
        
    













    



   









  





        



























    



   








    


    












        














    
    
   
   
  


   

    
  









    


 









    


   
 






















    

    






    


    
        













                

    


                
    





    















    




               
           
            


   





   






        



    
    




    





    









        



     




  

       
            



      





        




    



    
    






       




    





    












 








    









