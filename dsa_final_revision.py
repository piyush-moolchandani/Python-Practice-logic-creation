'''•	Reverse Array '''
# l = [1,2,3,4,5,6,7]
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right] = l[right],l[left]
#     left+=1
#     right-=1
# print(l)

'''•	Rotate Array 
•	Rotate Array by K 
Right
'''

# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right] = l[right],l[left]
#         left+=1
#         right-=1
# l = [1,2,3,4,5]
# k = 3
# k = k%len(l)
# reverse(l,0,len(l)-1)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# print(l)

'''•	Rotate Array by K 
left'''
# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l = [1,2,3,4,5]
# k = 3
# k = k%len(l)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# reverse(l,0,len(l)-1)
# print(l)

'''•	Move Zeroes '''
# l=[1,0,2,0,3,0]
# left = 0
# for right in range(len(l)):
#     if l[right]!=0:
#         if left!=right:
#             l[left],l[right]=l[right],l[left]
#         left+=1
# print(l)
