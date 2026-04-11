# # # what are operators
# # ''' Operators are symbols that perform operations on variables
# # and values. Python has several types of operators for
# # different tasks like arithmetic, comparison, logical operations,
# # and more
# #  Lets see every operators one by one.'''

# # #1-arthemitic operators
# # ''' 
# #  Arithmetic operators perform mathematical operations like
# # addition, subtraction, multiplication, division, etc
# #  There are 7 types of arithmetic operator.
# #  addition +
# #  subtraction -
# #  multiplication *
# #  division /
# #  Floor division //
# #  modulus %
# #  Exponentiation **'''

# # #add example
# # a=5
# # b=20
# # # print(a+b)
# # # print(b-a)
# # # print(a*b)
# # # print(b/a)#it gives anwer in float
# # # print(b//a)#floor division removes decimal value
# # # print(5**2)# 5 ki power 2 answers is 25
# # # print(32%5)# mod means reminder 
# # print(12+4/2)#it follows bodmas first 4 will divided by 2 then addition happens
# # #what is bodmas-multiplication and division happens before addition and substraction
# # # print(25+47)
# # # print(150-89)
# # # print(45+15*2)
# # # print(135*1/60)

# # #assignment operators
# # ''' Assignment operators are used to assign values to variables.
# # Python also provides compound assignment operators that
# # perform operations like addition, subtraction, multiplication,
# # etc
# #  A basic assignment operator is simple =.'''

# # # = assignment operator the variable we are creating it assigns value to it

# # # a = 23
# # # compund assignment operations
# # '''  Compound assignment operator combines arithmetic
# # operations with assignment
# #  But first you have to understand how things work when we
# # reassign variables in python and also reassigning variables
# # with addition, subtraction etc
# #  To understand watch the video carefully
# #  Using compound assignment operators the reassigning
# # works better
# #  += Add and assigD
# #  -= Subtract and assigD
# #  *= Multiply and assignA
# #  /= Divide and assigD
# #  //= Floor divide and assigD
# #  %= modulus and assigD
# #  **= Exponentiation and assign'''

# # # a=20
# # # a=a+20
# # # a=a+40
# # # a=a+60
# # # print(a)this is called reaasignment of value we can do this in python

# # # a=20
# # # a+=20
# # # a+=40
# # # a+=60
# # # # we csn make
# # # a-=
# # # a*=
# # # a%=
# # # a/=
# # # a//=
# # # a**= so these are the compund assignment operators the upper process we do is shortern by these
# # # basically pehle se jo value chal rahi hai usme kuch add kar rha hu jodh rha hu usme kuch bhi plus minus divide 

# # #comparison operators most most imp 
# # '''comparison means to compare between two values for ex- there are two girls 
# # one height is small one height is big i easily compare between them
# # that whose height is big whose is small comparison is done between two or more things
# # in python if i want to compare something there will me two variables more than two variables or values

# #  Comparison operators, also called relational operators, are
# # used to compare two values
# # 5 Comparison operators will always provide Boolean result that
# # is True and False
# # 5 comparison operators are as follow
# # 5 == Equal t<
# # 5 != Not Equal to3
# # 5 > Greater than3
# # 5 < Less than 3
# # 5 >= Greater than or equal t<
# # 5 <= Less than or equal t<
# # 5 Comparison operators will work with numbers but you can
# # use them with strings as well.3
# # 5 Strings will be comparing the Ascii values of string.'''

# # a=12.1# we can compare int and float in python
# # b=12
# # print(a==b)#it checks left or right side value is same if both values is same answer is true else false

# # print(a!=b)#it checks left side and right side value should not be same
# # print(a>b)
# # print(45<67)# bigger than smaller than 
# # print(23>=23)#left side waali jo value hai ya toh wo chhoti ho ya toh wo equal ho jae right side se
# # print(45<=45)#right side waali vaLUE ya toh baadi ya to equals honi chaiye left side se

# # #ascii values is also unicode 
# # print(ord("a"))#unicode me se kuch chizzo ko hi apan ascii values bolte hai
# # print("A">"B")# false because a unicode is 65 and b is 66 basicaaly ord func ascii values decide its answer
# # print("ABC">"ACD")#it compares multi ascii values it checks in basis of precendence first compare with first value then second then third
# # #like this it gives output like a is 65,65 then b is 66 and c is 67 so the condition become false
# # # print("A">34)#it will not work we can compare string with string but we cannot compare string with int

# # #logical operators
# # #  Logical operators in Python are used to combine multiple
# # # conditions and return a Boolean result (True or False)
# # # 5 There are 3 types of logical operator3
# # # 5 and - Return True if both condition are True
# # # 5 or - Return True if at least one condition is True
# # # 5 not - Reverse the boolean value
# # # 5 **important** watch the full video for better understanding.
# # # we combine two comparison operators using logical operator

