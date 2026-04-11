'''higher order functions: passing function under function is called higher order function'''
# types of hof- map ,filter ,reduce,lambda,decorators (lamda doesnt comes under higher order function)
# map
'''map'''
'''if total no of input is total no of output is called map (map creates object which is a memory address and python checks that)'''
# syntax:-
# iterable1(l1)
# iterable2(l2)...multiple

# def fun_name(1,2,3,...):
#     fun_body
# res=map(fun_name,iterable1,iterable2,....)
# print(list(res)) 

'''map questions square of a list'''
# l=[1,2,3,4,5,6]
# def sq(n):
#     return n**2
# res=map(sq,l)
# print(list(res))
'''add 5'''
# l=[1,2,3,4,5,6]
# def sq(n):
#     return n+5
# res=map(sq,l) 
# print(list(res))

# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]
# l3=[1,2,3]
# def add(n1,n2,n3):
#     return n1+n2+n3
# res=list(map(add,l1,l2,l3))
# print(res) in third list it wont find any element to add so map break the iterations and give only 3 outputs


'''filter'''
# syntax:-
# iterable only one iterable it wont support multiple iterable
# def fun_name(n):
#     fun_body
# res=filter(fun_name,iterables)
# print(list(res))

'''questions of filter'''
'''if total no of input is equals to total no of output or less than input is called filter'''
# l=[1,2,3,4,5,6,7,8,9,10]
# def even(n):
#     if n%2==0:
#         return n
# res=list(filter(even,l))
# print(res)

# l=[1,2,3,4,5,6,7,8,9,10]
# def greater(n):
#     if n>5:
#         return n
# res=list(filter(greater,l))
# print(res)

# l=[1,2,3,4,5,6,7,8,9,10]
# def sorted(n):
#     if n%2!=0:
#         return n
# res=list(filter(sorted,l))

# def sorted(n):
#     if n%2==0:
#         return n
# res2=list(filter(sorted,l))
# print(res+res2)

# l=[1,0,2,0,3,0,4,0]
# def out(n):
#     if n==0:
#         return n
# res=list(filter(out,l))

# l=[1,0,2,0,3,0,4,0]
# def out(n):
#     if n!=0:
#         return n
# res2=list(filter(out,l))
# print(res2+res)

# l=[1,0,2,0,3,0,4,0]
# def nonzero(n):
#     if n!=0:
#         return n
# x=len(l)
# res=list(filter(nonzero,l))
# y=len(res)
# result=res+[0]*(x-y)
# print(result)

'''reduce'''
'''multiple inputs but single output is called reduce'''
# import functools
from functools import reduce
# syntax-
# iterable
# def fun_name(n1,n2):
#     fun_body
# res=reduce(fun_name,iterable,initial value(optional))
# print(res)

# l=[1,2,3,4,5]
# def sum(n1,n2):
#     return n1+n2
# res=reduce(sum,l) ye iteration se 2 value se nikalega
# res=reduce(sum,l,0) 0 is initial dena hai toh do nahi to mat do ya se iteration se 1 value nikalega
# print(res)
'''max'''
# l=[10,30,20,15,25,55,40]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# res=reduce(max,l)
# print(res)
'''min'''
# l=[10,30,20,15,25,55,40]
# def min(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# res=reduce(min,l)
# print(res)

'''find average'''
# l=[1,2,3,4,5]
# def sum(n1,n2):
#     return n1+n2
# res=reduce(sum,l)
# def len(x,y):
#     return x+1
# len=reduce(len,l,0)
# avg=res/len
# print(avg)

# ----------------------------------------------------------------------------------------------------------------
'''lambda'''
'''only while loop is not work under it '''
'''it doesnt have any name it is a anonymous function jiska koi naam nahi hota hai'''
# syntax-
# lambda variables:expression (lambda is a keyword and we can pass n no of variables: single line expression)
# we will not use return in it it returns by default value only (it by default gives expression output)
'''example'''
# var=lambda x,y:x+y
# n=(var(10,20))
# print(n)

# var=lambda x:x**2
# n=int(input("enter "))
# x=(var(n))
# print(x)

# syntax lamda if else:-
# lamda variables:result if true if condition else result if false
'''even odd using lambda'''
# res=lambda n:'even' if n%2==0 else 'odd'
# n=int(input("enter "))
# print(res(n))

# res=lambda n:"logined" if n==7890 else "invalid"
# n=int(input("enter your password "))
# print(res(n))

'''lambda with map filter reduce'''
'''using eval () '''
# x=eval(input("enter any value"))
# print(x,type(x))

'''map with lambda'''
# print(list(map(lambda n: n**2,eval(input("enter your list")))))
# print(list(map(lambda x:x+5,eval(input("enter ")))))
'''add 3 list'''
# print(list(map(lambda x1,x2,x3:x1+x2+x3,eval(input("enter "),eval(input("enter "),eval(input('enter')))))))



''' filter with lambda '''
# even
# l=[1,2,3,4,5,6,7,8]
# res=list(filter(lambda n:n if n%2==0 else None,l))
# print(res)
'''odd and even with map we can use filter also'''
# l=[1,2,3,4,5,6,7,8]
# res=list(map(lambda n:'even' if n%2==0 else 'odd',l))
# print(res)

'''in a list first odd then even'''
'''in a list make output first numbers then zeros'''

'''lambda with reduce'''



'sabse bada number kon h. with reduce?'
from  functools import reduce 
# a=[20,30,40,50]
# result=reduce(lambda x,y: x if x>y else y ,a)
# print(result)




'sabse chota number kon h. with reduce?'
# a=[20,30,40,50]
# result=reduce(lambda x,y: x if x<y else y,a)
# print(result)


#decorator
'''need-without changing internall code change the behaviour of code is called 
decorator '''
''' it is a special type of higher order function which returns function only'''
# syntax-
# decorator(parameter):
#     def inner(parameters)
#        body
#     return inner
#     return function
# def main_func (parameter):
#     body
# decorator(main func)



'random understanging by decorator'
# def outer(var):
#     def inner():
#         var()
#     return inner
# def show():
#     print("from show function")
# res=outer(show)
# res()



''

# def outer(var):
#     def inner():
#         var()
#     return inner
# @outer
# def show():
#     print("from show function")
# show()
# res=outer(show)
# res()





# def outer(var):
#     def inner():
#         print("hello")
#     return inner
# @outer
# def show():
#     print("from show function")
# show()



'Aankho ka dhokha from help of decorator'
# def outer(var):
#     def inner(a,b,c):
#         print("hello")
#     return inner
# @outer
# def show(x,y,z):
#     print("from show function")
# show(2,3,4)




# def outer(var):
#     def inner(a,b,c):
#         a=a+5
#         b=b+2
#         c=c+2
#         var(a,b,c)
#     return inner
# @outer
# def show(x,y,z):
#     print(x+y+z)
# show(2,3,4)



