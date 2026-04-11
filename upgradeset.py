'''🧠 SECTION 1: Digit Logic Mastery (Core Strength)'''

'''1.	Replace each digit with its frequency in the number '''
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
#     digit=count
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''2.	Remove digits that appear only once '''
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
#     if count>1:
#         new=new*10+digit
#     n=n//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''3.	Keep only digits whose frequency is prime '''
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
#     for i in range(1,count+1):
#         if count%i==0:
#             count2=count2+1
#     if count2==2:
#         new=new*10+digit
#     n=n//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''4.	Replace each digit with sum of digits to its right '''
# n=int(input("enter your number "))
# new=0
# sum=0
# while n>0:
#     digit=n%10
#     new=new*10+sum
#     sum=sum+digit
#     n=n//10
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''5.	Replace each digit with product of digits to its left '''
# n=int(input("enter your number "))
# new=0
# prod=1
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# while rev>0:
#     digit=rev%10
#     new=new*10+prod
#     prod=prod*digit
#     rev=rev//10
# print(new)

'''🔁 SECTION 2: Position + Digit Combo (VERY IMPORTANT)'''

'''6.	Replace digits at even positions with square of digit '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if pos%2==0:
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

'''7.Replace digits at positions divisible by 3 with sum of digits '''
# n=int(input("enter your number "))
# x=n
# pos=len(str(n))
# new=0
# sum=0
# while x>0:
#     digit=x%10
#     sum=sum+digit
#     x=x//10
# while n>0:
#     digit=n%10
#     if pos%3==0:
#         digit=sum
#     n=n//10
#     pos=pos-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''8.	Replace digits where digit == position with 0 '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if digit==pos:
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