# # print(123>100 and 34==34 and 45<90 and 12>20)#by applying , it gives sepateraly answer but combining with logical operator
# # # it gives only one true and both the conditions are true and operation combine both and give one answer
# # # and operation say that every operation should come true then only i will work if any one thing is false i will convert everything in into false
# # #break point-if first condition is false then it will not check second or the whole code it will break it and give anwer false


# # #or says if any one condition is true then everything is true

# # print(12!=12 or 45==67 or 10>9)# its true 

# # #not reverse boolean value 
# # print(not 12==12)# not says in my front if any operation is true i will reverse to false and false to true

# # marks=int(input("enter your marks"))
# # print(marks>33)

# # vote=int(input("enter your age"))
# # print(vote>18)

# # a=int(input("enter number"))
# # b=int(input("enter number"))
# # print(a<b)

# # num=int(input("enter number to check"))
# # print(num%4==0)

# # arthemetic questions
# '''Check whether a number is even or odd.

# Check whether a number is divisible by 5.

# Check whether a number is divisible by 3 and 7.

# Find the sum of two numbers and check if it is greater than 100.

# Find the product of two numbers and check if it is even.

# Check whether the difference of two numbers is positive or negative.

# Find the remainder when a number is divided by 4.

# Check whether a number is a multiple of 10.

# Calculate the average of three numbers.

# Check whether a number is a perfect square.'''

# # n=int(input("enter your number"))
# # if n%2==0:
# #     print("even")
# # else:
# #     print("odd")
# # if n%3==0 and n%7==0:
# #     print("divisible")
# # else:
# #     print("not divisible")

# # n=int(input("enter your number"))
# # n2=int(input("enter your number"))
# # if n+n2>100:
# #     print("greater")
# # else:
# #     print("not greater")


# # n=int(input("enter your number"))
# # n2=int(input("enter your number"))
# # if n*n2%2==0:
# #     print("even")
# # else:
# #     print("odd")
# # diff= n-n2
# # if diff>0:
# #     print("posotive")
# # elif diff<0:
# #     print("negative")
# # rem=n%4
# # print(rem)
# # n=int(input("enter your number"))
# # n2=int(input("enter your number"))
# # n3=int(input("enter your number"))
# # avg= n+n2+n3/3
# # print(avg)

# # i=int(input("enter"))
# # if i**i:
# #     print(i,"is a perfect square")

# # num = int(input("Enter a number: "))

# # root = int(num ** 0.5)

# # if root * root == num:
# #     print("Perfect square")
# # else:
# #     print("Not a perfect square")

# # a=int(input("enter number to print"))
# # b=int(input("enter number to print"))
# # print(a%b)

# # a=int(input("enter"))
# # print(a*a)
# a=5678
# print(a%10)#%10 always give last digit 

# # num=int(input("enter"))
# # num=abs(num)
# # digit=int(str(num)[0])
# # print(digit) this always give first digit of a number

# # a=int(input("enter your number "))
# # if a%10==0:
# #     print("multiple")
# # else:
# #     print("not multiple")
# # print(a%10==0)

# # a=int(input("enter your number "))
# # b=int(input("enter your number "))
# # print(2*(a+b))
# # a=int(input("enter your number "))
# # print(a/60)

# a=5
# b=6
# a = a * b
# b = a // b
# a = a // b
# print(a,b)

# #reversing a digit
# # num=int(input("enter a number"))
# # num=abs(num)
# # digit=int(str(num)[0])
# # print(num%10,digit) 



# # num = int(input("Enter a 2-digit number: "))

# # tens = num // 10      # first digit
# # ones = num % 10       # last digit

# # print( ones * 10 + tens)

# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)


# a=int(input("enter"))
# b=int(input("enter"))
# diff=a-b
# diff=abs(diff)
# print("the difference is",diff)

# a=int(input("enter your number"))
# print(a**a%2!=0)

# b=int(input("enter your number"))
# print(b**3%9==0)

# a=int(input("enter your number"))
# b=int(input("enter your number"))
# print((a+b)%2==0)

# a=int(input("enter"))
# print(a%4==0 and a%6==0)
# secondlast=(a//10)%10
# print(secondlast)
# print(a%10==0)

# a=int(input("enter"))
# b=int(input("enter"))
# sq1=a*a
# sq2=b*b
# diff=sq1-sq2
# diff=abs(diff)
# print(diff)-Check if difference of squares of two numbers is positive 1 question solved by myself

# a=int(input("enter"))
# b=int(input("enter"))
# sq1=a*a
# sq2=b*b
# sum=sq1+sq2
# print(sum%2==0)

# a = int(input("Enter a 2-digit number: "))
# a = abs(a)

# print(a % 10 == 0 or a // 10 == 0)

# a=int(input("enter your number"))
# print(a**0.5)

# a=int(input("enter your number"))
# print(a**1/3)
# digit=((a%10)+((a//10)%10)+(a//100))

# print(a%digit)

