'''•	Prime Number '''
# n = int(input("enter your number "))
# prime_count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         prime_count+=1
# if prime_count == 2:
#     print("prime")
# else:
#     print("not prime")

'''optimized approach'''
# n = int(input("enter your number "))
# if n<2:
#     print('prime')
# else:
#     prime = True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             prime = False
#             break
#     if prime:
#         print('prime')
#     else:
#         print('not prime')


'''•	Armstrong Number '''
# n = int(input("enter your number "))
# x = n
# power = len(str(n))
# digit_sum=0
# while n>0:
#     digit=n%10
#     digit_sum+=digit**power
#     n=n//10
# if digit_sum == x:
#     print('Armstrong')
# else:
#     print('Not Armstrong')
    

'''•	Palindrome Number '''
# n = int(input("enter your number "))
# x = n
# rev = 0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if x == rev:
#     print('palindrome')
# else:
#     print('not palindrome')


'''•	Happy Number '''
# n = int(input("enter your number "))
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
# if n== 1:
#     print('Happy')
# else:
#     print('Not happy')


        


   




    