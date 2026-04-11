''' basics of for loop'''
# for i in "python":
#     # print(i*1)
#     # print(i*2)
#     # print(i*3)
#     print(i)
'''it will not work with int because it is not iterable'''

'''list for loop output'''
# for i in [10,20,30,'python','java']:
#     print(i)

'''tuple for loop output'''
# for i in (10,20,30,'python','java'):
#     print(i)

'''set for loop output it has randomed output no formation immutable'''
# for i in {10,20,30,'python','java'}:
#     print(i)

'''frozen set it has also randomized output it is muttable'''
# for i in ({10,20,30,'python','java'}):
#     print(i)

'''dictonary'''
# a={'name': 'piyush', 'age': '22' , 'qual' : 'bcom'}
# for i in a:
#     print(i) it returns keys

# for i in a.keys():
#     print(i) it also returns keys

# for i in a.values():
#     print(i) it returns values

# for i in a.items():
#     print(i) it returns both key and value pair 

# for k,v in a.items():
#        print('my key is',k)
#        print('my value is',v) for taking out key value as different variable 

'''range (use to generate collection)'''
# a=range(10)
# print(a)
# it will return like (0,10) because no data type was defined

# a=list(range(10))
# print(a)
# in this return 0 to 9 in list because data type is defined


'''for loop and range function together'''
# n=int(input("enter "))
# sum=0
# for i in range (1,n+1):
#     sum=sum+i
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end='=')
# print(sum)

'''even number'''
# n=int(input("enter "))
# sum=0
# for i in range (1,n+1):
#     sum=sum+2*i
#     if i<n:
#         print(2*i,end='+')
#     else:
#         print(2*i,end='=')
# print(sum)

'''odd number'''
# n=int(input("enter "))
# sum=0
# for i in range (1,n+1):
#     sum=sum+(2*i-1)
#     if i<n:
#         print((2*i-1),end='+')
#     else:
#         print((2*i-1),end='=')
# print(sum)

'''upto n even no.'''
# n=int(input("enter "))
# sum=0
# for i in range(2,n+1,2):
#     sum=sum+i
#     print(sum,end=' ')

'''for loop star pattern 1'''
# n=int(input("enter "))
# for i in range (1,n+1):
#     print('*'*i+' '*(n-i))


'''for loop star pattern 2'''
# n=int(input("enter "))
# for i in range (1,n+1):
#     print(' '*(n-i)+i*'*')

'''for loop star pattern 3'''
# n=int(input("enter "))
# for i in range (1,n+1):
#     print(' '*(n-i)+i*'* ') 

'''for loop pattern 4'''
# n=int(input("enter "))
# for i in range (0,n):
#     print('* '*(n-i)+' '*i) 

'''for loop pattern 5'''
# n=int(input("enter "))
# for i in range (0,n):
#     print(' '*i+'*'*(n-i))

'''for loop pattern 6'''
# n=int(input("enter "))
# for i in range (0,n):
#     print(' '*i+'* '*(n-i))

'''count total vowels and consonent in string'''
# n=input("enter ")
# v=0
# c=0
# for i in n:
#     if i.isalpha():
#         if i in ['a','e','i','o','u','A','E','I','O','U']:
#             v=v+1
#         else:
#             c=c+1
# print("Total no of vowel char -",v)
# print('Total no of consonent char -',c)
''' space ascii value is 32'''

'''acscii number is in inside keyboard for pc understand '''
# ch='A'
# print(ord('A')) FOR checking ascii value of character 

# x=65 
# print(chr(x)) for checking character from ascii value 

'''increament in alphabet'''
# ch='A'
# ch=chr(ord(ch)+1)
# print(ch)

'''pattern 1 '''
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#      print('*',end=' ')
#     print()

'''pattern 2'''
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#      print('*',end=' ')
#     print()

'''pattern 3 1234'''
n=4
# for i in range(1,n+1):
#     x=1
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=x+1
#     print()

'''pattern 4 odd number'''
# n=4
# for i in range(1,n+1):
#     x=1
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=x+2
#     print()

'''pattern 5 even number'''
# n=4
# for i in range(1,n+1):
#     x=2
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=x+2
#     print()

'''pattern 6 1 to 10'''
# n=4
# x=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=x+1
#     print()

'''pattern 7 odd'''
# n=4
# x=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=x+2
#     print()

'''pattern 8 even'''
# n=4
# x=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=x+2
#     print()

'''pattern 9 abcd'''
# n=4
# for i in range(1,n+1):
#     x='A'
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=chr(ord(x)+1)
#     print()


'''pattern 10 abcd'''
# n=4
# x='A'
# for i in range(1,n+1):
#     for j in range(1,i+1):
#      print(x,end=' ')
#      x=chr(ord(x)+2)
#     print()
# square bracket is also a character 