# v=int(input("enter"))
# dig=v%10
# print(v%dig==0)second question i solved by my self

# num=int(input("enter your number"))
# print((a%10)+((a//10)%10)+(a//10)%3)print(num%9)

# a = int(input("Enter a number: "))
# print((a * a) % 10 == 6)

# a = int(input("Enter a number: "))
# print(a*3%2!=0)

# a = int(input("Enter a number: "))
# b= int(input("Enter a number: "))
# c= int(input("Enter a number: "))
# print((a+b+c)%3==0)


# print(a%2==0 or a%3==0 or a%5==0)
# print((a+b)%4==0)

 

# a=int(input("enter your number"))
# print(a%2==0)

# a=int(input("enter your number"))
# b=int(input("enter your number"))
# diff=a-b
# diff=abs(diff)
# print(diff)
# rev=(diff%10)(diff//10)
# print(rev)


# num = int(input("Enter a 2-digit number: "))
# num = abs(num)

# reverse = (num % 10) * 10 + (num // 10)

# # print((num - reverse) % 2 == 0)
# print(reverse)

# a=int(input("enter your number"))
# b=int(input("enter your number"))
# print(a*b%2==0)

# a=int(input("enter 2 digit number"))
# sum=(a%10+a//10)
# prime = sum > 1 and sum % 2 != 0 or sum == 2
# print(prime)
''' The logic says:
“A number is prime if:
it is greater than 1
AND it is not divisible by 2
OR it is exactly equal to 2” '''

#23 it should divided by its first digit
# 24- it should divided by 2
# for 2 digit number
# a=int(input("enter 2 digit number"))
# digit= a//10
# div=a%digit==0
# print(div)
#for 3 digit number
# a=int(input("enter your 3 number"))
# digit=a//100
# div=digit%a==0
# print(div)

#33.Check if square minus number is even

# a*a-num%2==0

# num=24
# sq=num*num
# min=sq-num
# print(min%2==0)

# num=int(input("enter your number"))
# cu=num**3
# print(cu+num%2!=0)

# a=int(input("enter"))
# print(a%10==0)

# a=int(input("enter"))
# print(a%100==0)

# a=int(input("enter"))
# print(a%25==0)

# a=int(input("enter"))
# print(a%3==1)

# a=int(input("enter"))
# print(a%4==2)

# a=int(input("enter"))
# b=int(input("enter"))
# print(a*a%6==0)

# 41.	Check if sum of numbers is perfect square
# a=int(input("enter your number"))
# sum=a%10+a//10
# sq=(sum**2)

# a=int(input("enter your number"))
# diff=a//10-a%10
# diff=abs(diff)
# print(diff%5==0)

# n=int(input("enter your number "))
# sq=n*n
# print(sq%16==0)

# n=int(input("enter your number "))
# cube=n**3
# print(cube%27==0)

# n=int(input("enter your number "))
# print(n%9==0)

# n=int(input("enter your number "))
# cube=n**3
# sum=cube%10+(cube//10)%10+cube//100
# print(sum%2==0)

# n=int(input("enter your number "))
# m=n*5
# print(m%10==0)

# n=int(input("enter your number "))
# root=n**0.5
# print(root%2==0)

# a=int(input(" "))
# b=int(input(" "))
# print(a//b)

'''armstrong 3 digit number'''
# a=int(input("enter-3-digits-armstrong number"))
# b=(a%10)**3+((a//10)%10)**3+(a//100)**3
# if a==b:
#     print("its an armstrong number")
# else:
#     print("no it is not a armstrong number") 

'''pallindrome 3 digit number'''
# a=int(input("enter-3-digit-number-to-check"))
# rev= (a%10)*10+(a//10)%10
# rev2=rev*10+(a//100)
# if rev2==a:
#     print("your-3-digit number is pallindrome")
# else:
#     print("it's not pallindrome")

'''reverse'''
# a=int(input("enter-3-digit-number-to-check"))
# rev= (a%10)*10+(a//10)%10
# rev2=rev*10+(a//100)
# print(rev2) reversing a digit

'''sum of digits'''
# digit=int(input("enter your 3 digit number only"))
# sum= (digit%10)+((digit//10)%10)+(digit//100)
# print(sum)

'''perfect square'''
# a=int(input("enter number to check"))
# sq=(a**0.5)
# ch=sq**2
# if ch==a:
#     print(f"{a} is a perfect square")
# else:
#     print(f"{a} is not a perfect square")

'''total and percentage of a marks'''
# sub1=int(input("enter marks to check"))
# sub2=int(input("enter marks to check"))
# sub3=int(input("enter marks to check"))
# sub4=int(input("enter marks to check"))
# sub5=int(input("enter marks to check"))
# marks=(sub1+sub2+sub3+sub4+sub5)
# print(f"your total marks is {marks}")
# total=(marks/500*100)
# print(f"your percentage is {total}")

