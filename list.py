'''1.	Find largest element '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)

'''3.	Find second largest '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# large=0
# second_largest=0
# for i in l:
#     if i>large:
#        second_largest=large
#        large=i
#     elif i>second_largest and i!=large:
#         second_largest=i
# print(second_largest)
    

'''4.	Find second smallest '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# small=l[0]
# second_small=l[0]
# for i in l:
#     if i<small:
#         second_small=small
#         small=i
#     elif i<second_small and i!=small:
#         second_small=i
# print(second_small)

'''6.	Count even numbers '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# count=0
# for i in l:
#     if i%2==0:
#         count=count+1
# print(count)
   
'''8.	Find average of list '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# div=len(l)
# sum=0
# for i in l:
#     sum=sum+i
# avg=sum/div
# print(avg)

'''9.	Print elements greater than average '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# div=len(l)
# sum=0
# for i in l:
#     sum=sum+i
# avg=sum/div
# for j in l:
#     if j>avg:
#         print(j)

'''11.	Print all even numbers '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# for i in l:
#     if i%2==0:
#         print(i)

'''13.	Remove all even numbers '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%2!=0:
#         l2.append(i)
# print(l2)

'''15.	Replace even numbers with 0 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%2==0:
#         i=0
#     l2.append(i)
# print(l2)

'''17.	Keep only numbers divisible by 3 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%3==0:
#         l2.append(i)
# print(l2)

'''18.	Remove numbers divisible by 5 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%5!=0:
#         l2.append(i)
# print(l2)
        
'''19.	Replace negative numbers with 0 '''
# l=[4,5,-6,3,-5,6,-43,35,-65,32,-4]
# l2=[]
# for i in l:
#     if i<0:
#         i=0
#     l2.append(i)
# print(l2)


'''20.	Count numbers greater than 10 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# count=0
# for i in l:
#     if i>10:
#         count=count+1
# print(count)

'''21.	Replace each element with its square '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     l2.append(i**2)
# print(l2)

'''23.	Replace even numbers with their square '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%2==0:
#         sq=i**2
#     else:
#         sq=i
#     l2.append(sq)
# print(l2)    

'''25.	Replace numbers > 10 with 100 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i>10:
#         i=100
#     l2.append(i)
# print(l2)

'''26.	Replace numbers < 5 with -1 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i<5:
#         i=i-1
#     l2.append(i)
# print(l2)
  
'''27.	Replace each element with difference from max '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# for j in l:
#     j=j-max
#     l2.append(abs(j))
# print(l2)

'''reverse of a list'''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

'''29.	Replace each element with sum of all elements '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# sum=0
# for i in l:
#     sum=sum+i
# for j in l:
#     j=sum
#     l2.append(j)
# print(l2)

'''31.	Count frequency of each element '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# for i in l:
#     count=0
#     for j in l:
#       if i==j:
#         count=count+1
#     print(i,"==",count)

'''32.	Find most frequent element '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# max_count = 0
# most = 0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>max_count:
#         max_count=count
#         most=i
# print("Most frequent element =", most)
# print("Frequency =", max_count)












   
   




        
     


