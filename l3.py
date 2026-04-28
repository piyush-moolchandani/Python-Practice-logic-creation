'''Find third largest element'''
# l=[1,2,3,4,5,6,7,8,9]
# large=0
# se_large=0
# th_large=0
# for i in l:
#     if i>large:
#         th_large=se_large
#         se_large=large
#         large=i
#     elif i>se_large and i!=large:
#         th_large=se_large
#     elif i>th_large and i!=se_large and i!=large:
#         th_large=i
# print(th_large)

'''Find third smallest element'''
# l=[1,2,3,4,5,6,7,8,9]
# small=9
# se_small=9
# th_small=9
# for i in l:
#     if i<small:
#         th_small=se_small
#         se_small=small
#         small=i
#     elif i<se_small and i!=small:
#         th_small=se_small
#         se_small=i
#     elif i<th_small and i!=se_small and i!=small:
#         th_small=i
# print(th_small)


'''Find average of even numbers only'''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     if i%2==0:
#         l2.append(i)
# sum=0
# for i in l2:
#     sum=sum+i
# avg=sum/len(l2)
# print(avg)

'''Print numbers greater than both neighbors'''
# l=[2,5,1,7,3,6,4]
# l2=[]
# for i in range(1,len(l)-1):
#     if l[i]>l[i-1] and l[i]>l[i+1]:
#         l2.append(l[i])
# print(l2)

'''Print numbers smaller than both neighbors'''
# l=[4,1,2,5,3,7]
# for i in range(1,len(l)-1):
#     if l[i]<l[i-1] and l[i]<l[i+1]:
#         print(l[i])

'''Remove all duplicate values'''
# l=[1,1,2,3,4,4]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l2)

# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         l2.append(i)
# print(l2)

'''Keep only repeated values'''
# l=[1,1,2,3,4,4,5,5,5,5]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>=2:
#         l2.append(i)
# print(l2)

'''Replace multiples of 3 with -3'''
# l=[1,3,4,6,44,15,9,10]
# l2=[]
# for i in l:
#     if i%3==0:
#         i=-3
#     else:
#         i=i
#     l2.append(i)
# print(l2)
    
'''Count numbers in range 10 to 50'''
# l=[12,45,6,78,34,88,546,44]
# count=0
# for i in l:
#     if i>10 and i<50:
#         count=count+1
# print(count)

'''Replace negative odd numbers with 0'''
# l=[1,2,-3,-4,5,6,-7,8,-9]
# l2=[]
# for i in l:
#     if i<0 and i%2!=0:
#         i=0
#     l2.append(i)
# print(l2)
    

'''21.	Replace each element with double value '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     l2.append(i*2)
# print(l2)    

'''25.	Replace even numbers with next even number '''
# l=[2,8,16,4]
# l2=[]
# for i in l:
#     if i%2==0:
#         l2.append(i+2)
#     else:
#         l2.append(i)
# print(l2)

'''26.	Replace odd numbers with previous odd number '''
# l=[1,2,3,4,5,6,7,8]
# l2=[]
# for i in l:
#     if i%2!=0:
#         l2.append(i-2)
#     else:
#         l2.append(i)
# print(l2)

# '''31.	Find all elements with highest frequency '''
# l=[1,1,2,2,3]
# max=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>max:
#         max=count
# l2=[]
# for i in l:
#     c2=0
#     for j in l:
#         if i==j:
#             c2=c2+1
#     if max==c2 and i not in l2:
#         l2.append(i)
# print(l2)
       

'''32.	Find all elements with lowest frequency '''
# l=[4,4,7,7,7,8,8,9,9,9,9]
# min=9
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count<min:
#         min=count
# l2=[]
# for i in l:
#     c=0
#     for j in l:
#         if i==j:
#             c=c+1
#     if min==c and i not in l2:
#         l2.append(i)
# print(l2)


'''33.	37.	Find first repeating element '''
# l=[4,7,7,7,8,8,9,9,9,9]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         print(i)
#         break

'''38.	Find last repeating element '''
# l=[4,7,7,7,8,8]
# for i in range(len(l)-1,-1,-1):
#     count=0
#     for j in l:
#         if l[i]==j:
#             count=count+1
#     if count>1:
#         print(l[i])
#         break

'''41.	Rotate left by 2 positions '''
# l=[1,2,3,4,5,6]
# k=2
# for j in range(k):
#     fi=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=fi
# print(l)

'''right'''
# l=[1,2,3,4,5,6]
# k=2
# for j in range(2):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''43.	Reverse only first half of list(even length) '''
# l=[1,2,3,4,5,6]
# l2=l[0:3]
# l3=l[3:6]
# l4=[]
# for i in range(len(l2)-1,-1,-1):             --->excellent work great logic if len(l)is know
#     l4.append(l2[i])                         --->else not known use len(l)//2 but very brilliant work piyush
# print(l4+l3)
# =====================================================================================================
# l= [1,2,3,4,5,6]
# mid = len(l) // 2
# l2 = l[0:mid]
# l3 = l[mid:]
# l4 = []
# for i in range(len(l2)-1, -1, -1):
#     l4.append(l2[i])
# print(l4 + l3)
# =====================================================================================================
# l = [1,2,3,4,5,6]
# mid = len(l) // 2
# l2 = []
# for i in range(mid-1, -1, -1):
#     l2.append(l[i])
# for i in range(mid, len(l)):
#     l2.append(l[i])
# print(l2)
    

'''Reverse only first half of list(odd length) '''
# l=[1,2,3,4,5]
# mid=len(l)//2
# l2=l[0:mid]
# l3=l[mid:]
# l4=[]
# for i in range(len(l2)-1,-1,-1):
#     l4.append(l[i])
# print(l4+l3)

'''44.	Reverse only second half of list '''
# l=[1,2,3,4,5,6]
# mid=len(l)//2
# l2=l[0:mid]
# l3=l[mid:]
# l4=[]
# for i in range(len(l3)-1,-1,-1):
#     l4.append(l3[i])
# print(l2+l4)

'''45.	Put all even numbers first, odd later '''
# l=[1,2,3,4,5,6]
# l2=[]
# for i in l:
#     if i%2==0:
#         l2.append(i)
# for i in l:
#     if i%2!=0:
#         l2.append(i)
# print(l2)

'''49.	Merge two sorted lists into one sorted list (ascending order ) '''
# l=[1,2,7]
# l2=[3,4,5,6]
# l3=l+l2
# print(l3)
# for i in range(len(l3)):
#     for j in range(i+1,len(l3)):
#         if l3[i]>l3[j]:
#             x=l3[i]
#             l3[i]=l3[j]
#             l3[j]=x
# print(l3)

'''50.	Find union of two lists (unique elements from two list) '''
# l=[1,2,3]
# l2=[2,3,4]
# l3=[]
# for i in l:
#     if i not in l3:
#         l3.append(i)
# for i in l2:
#     if i not in l3:
#         l3.append(i)
# print(l3)