'''converting time into min to hrs then hrs to min'''
# time=int(input("enter your time to check how many hrs"))
# hrs=(time/60)
# print(f"your min to hrs is {hrs}")
# min=(time*60)
# print(f"your hrs to min is {min}")

'''simple interest'''
# principal=int(input("enter amount to check S.I"))
# interestrate=int(input("enter interest rate to check S.I"))
# time=int(input("enter time to check S.I"))
# si=principal*interestrate*time/100
# print(f"your simple interest is {int(si)}")

'''factorial'''
# fact=120-with loop i will do

'''power of a number'''
# a=int(input("enter your number "))
# print(a**3) for good output we use loop

'''perimeter of square'''
# a=int(input("enter side to check perimeter"))
# print(a*4)

'''perimeter of rectangle'''
# a=int(input("enter side to check perimeter"))
# b=int(input("enter side to check perimeter"))
# print(2*(a+b))

'''profit or loss'''
# sp=int(input("enter side to check perimeter"))
# cp=int(input("enter side to check perimeter"))
# if sp-cp and sp>cp:
#     print("you earned profit")
# else:
#     print("you loss")

'''swap case'''
# a=int(input(" "))
# b=int(input(" "))
# a=a*b
# b=a//b
# a=a//b
# print(a,b)

'''converting days into years,weeks,days'''
# a = int(input("Enter days: "))
# years = a // 365
# remaining_days = a % 365
# weeks = remaining_days // 7
# days = remaining_days % 7
# print(years, "years")
# print(weeks, "weeks")
# print(days, "days")

'''calculator'''
# num1=int(input("enter your number "))
# num2=int(input("enter your number "))
# operator=input("enter your operator ")
# if operator=="+":
#     print(num1+num2)
# elif operator=="-":
#     print(num1-num2)
# elif operator=="*":
#     print(num1*num2)
# elif operator=="/":
#     print(num1/num2)
# else:
#     print("invalid")

'''find distance'''
# speed=int(input("enter your speed"))
# time=int(input("enter your time"))
# distance=speed*time
# print(f"your distance you covered is {distance}km")

'''If:
Q1..Basic Salary = ₹20,000
Then (one possible structure):
HRA (40%) 
DA (15%) 
TA (5%) 
Medical (5%) 
Special (10%) 
40% of Basic Salary → if living in non-metro city
50% of Basic Salary → if living in metro city'''

'''
Q2..💼 Real-World Salary Calculation Question
An employee works in a private company and earns a basic monthly salary of ₹30,000.
The company provides the following allowances:
House Rent Allowance (HRA) = 40% of basic salary
Dearness Allowance (DA) = 15% of basic salary
Travel Allowance (TA) = 5% of basic salary
Medical Allowance = ₹1,500 per month
Special Allowance = 10% of basic salary
The company also deducts the following:
Provident Fund (PF) = 12% of basic salary
Professional Tax = ₹200 per month
🔍 Tasks
Calculate the total allowances.
Calculate the gross salary.
Calculate the total deductions.
Find the net (take-home) salary of the employee.'''

# Q2 ANS
# salary=30000
# hra=salary*0.40
# da=salary*0.15
# ta=salary*0.05
# ma=1500
# sa=salary*0.10
# total_allowances=hra+da+ta+ma+sa
# print(f"the total allowances added in your salary is {total_allowances}")
# gross_salary=total_allowances+salary
# print(f"your gross salary will be without deduction is {gross_salary}")
# pf=salary*0.12
# pt=200
# total_deduction=pf+pt
# print(f"your total deduction form gross salary will be {total_deduction}")
# net=gross_salary-total_deduction
# print(f"your net salary will be {net}")

'''sum of first n natural numbers'''
# a=int(input("enter your 2 digit number"))
# if a>0 and a==0 and (float(a)):
#     print("not a natural number")
# else:
#     print(a%10+a//10) perfectly done by loop

'''find remainder without using %'''
# a=27
# b=a//2
# remainder=a-b*2
# print(remainder)

'''41.sum of even numbers	'''
# a=int(input("enter your 2-digit even number"))
# b=int(input("enter your 2-digit even number"))
# if a%2==0 and b%2==0:
#     print(a+b)
# else:
#     print("invalid number") for big condition we need looop

'''compare two lists'''
# a=[1,3,5]
# b=[3,5,7]
# if len(a)==len(b):
#     print("both list are equal")
# else:
#     print("not equal")

'''empty string'''
# a=(input("enter something"))
# if a=="":
#     print("the sring is empty")
# else:
#     print("something is there in string")

'''compare years'''
# year1 = int(input("Enter first year: "))
# year2 = int(input("Enter second year: "))
# if year1 > year2:
#     print("First year is greater")
# elif year2 > year1:
#     print("Second year is greater")
# elif year1==year2:
#     print("both years are equal")
# else:
#     print("invalid")

'''password is valid or not'''
# password=1234
# a=int(input("enter your password to unlock"))
# if a==password:
#     print("welcome")
# else:
#     print("go back")

