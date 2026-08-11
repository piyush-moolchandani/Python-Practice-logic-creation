'''•	Reverse Array '''
# l=[1,2,3,4,5,6]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

'''optimized approach using two pointers'''
# l=[1,2,3,4,5,6]
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# print(l)
# ----------------------------------------------------------------------------------------------
'''•	Rotate Array '''
# l=[1,2,3,4,5]
# fi = l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)

'''optimized aprroach right '''
# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4,5,6]
# k=3
# k=k%len(l)
# reverse(l,0,len(l)-1)
# reverse(l,0,k-1)
# reverse(l,3,len(l)-1)
# print(l)

'''optimized aprroach left '''
# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4,5,6,7]
# k=2
# k=k%len(l)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# reverse(l,0,len(l)-1)

''' right rotate only no k '''
# def rev(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4]
# rev(l,0,len(l)-1)
# rev(l,1,len(l)-1)
# print(l)


'''left rotate only no k'''
# def rev(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4]
# rev(l,0,len(l)-1)
# rev(l,0,len(l)-2)
# print(l)
# --------------------------------------------------------------------------------------------------
'''•	Move Zeroes '''
# l=[1,0,2,0,3,0,4]
# left = 0
# for right in range(len(l)):
#     if l[right]!=0:
#         if l[left]!=l[right:]:
#             l[left],l[right]=l[right],l[left]
#         left+=1
# print(l)
# ----------------------------------------------------------------------------------------------------
'''•	Merge Two Sorted Arrays '''
# l1=[1,3,5]
# l2=[2,4,6]
# l3=[]
# i=0
# j=0
# while i<len(l1) and j<len(l2):
#     if l1[i]<l2[j]:
#         l3.append(l1[i])
#         i+=1
#     else:
#         l3.append(l2[j])
#         j+=1
# while i<len(l1):
#     l3.append(l1[i])
#     i+=1
# while j<len(l2):
#     l3.append(l2[j])
#     j+=1
# print(l3)
# --------------------------------------------------------------------------------------------------
'''pair sum/Two sum'''
# l=[4,7,2,3]
# target = 10
# d={}
# for i in l:
#     need = target-i
#     if need in d:
#         print((need,i))
#     d[i]=1

''' two sum but in output indices'''
# l = [4, 7, 2, 3]
# target = 10
# d = {}
# for index, i in enumerate(l):
#     need = target - i
#     if need in d:
#         print((d[need], index))
#     d[i] = index

'''for index, value in enumerate(l):
ok so enumerate gives indices with their respected values for example it will create 
a pair like this 
(0,4),(1,7),(2,2),(3,3)'''

