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
    