'''pallindrome'''
# a=int(input("enter-3-digit-pallindrome-number "))
# rev= (a%10)*10+(a//10)%10
# mul=rev*10+a//100
# if a==mul:
#     print("it's a pallindrome number")
# else:
#     print("it's not a pallindrome number")

'''absolute value of a number is greater than 50.'''
# a=int(input("enter your ab value"))
# if a>0 and a>50:
#     print("the absolute value is greater than fifty")
# else:
#     print("not absolute or greater than 50")

'''Determine if a number is divisible by 2, 4, and 8.'''
# a=int(input("enter your number"))
# if a%2==0 and a%4==0 and a%8==0:
#     print("it's divisible")
# else:
#     print("it's not divisible")

'''the sum of digits is divisible by 9'''
# a=int(input(" enter your 2or3 digit number "))
# add= (a%10)+((a//10)%10)+(a//100)
# if add%9==0:
#     print("the sum of digits is divisible by 9")
# else:
#     print("it's not divisible by 9")

'''power of 2 loop needed'''
'''Determine if a number is a single-digit, double-digit, or more'''
# a=int(input("enter to check digits of a number "))
# if a>0 and a<=9:
#     print("the number you have given is single digit")
# elif a>=10 and a<=99:
#     print("the number you have given is double digit")
# elif a>=100:
#     print("the digit is more than these digits")
# else:
#     print("invalid")

'''	Check if a number is within 5 units of 100'''
# a=int(input("enter your number"))
# if a >= 95 and a <= 105:
#     print("the number is within 5 units of 100")
# else:
#     print("it's not ")

'''triangular number'''
# x = int(input("Enter a number: "))
# n = int(((8 * x + 1) ** 0.5 - 1) / 2)
# # if n * (n + 1) // 2 == x:
# #     print("It is a triangular number")
# # else:
# #     print("It is not a triangular number")

'''perfect cube '''
# a=int(input("enter your number to  check perfect cube"))
# b=round(a**(1/3))
# c=b**3
# if a==c:
#     print("it's a perfect cube")
# else:
#     print("it's not a perfect cube") also do this question with loop

'''odd and divisible by 7'''
# a=int(input("enter your number"))
# if a%2!=0 and a%7==0:
#     print("it's odd and divisible by 7")
# else:
#     print("invalid")

'''even and >100'''
# a=int(input("enter your number to check"))
# if a%2==0 and a>100:
#     print("the condition is correct")
# else:
#     print("invalid")

'''Determine if a number ends with digit 0'''
# a=int(input("enter your number"))
# if a%10==0:
#     print("the number ends with zero")
# else:
#     print("it's not")

'''	Check if a number has exactly 3 digits'''
# a=int(input("enter your number"))
# if a>=100 and a<=999:
#     print("the number has 3 digits")
# else:
#     print("it does not has 3 digits")

'''if a number is divisible by all digits from 1to9. pertfectly done by loop'''

'''harshad number it is a fixed digit case for perfectly we use loop'''
# a=int(input("enter your 3 digit number "))
# sum= (a%10)+((a//10)%10)+(a//100)
# if a%sum==0:
#     print("it,s a harshad number")
# else:
#     print("it's not a harshad number")

'''divisible by last digit'''
# a=int(input("enter your number"))
# div=a%10
# if a%div==0:
#     print("yes it's divisible by its last digit")
# else:
#     print("it's not")

'''	Determine if a number is both square and cube.'''
# a=int(input("enter your number "))
# b=a**(1/2)
# c=b**2
# d=round(a**(1/3))
# e=d**3
# if a==c==e:
#     print("the number is both perfect square and cube")
# else:
#     print("it's not")

'''Check if a number is within ±10 of another number.'''
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a >= b - 10 and a <= b + 10:
#     print("The number is within ±10")
# else:
#     print("The number is not within ±10")

'''Determine if a number is greater than the average of two numbers.'''
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c=(a+b)/2
# d=int(input("enter "))
# if d>c:
#     print( "number is greater than the average of two numbers")
# else:
#     print("no") done by myself great work piyush

'''Identify if a number is prime and less than 50.'''
# a=int(input("enter your number"))
# prime = a>2 and a%2!=0 or a==2
# if prime and a<50:
#     print("number is prime and less than 50")
# else:
#     print("it's not")

'''determine if the product of digits is greater than 20.'''
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a*b>20:
#     print("the product of digits is greater than 20")
# else:
#     print("it,s not")

'''	Check if a number contains digit 5.'''
# a=input("enter your number")
# if "5" in a:
#     print("yes it's present ")
# else:
#     print("it's not present")perfectly we need a loop

# a=int(input("enter your 2 digit number "))
# b=(a%10)
# c=(a//10)
# if b==5 or c==5:
#     print("5 is present in then ")
# else:
#     print("it's not present in it")very well done piyush

