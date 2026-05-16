'''41.	Reverse a list '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)
    
'''42.	Rotate list left by 1 '''
# l=[1,2,3,4]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)

'''43.	Rotate list right by 1 '''
# l=[1,2,3,4]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)

'''44.	Rotate list by k positions '''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)

'''Rotate list right by k8 positions'''
# l=[1,2,3,4,5]
# k=8
# k=k%len(l)
# for i in range(k):
#     lv=l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=lv
# print(l)

'''45.	Move all zeros to end '''
# l=[1,0,2,0,3,0,4,0,5,0]
# pos=0
# for i in range(len(l)):
#     if l[i]!=0:
#         l[pos],l[i]=l[i],l[pos]
#         pos+=1
# print(l)


'''47.	Separate even and odd numbers '''
# l=[1,2,3,4,5,6,7,8]
# pos=0
# for i in range (len(l)):
#     if l[i]%2==0:
#         l[pos],l[i]=l[i],l[pos]
#         pos+=1
# print(l)

'''48.	Sort list (without using sort) –(ascending,descending both)'''
# ascending order small to big
# l=[8,9,3,4,5,6,7,2,1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)

# descending order
# l=[8,9,3,4,5,6,7,2,1]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         x=l[i]
#         l[i]=l[i+1]
#         l[i+1]=x
# print(l)

'''49.	Merge two lists '''
# l=[1,2,3]
# l2=[4,5,6]
# for i in l2:
#   l.append(i)
# print(l)

'''52.	Find pair with given sum '''
# l=[1,2,3,4,5]
# given_sum=7
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==given_sum:
#            print((l[i],l[j]))

'''53.	Find all pairs with sum = k '''
# same solution

'''54.	Find maximum difference between elements '''
# l=[1,15,3,4]
# large=l[0]
# small=l[0]
# for i in l:
#     if i>large:
#         large=i
#     elif i<small:
#         small=i
# maximum_diff=large-small
# print(maximum_diff)

'''56.	Find longest increasing sequence '''
# l=[1,2,3,1,2,3,4,0]
# current=1
# maximum=1
# for i in range(len(l)):
#     for j in range(i+i,len(l)):
#         if l[j]>l[i]:
#             current+=1
#         else:
#             if current>maximum:
#                 maximum=current
#             current=1
# if current>maximum:
#     maximum=current
# print(maximum)


'''58 Replace element with next greater element'''
# l=[4,5,2,10]
# l2=[]
# for i in range(len(l)):
#     found=-1
#     for j in range(i+1,len(l)):
#         if l[j]>l[i]:
#             found=l[j]
#             break
#     l2.append(found)
# print(l2)

'''59.	Replace element with previous smaller element '''
# l=[4,2,5,1,6,3]
# l2=[]
# for i in range(len(l)):
#     found=-1
#     for j in range(i-1,-1,-1):
#         if l[j]<l[i]:
#             found=l[j]
#             break
#     l2.append(found)
# print(l2)

'''60.	Find equilibrium index (left sum = right sum)'''
# l=[1,3,5,2,2]
# for i in range(len(l)):
#     left=0
#     right=0
#     for j in range(0,i):
#         left=left+l[j]
#     for k in range(i+1,len(l)):
#         right=right+l[k]
#     if left==right:
#         print(i)

''''''

    

