# Nested Loops (Brute Force) 
'''•	Reverse List '''
# l=[1,2,3,4,5]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

'''•	Rotate Left/Right '''
'''left rotate by 2 and 1'''
# 1
# l=[1,2,3,4,5]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)
'''optimized version'''
# l=[1,2,3,4,5]
# l=l[1:]+l[:1]
# print(l)

# 2
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)
'''optimized version'''
# l=[1,2,3,4,5]
# k=2
# l=l[k:]+l[:k]
# print(l)
# --------------------------------------------------------------------------------------------------
'''right rotaion by 1 and 2'''
# 1
# l=[1,2,3,4,5]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)
'''optimized version'''
# l=[1,2,3,4,5]
# l=l[-1:]+l[:-1]
# print(l)

'''•	Bubble Sort ascending order'''
# l=[1,5,4,2,8]
# for i in range(len(l)-1):
#     for j in range(len(l)-1-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

'''•	Selection Sort '''
# l=[1,5,4,2,8]
# for i in range(len(l)):
    # minimum = i                 min stored current index  like l[0]
#     for j in range(i+1,len(l)):
#         if l[j]<l[minimum]:
#             minimum = j
#     l[i],l[minimum]=l[minimum],l[i]
# print(l)

'''•	Pair Sum '''
# l=[1,2,3,4,5]
# target=7
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j] == target:
#             print((l[i],l[j]))

'''•	Pair Product '''
# l=[10,5,2,6]
# target=30
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]*l[j] == target:
#             print((l[i],l[j]))

'''•	Pair Difference '''
# l=[5,20,3,2,50,80]
# target=78
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if abs(l[i]-l[j]) == target:
#             print((l[i],l[j]))

'''•	Pair with GCD > 1 '''
# l=[2,3,4,9]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         x=l[i]
#         y=l[j]
#         gcd=1
#         small=min(x,y)
#         for k in range(1,small+1):
#             if x%k==0 and y%k==0:
#                gcd=k
#         if gcd>1:
#             print((x,y))

'''•	Pair with Same Last Digit '''
# l=[27,45,17,62,82,97]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]%10 == l[j]%10:
#             print((l[i],l[j]))

# optimized
# l=[27,45,17,62,82,97]
# d={}
# for i in l:
#     temp=i
#     key=temp%10
#     if key in d:
#         print(d[key],temp)
#     else:
#         d[key]=temp

'''•	Pair with Same Digit Sum '''
# l=[123,240,330,411,78]
# for i in range(len(l)):
#     sum1=0
#     x=l[i]
#     while x>0:
#         digit=x%10
#         sum1+=digit
#         x=x//10
#     for j in range(i+1,len(l)):
#         sum2=0
#         y=l[j]
#         while y>0:
#             digit=y%10
#             sum2+=digit
#             y=y//10
#         if sum1==sum2:
#             print((l[i],l[j]))

# optimized
# l=[123,240,330,411,78]
# d={}
# for i in l:
#     temp=i
#     digit_sum=0
#     while temp>0:
#         digit=temp%10
#         digit_sum+=digit
#         temp=temp//10
#     if digit_sum in d:
#         print(d[digit_sum],i)
#     else:
#         d[digit_sum]=i

'''•	Pair with Prime Sum '''
# l=[5,8,11,14]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         pr_check=0
#         for k in range(1,sum+1):
#             if sum%k==0:
#                 pr_check+=1
#         if pr_check==2:
#             print(l[i],l[j])

'''•	Zigzag Array '''
# l=[1,2,3,4,5]
# for i in range(len(l)-1):
#     if i%2==0:
#         if l[i]<l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
#     else:
#         if l[i]>l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
# print(l)
    

'''•	Count Inversions '''
# l=[8,4,2,1]
# inversion_count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             inversion_count+=1
# print(inversion_count)
'''"I fix one element using the outer loop. Then I compare it with every element to its right
using the inner loop. Whenever the left element is greater than the right element, it forms an 
inversion because the larger element appears before a smaller one. I increment the inversion count
for every such pair. Finally, the count gives the total number of inversions."'''



 