'''	Determine if a number has repeated digits.'''
# a=int(input("enter your number"))
# b=(a%10)
# c=(a//10)%10
# d=(a//100)
# if b==c or b==d or c==d:
#     print("du")
# else:
#     print("no") perfectly done by loop

'''armstrong'''
# a=int(input("enter your three digit armstrong number"))
# arm=((a%10)**3+((a//10)%10)**3+(a//100)**3)
# if arm==a:
#     print("it's an armstrong number")
# else:
#     print("it's not an armstrong number")

'''dynamic range perfectly done by loop'''
'''square of a number is even'''
# a=int(input("enter your number"))
# square=a**2
# if square%2==0:
#     print("the square of a number is even")
# else:
#     print("it's not even")

'''half of a numbers is int'''
# a=int(input("enter your "))
# print(a%2==0)

'''	Check if a number is less than its reverse'''
# a=int(input("enter 3-digit number"))
# rev=(a%10)*10+(a//10)%10
# rev2=rev*10+(a//100)
# print(rev2)
# if a<rev2:
#     print("number is less than its reverse")
# else:
#     print("number is not less than its reverse") perfectly done by loop

'''pallindrome words'''
# a=input("enter your ")
# b=(a[::-1])
# if b==a:
#     print("it's pallindrome")
# else:
#     print("it's not pallindrome")

'''empty string'''
# a=input("enter ")
# if a==(""):
#     print("it's an empty string")
# else:
#     print("it's not an empty string")

'''string is a pallindrome'''
# a=input("enter your word ")
# b=a[::-1]
# print(b)
# if a==b:
#     print("the string is pallindrome")
# else:
#     print("the string is not pallindrome")

'''Determine if a string length is even or odd'''
# a=input("enter your word ")
# b=len(a)
# if b%2==0:
#     print("the length of string is even")
# else:
#     print("the length of string is odd")

'''Determine if a string contains only alphabets'''
# a=input("enter ").isalpha()
# print(a)

'''	Check if a string contains only digits.'''
# a=input("enter your number ").isdigit()
# print(a)

'''	Identify if a string is alphanumeric.'''
# a=input("enter your number ").isalnum()
# print(a)

'''Check if a string starts with a vowel.'''
# a=input("enter your word ")
# b=(a[0])
# if b in ("a","e","i","o","u") :
#     print("it starts with vowel")
# else:
#     print("it not starts with vowel")

'''	Determine if a string ends with a consonant.'''
# a=input("enter your string")
# b=(a[-1])
# if b not in ("a","e","i","o","u") :
#     print("it's ending with consonant")
# else:
#     print("it's not ending with consonant")

'''Check if a string contains the word "python".'''
# a=input("enter your words ")
# if "python" in a:
#     print("the string contains python")
# else:
#     print("the string does not contains python")excellent work piyush

# '''	Check if a string has at least one digit and one letter.'''
# a=input("enter ").isalnum()
# print(a)

'''Check if the first and last characters are the same.'''
# a=input("enter your word ")
# b=a[0]
# c=a[-1]
# if b==c:
#     print("the first and the last char are same")
# else:
#     print("they are not same")

'''	Check if a string contains exactly 5 characters.'''
# a=input("enter your word")
# if len(a)==5:
#     print("it containes 5 char")
# else:
#     print("its not")

'''	Determine if a string has more than 3 words.'''

# a=input("enter your word")
# if len(a)>3:
#     print("string has more than 3 words")
# else:
#     print("no")

'''Check if a string contains consecutive spaces.'''
# a=input("enter your word ")
# if "  " in a:
#     print("it has consecutive space")
# else:
#     print("no")

'''Check if a string contains both vowels and digits.(loop)'''

'''	Check if a string contains a substring at a specific position.'''
# a = input("Enter your word: ")
# sub = input("Enter substring to check: ")
# if a[2:5] == sub:
#     print("The string contains the substring at the specific position")
# else:
#     print("The string does not contain the substring at that position")

'''Determine if a string contains a valid email symbol (@).'''
# a = input("Enter your word: ")
# if "@" in a:
#     print("it contains special symbol")
# else:
#     print("it doesnt contain")

'''Check if a string contains at least 2 vowels in a row at starting.'''
# a=input("enter your word ")
# b=a[0]
# c=a[1]
# if b in ("aeiou") and c in ("aeiou"):
#     print(" the string contains at least 2 vowels in a row at starting")
# else:
#     print("no")

'''Determine if a string ends with punctuation.'''
# a=input("enter to check ")
# b=a[-1]
# if b in ";:!.":
#     print("it has punchuation mark")
# else:
#     print("no")

'''	Check if a number is even and greater than 50.'''
# a=int(input("enter your number "))
# if a%2==0 and a>50:
#     print("the number you enter is even and greater than 50")
# else:
#     print("it's not")


'''Determine if a string length is even and contains a vowel'''

