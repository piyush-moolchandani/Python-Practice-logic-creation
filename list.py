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

"Find Least Frequency "
# l=[4,5,6,3,5,6,43,35,65,32,4]
# min=l[0]
# minimun=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count<min:
#         min=count
#         minimun=i
# print("Most frequent element =", minimun)
# print("Frequency =", min)


'''34.	Count elements appearing more than once '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
# if count>1:
#     print(count)

'''35.	Print duplicate elements '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         l2.append(i)
# print(l2)

'''36.	Remove duplicates '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         l2.append(i)
# print(l2)

'''37.	Count unique elements '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# count2=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         count2=count2+1
# print(count2)

'''38.	Replace duplicates with 0 '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         i=0
#     l2.append(i)
# print(l2)

'''39.	Find first non-repeating element '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#          print("First non-repeating element =", i)
#          break

'''40.	Find second most frequent element '''
# l = [4,5,6,3,5,6,43,35,65,32,4,4]
# max1 = 0
# max2 = 0
# first = 0
# second = 0
# done = []
# for i in l:
#     if i not in done:
#         count = 0
#         for j in l:
#             if i == j:
#                 count = count + 1
#         if count > max1:
#             max2 = max1
#             second = first
#             max1 = count
#             first = i
#         elif count > max2:
#             max2 = count
#             second = i
#         done.append(i)
# print("Second most frequent =", second)

'''42.	Rotate list left by 1 '''
# l=[10,20,30,40]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)

'''43.	Rotate list right by 1 '''
# l=[10,20,30,40]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)

'''44.	Rotate list by k positions '''
# l=[1,2,3,4,5]
# k=2
# for j in range(2):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''Rotate list by k 7 '''
# l=[1,2,3,4,5]
# k=7
# k=k%len(l)
# for j in range(k):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''Left rotate by k'''
# l=[1,2,3,4,5]
# k=2
# for j in range(k):
#     fi=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=fi
# print(l)

'''Left rotate by k3 '''
# l=[1,2,3,4,5,6,7,8]
# k=3
# for j in range(k):
#     fi=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=fi
# print(l)

'''right rotate by k3 '''
# l=[1,2,3,4,5,6,7,8]
# k=3
# for i in range (k):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''45.	Move all zeros to end '''
# l=[1,0,2,0,3,0,4,0,5,0]
# l2=[]
# l3=[]
# for i in l:
#     if i!=0:
#         l2.append(i)
# for i in l:
#     if i==0:
#         l3.append(i)
# print(l2+l3)

'''46.	Move all zeros to front '''
# l=[1,0,2,0,3,0,4,0,5,0]
# l2=[]
# l3=[]
# for i in l:
#     if i==0:
#         l2.append(i)
# for i in l:
#     if i!=0:
#         l3.append(i)
# print(l2+l3)

'''48.	Sort list (without using sort) '''
'''🔹 Ascending Order (small to big)'''
# l=[4,2,7,1,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)

'''🔹 descending Order (big to small)'''
# l=[4,2,7,1,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)


'''49.	Merge two lists '''
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# for i in l2:
#     l1.append(i)
# print(l1)

'''50.	Find intersection of two lists '''
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# l3=[]
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)
  
''''''
       

    


        






















   
   




        
     