'''9.	Replace digits whose position divides digit with 1 '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if digit%pos==0:
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

'''10.	Replace digits whose digit divides position with 9 '''
# n=int(input("enter your number "))
# pos=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     if pos%digit==0:
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


'''🔢 SECTION 3: Frequency + Nested Loop (Your weak zone)'''
'''11.	Find the first non-repeating digit '''
# n=int(input("enter your number "))
# rem=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# while rev>0:
#     digit=rev%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==1:
#         print(f"the first non-repeating number is {digit}")
#         break
#     rev=rev//10


'''12.	Find the second most frequent digit '''
# n=int(input("enter your number "))
# rem=n
# temp=rem
# max1=0
# while temp>0:
#     digit=temp%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count>max1:
#         max1=count
#     temp=temp//10
# temp=rem
# max2=0
# while temp>0:
#     digit=temp%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count>max2 and count<max1:
#         max2=count
#     temp=temp//10
# temp=rem
# found=0
# while temp>0:
#     digit=temp%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==max2:
#         print(digit)
#         found=1
#         break
#     temp=temp//10
# if found==0:
#     print(" No second most frequent digit ")


'''13.	Replace most frequent digit with least frequent digit '''
# n=int(input("enter your number "))
# rem=n
# z=rem
# max=0
# while z>0:
#     digit=z%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count>max:
#         max=count
#     z=z//10
# z=rem
# min=9
# while z>0:
#     digit=z%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count<min:
#         min=count
#     z=z//10
# z=rem
# new=0
# while z>0:
#     digit=z%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count==max:
#         digit=min
#     z=z//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)


'''14.	Count digits that appear exactly twice '''
# n=int(input("enter your number "))
# rem=n
# count2=0
# while n>0:
#     digit=n%10
#     z=n//10
#     found=0
#     while z>0:
#         d2=z%10
#         if digit==d2:
#             found=1
#         z=z//10
#     if found==0:
#         x=rem
#         count=0
#         while x>0:
#             digit2=x%10
#             if digit==digit2:
#                 count=count+1
#             x=x//10
#         if count==2:
#             count2=count2+1
#     n=n//10
# print(count2)


# --------------------------------------------------------------------------------------------------
# 1.	Find the most frequent digit 
# n=int(input("enter youe number "))
# rem=n
# max=0
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count>max:
#         max=count
#     n=n//10
# print(max)


'''2.	Find the least frequent digit '''
# n=int(input("enter your number "))
# rem=n
# min=9
# while n>0:
#     digit=n%10
#     x=rem
#     count=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             count=count+1
#         x=x//10
#     if count<min:
#         min=count
#     n=n//10
# print(min)


'''3.	Count how many digits have frequency > 1 '''
# n=int(input("enter your number "))
# rem=n
# count=0
# while n>0:
#     digit=n%10
#     x=rem
#     freq=0
#     while x>0:
#         digit2=x%10
#         if digit==digit2:
#             freq=freq+1
#         x=x//10
#     if freq>1:
#         count=count+1
#     n=n//10
# print(count)

# -------------------------------------------------------------------------------------------------------
'''1.	Replace digits whose frequency is prime with 7 '''
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
#     for i in range(1,count+1):
#         if count%i==0:
#             count2=count2+1
#     if count2==2:
#         digit=7
#     n=n//10
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

'''31.	Replace digits where digit² + position is prime with 7 '''
# def check(a):
#     pos=len(str(a))
#     new=0
#     while a>0:
#         digit=a%10
#         add=digit**2+pos
#         count=0
#         for i in range(1,add+1):
#             if add%i==0:
#                 count=count+1
#         if count==2:
#             digit=7
#         a=a//10
#         pos=pos-1
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# n=int(input("enter your number "))
# result=check(n)
# print(result)

'''32.	Replace digits where digit³ + frequency is even with 1'''
# def check(a):
#     rem=a
#     new=0
#     while a>0:
#         digit=a%10
#         x=rem
#         count=0
#         while x>0:
#             digit2=x%10
#             if digit==digit2:
#                 count=count+1
#             x=x//10
#         if (digit**3+count)%2==0:
#             digit=1
#         a=a//10
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# n=int(input("enter your number "))
# result=check(n)
# print(result)

'''33.	Replace digits where digit² + running sum is prime digit = 9 '''
# def check(a):
#     sum=0
#     new=""
#     for i in a:
#         digit=int(i)
#         v=digit**2+sum
#         count=0
#         for j in range(1,v+1):
#             if v%j==0:
#                 count=count+1
#         if count==2:
#             new+="9"
#         else:
#             new+=str(digit)
#         sum=sum+digit
#     return new
# n=input("enter your number ")
# result=check(n)
# print(result)

'''34.	Replace digits where digit + freq + pos is even digit=5 '''
# def check(a):
#     pos=len(str(a))
#     rem=a
#     new=0
#     while a>0:
#         digit=a%10
#         x=rem
#         count=0
#         while x>0:
#             digit2=x%10
#             if digit==digit2:
#                 count=count+1
#             x=x//10
#         if (digit+count+pos)%2==0:
#             digit=5
#         a=a//10
#         pos=pos-1
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# n=int(input("enter your number "))
# result=check(n)
# print(result)

'''35.	Replace digits where (digit × freq) + pos is prime digit= 3 '''
# def check(n):
#     pos=len(str(n))
#     rem=n
#     new=0
#     while n>0:
#         digit=n%10
#         x=rem
#         count=0
#         while x>0:
#             digit2=x%10
#             if digit==digit2:
#                 count=count+1
#             x=x//10
#         pr=(digit*count)+pos
#         count=0
#         for i in range(1,pr+1):
#             if pr%i==0:
#                 count=count+1
#         if count==2:
#             digit=3
#         n=n//10
#         pos=pos-1
#         new=new*10+digit
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# z=int(input("enter your number "))
# result=check(z)
# print(result)

'''36.	Replace digits where digit² + freq² is even '''
# def check(n):
#     rem=n
#     new=0
#     while n>0:
#         digit=n%10
#         x=rem
#         count=0
#         while x>0:
#             digit2=x%10
#             if digit==digit2:
#                 count=count+1
#             x=x//10
#         if (digit**2+count**2)%2==0:
#             new=new*10+digit
#         n=n//10
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# z=int(input("enter your number "))
# result=check(z)
# print(result)

'''38.	Replace digits where digit + pos + running sum is even '''
# def check(n):
#     pos=1
#     new=""
#     sum=0
#     for i in n:
#         digit=int(i)
#         if (digit+pos+sum)%2==0:
#             new+="8"
#         else:
#             new+=str(digit)
#         sum=sum+digit
#         pos+=1
#     return new
# a=input("enter your number ")
# result=check(a)
# print(result)

'''39.	Replace digits where digit × pos × freq is prime '''
# def check(n):
#     pos=len(str(n))
#     rem=n
#     new=0
#     while n>0:
#         digit=n%10
#         x=rem
#         count=0
#         while x>0:
#             digit2=x%10
#             if digit==digit2:
#                 count=count+1
#             x=x//10
#         pr=digit*count*pos
#         count=0
#         for i in range(1,pr+1):
#             if pr%i==0:
#                 count=count+1
#         if count==2:
#             new=new*10+digit
#         n=n//10
#         pos=pos-1
#     res=0
#     while new>0:
#         digit=new%10
#         res=res*10+digit
#         new=new//10
#     return res
# a=int(input("enter your number"))
# result=check(a)
# print(result)

'''21.	Replace digits where running sum is prime '''
# def check(n):
#     new=""
#     sum=0
#     for i in n:
#         digit=int(i)
#         rs=sum+digit
#         count=0
#         for j in range(1,rs+1):
#             if rs%j==0:
#                 count=count+1
#         if count==2:
#             new+="P"
#         else:
#             new+=str(digit)
#         sum=sum+digit
#     return new
# x=input("enter your number ")
# result=check(x)
# print(result)

'''22.	Replace digits where running sum is even '''
# def check(n):
#     new=""
#     sum=0
#     for i in n:
#         digit=int(i)
#         sum=sum+digit
#         if sum%2==0:
#             new+="7"
#         else:
#             new+=str(digit)
#     return new
# a=input("enter your number ")
# result=check(a)
# print(result)
            
'''23.	Replace digits where running sum > 10 '''
# def check(n):
#     new=""
#     sum=0
#     for i in n:
#         digit=int(i)
#         sum=sum+digit
#         if sum>10:
#             new+="B"
#         else:
#             new+=str(digit)
#     return new
# a=input("enter your number ")
# result=check(a)
# print(result)

'''24.	Replace digits where running sum < digit '''
# def check(n):
#     new=""
#     running_sum=0
#     for i in n:
#         digit=int(i)
#         if running_sum<digit:
#             new+="S"
#         else:
#             new+=str(digit)
#         running_sum=running_sum+digit
#     return new
# a=input("enter your number")
# res=check(a)
# print(res)
    
'''25.	Replace digits where running product is prime '''
# def check(n):
#     new=""
#     running_product=1
#     for i in n:
#         digit=int(i)
#         running_product=running_product*digit
#         count=0
#         for j in range(1,running_product+1):
#             if running_product%j==0:
#                 count=count+1
#         if count==2:
#             new+="P"
#         else:
#             new+=str(digit)
#     return new
# a=input("enter your number ")
# res=check(a)
# print(res)

'''digit × running product is even'''
# def check(n):
#     new=""
#     running_prod=1
#     for i in n:
#         digit=int(i)
#         if (running_prod*digit)%2==0:
#             new+="E"
#         else:
#             new+=str(digit)
#         running_prod=running_prod*digit
#     return new
# a=input("enter your number ")
# res=check(a)
# print(res)
    
   


            

        
   