# a=input("enter your word  ")
# b=len(a)
# if b%2==0 and ("a" in a or "e" in a or "i" in a or "o" in a or "u" in a):
#     print("the word is correct")
# else:
#     print("the word is not correct")

'''	Check if a number is odd or divisible by 3 '''

# a=int(input("enter your number"))
# if a%2!=0 or a%3==0:
#     print("the number is odd or div by 3")
# else:
#     print("it's not ")

'''Identify if a string is palindrome and length > 5'''

# a=input("enter your word ")
# if a[::-1] and len(a)>5:
#     print("the string is palindrome and length > 5")
# else:
#     print("it's not ")

'''	Check if age qualifies for voting and senior benefits.'''
# a=int(input("enter your age"))
# if a>0 and a<18:
#     print("not eligible for voting and senior benefits")
# elif a>=18 and a<=59:
#     print("eligible for voting but no senior benefits")
# elif a>=60 and a<=100:
#     print("age qualifies for voting and senior benefits")
# else:
#     print("invalid")

'''ATM withdrawal validation'''
balance=10000
pin=int(input("enter pin to access your atm "))
if pin==2004:
    print("succesfully logined ")
    atm=int(input("enter your digit 1,2,3 for accessing atm "))
    if atm==1:
     a=int(input("enter amount to withdrawl "))
     b=balance-a
     print(f"{b} balance left {a} amount withdrawled")
    elif atm==2:
     c=int(input("enter amount to deposit "))
     d=balance+c
     print(f"{c} amount deposited current balance is {d}")
    elif atm==3:
     print(f"your current balance is {balance}")
    else:
      print("Invalid")
else:
  print("Invalid pin")
  












        
    
    















    
    
    
































   

"""relational operators><>=<="""
# a=int(input("enter your number "))
# b=int(input("enter your number "))
# print(a>b)

# a=int(input("enter your number "))
# b=int(input("enter your number "))
# print(a==b)
# print(a>=10 and a<=99 )
# print(a>=18)
# print(a>=33)
# print(a>0)
# print(a>15000)
# if a<=2000:
#     print("year is before")
# else:
#     print("year after")
# print(len(a)==8)solved by own proud of you piyush
# print(a>=0 and a<=9)
# print(a>=10 and a<=99)
# print(a>=100 and a<=999)
# print(a!=b)
# print(a>=0)
# print(a<0)
# print(a==0)
# print(f"the speed exceeds limit if you go {a>=60}")
# print(a>=2000, "the discount is applicable")
# print(a>=1000 ,"print baLANCE is sufficient")
# print(a>=10 and a<=50)
# print(a>=b)
# print(a>=175,"cm")
# print(a>=20 and a<=30)
# print(a>0 and a<=10)
# print(a>=90 and a<=100)
# range="1 to 99"
# num1=input("enter your numbers ")
# num2=int(input("enter your numbers "))
# number=(num1<num2 )
# larger=(num1>num2)
# print(larger)
# print(num1>=60 and num1<=100,"you are senior citizen")
# print(num1>500)
# if num1>=9 and num1<=17:
#     print("you are in office hrs")
# else:
#     print("money deducted")
# print(num1>99,"out of range")
# print(num1>10000,"you exceeds credit limit")
# print(num1>=33,"you are pass else fail")
# print(num1>30,"you are out of speed")
# print(num1%4==0,"can be leap candidate")
# print(num1==8,"maximum rating")
# print(num1<800,"the price is droped")
# print(num1==1234,"the user input is valid")
# print(len(num1)==10,"the phone number length is correct")

'''Q1
prepare an login system with username and password and pass length will be 8chr
1 capital , letter , 1 small , 1 digit , and 1 special character tell user
to make details by own'''
# CODE my first project made by me
          #login system
# username=input("create your username" )
# print("username sucessfully created")
# password=input("create your password" )
# print("password is sucessfully created")
# if username==username and password==password:
#     print("welcome to login base enter details")
# login=input("enter your username" )
# login2=input("enter your password" )
# if login==username and login2==password:
#     print("welcome to python ")
# else:
#     print("invalid details")

# a=int(input("enter your number"))
# b=int(input("enter your number"))
# c=int(input("enter your number"))

# print(a>5,"the count limit excedded")
# print(a==7809)
# print(a<10,"the number is boundry value")
# print(a>=90 and a<=100,"you are eligible ")
# print(a>100,"the score is improving")
# print(a+b/2>c) write logic applied good piyush

# n=int(input("enter"))
# # print(n<90,"threshold ")
# # print(n>4,"time exceeded")
# print(n<175,"the height is underlimit")

'''LOGICAL OPERATORS'''
# a=int(input(""))
# b=int(input(""))
# print(a%2==0 and a>=0)
# print(a%2!=0 and a<0)
# print(a%3==0 and a%3==0)
# print(a%7==0 or a%5==0)
# print(a>=18 and b=="india")
# print(a==7890 and b=="user &34")
# print(a>=35 and b>=75,"allowed in exam")
# print(a>=1 and a<=100,"the number is between them")
# print(a%4==0 and a%100!=0)
# print(a=="locked"or a=="failed")
# print( not a%2==0)good effort piyush
# print(not a=="")excellent piyush
# print(not a<0)
# print(not a<50,"extreme")
# print(a>=20 and a<=50,"the speed is in safe range")
# print(a>=75 and b>=40)
# print(a>=500000 and tax=="yes")
# discount_available = input("Is discount available? (yes/no): ")
# coupon_valid = input("Is coupon valid? (yes/no): ")

# print(discount_available == "yes" or coupon_valid == "yes")
# a=int(input(" enter "))
# print( a%3==0 and a%5!=0)
# marks1 = int(input("enter"))

# marks2 = int(input("enter")) 

# marks3 = int(input("enter"))
# print(marks1>=35 and marks2>=35 and marks3>=35,"you passed all three subjects") 

# a=input("enter vowel" ) .strip()
# print(a=="a"or a=="e"or a=="i"or a=="o"or a=="u")

# a=int(input("enter number to check prime"))
# print(a>1 and a%2!=0 or a==2,"your number is prime")

# year=int(input("enter your year"))
# print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


# value=int(input("enter"))
# print(value>=1 and value<=100,"valid value")
# a=int(input("enter"))
# b=int(input("enter")) 
# print(a>=0 and b>=0,"the number is positive")
# print(a<0 and b>0,"a is negative")
# print(a>0 and b>0)
# print(a>=35 or b>=95,"pass or fail")
# print(a=="account verifie" and a=="active")
# range= 50 to 100
# print(a <= 50 or a >= 100)
# print(a>20 and a<30,"the temperature is normal")
# print(a<0 and a>100,"the marks are invalid")
# user=input("are you blocked-yes/no").strip()
# user2=input("are you inactive-yes/no").strip()
# print(user=="yes" or user2=="yes")
# a=int(input("enter your number"))
# print(a%2==0 and a%3==0 and a%5==0)
# print(a==56789,"the login is allowed")
# if a>10 and a<100:
#     print("the value is accepted")
# else:
#     print("the value is not accepted")
# print(a<18,"the age is not acceptable")
# print(a==90,"the acceses granted")
# print(a>100,"the scored is improved")
# print(a=="python","the condition is satisfied")
# print(a.isdigit())
# print(not int(a**0.5)**2==a)

'''ASSIGNMENT OPERATORS'''
# balance=5000


# b=int(input("enter your number"))
# b=int(input("enter your number"))
# a+=10
# print(a)
# a-=5
# a*=2
# a/=2
# a+=b
# a*=3
# a-=(a*20//100)finally solved after 30 mins
# print(a)
# a+=(a*30//100)
# print(a,"30% salary increased")
# a+=balance
# print(f"your amount is deposited your current balance is {a}")
# balance-=a
# print(f"withdrawl successfyll your current amount is {balance}")
# a+=1
# print(a)
# a-=1
# print(a)
# a=23
# print(a//10+a%10)
'''accumulate sum,accumulate product and composite numbers will be done by loop'''
# amount=70000
# a=int(input("enter your number"))
# amount+=a
# print(amount)

# value=600
# value+=value
# print(value)

# amount=50000
# amount+=(amount*50//100)
# print(amount)

# amount=80000
# amount-=(amount*10/100)
# print(amount) sub tax

# amount=40000
# amount+=(amount*20/100)
# print(amount)

'''MEMBERSHIP OPERATORS'''

# a="python"
# print("y" in a)

# a="hello my name is python"
# print("name" in a)

# a=[1,3,4,6,8,9]
# print(1 in a)

# a=(23,56)
# print(56 in a)

# a = {
#     "name": "Alice",
#     "age": 20,
#     "city": "Delhi",
#     "course": "Python"
# }
# print("city" in a)dictonary

# a=[4,5,6,8]
# print(10 not in a)

# a=input("enter ch").strip().lower()
# print(a in "aeiou")

# a=input("enter to check ").strip()
# print("123" in a)-perfectly done by loop

# user=["user@1","user@2","user@3","user@4"]
# username=input("enter your username to check answer in true/false").strip()
# print(username in user) kya username input me user waali value aa rahi hai to check exists

# cart=["football","basketball","cricket kit","hockey set","golf set"]
# check=input("enter items to check").strip()
# print(check in cart) if i have to take out more than 2 items and a list is long than use loop
   
# colour=["red","blue","white","black"]
# checkcolour=input("enter colour to check").strip()
# print(checkcolour in colour)  

# records=["piyush","aadarsh","mohit","rahul","rohan","raj"]
# check=input("enter your name to check  " )
# print(check in records)  

# id=[121,45,67,23,45,7,8,90,43,12,101,123]
# check=int(input("enter id to check if exist"))
# print(check in id) learning to check errors 

















