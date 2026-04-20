'''51.	Find second largest negative number '''
# l=[1,2,3,-1,-2,-3]
# max=0
# sc_max=0
# for i in l:
#     if i<0:
#         if i<max:
#            sc_max=max
#            max=i
#     elif i>sc_max and i!=max:
#         sc_max=i
# print(sc_max)


'''52.	Find second smallest positive number '''
# l=[1,2,3,-1,-2,-3]
# min=9
# sc_min=9
# for i in l:
#     if i>0:
#         if i<min:
#             sc_min=min
#             min=i
#         elif i<sc_min and i!=min:
#             sc_min=i
# print(sc_min)

'''53.	Find largest odd number '''
# l=[1,2,3,4,5,6,7,8,9]
# large=0
# for i in l:
#     if i%2!=0:
#         if i>large:
#             large=i
# print(large)

'''54.	Find smallest even number '''
# l=[1,2,3,4,5,6,7,8,9]
# small=9
# for i in l:
#     if i%2==0:
#         if i<small:
#             small=i
# print(small)

'''55.	Find sum of prime numbers '''
# l=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         sum=sum+i
# print(sum)

'''56.	Find product of all negative numbers '''
# l=[1,2,3,-1,-2,-3]
# prod=1
# for i in l:
#     if i<0:
#         prod=prod*i
# print(prod)

'''57.	Print elements greater than average '''
# l=[1,2,3,4,5,6,7,8,9]
# sum=0
# power=len(l)
# for i in l:
#     sum=sum+i
# avg=abs(sum/power)
# for i in l:
#     if i>avg:
#         print(i)

'''58.	Print elements smaller than median '''
# l = [4, 1, 7, 2, 9]
# l.sort()
# n = len(l)
# if n % 2 == 1:
#     median = l[n // 2]
# else:
#     median = (l[n // 2 - 1] + l[n // 2]) / 2
# print(median)
# for i in l:
#     if i<median:
#         print(i)

'''59.	Find difference between sum of positive and negative numbers '''
# l=[1,2,3,-1,-2,-3]
# sum=0
# sum2=0
# for i in l:
#     if i>0:
#         sum=sum+i
# for i in l:
#     if i<0:
#         sum2=sum2+i
# diff=sum-sum2
# print(diff)

'''60.	Find element closest to zero '''
# l=[1,2,3,-1,-2,-3,0.5]
# min=l[0]
# for i in l:
#     if abs(i) < abs(min):
#         min=i
# print(min)

'''61.	Remove all duplicate values '''
# l=[1,2,3,1,4,2,5,6]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         l2.append(i)
# print(l2)

'''62.	Keep only prime numbers '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         l2.append(i)
# print(l2)

'''64.	Replace all zeros with previous element '''
# l=[5, 0, 3, 0, 8]
# for i in range(1,len(l)):
#     if l[i]==0:
#         l[i]=l[i-1]
# print(l)                         --> excellent p

'''65.	Replace all negatives with nearest positive number '''
# l=[1,-2,3,-4]
# for i in range(1,len(l)):
#     if l[i]<0:
#         l[i]=l[i-1]
# print(l)                      --> brilliant 

'''67.	Count numbers between two given values '''
# l=[1, 5, 8, 3, 10, 7]
# count=0
# a=3
# b=8
# for i in l:
#     if i>a and i<b:
#         count=count+1
# print(count)            between 3 and 8 how many values lies in the given list this ques means that

'''68.	Keep only alternate elements '''
# l=[10, 20, 30, 40, 50, 60]
# l2=[]
# for i in range(len(l)):
#     if i%2==0:
#         l2.append(l[i])
# print(l2)                       --> cr

'''69.	Remove every third and fifth element '''
# l=[10, 20, 30, 40, 50, 60]
# l2=[]
# for i in range(len(l)):
#     if i!=2 and i!=5:
#         l2.append(l[i])
# print(l2)

'''70.	Replace elements at even index with 0 '''
# l=[10, 20, 30, 40, 50, 60]
# l2=[]
# for i in range(len(l)):
#     if i%2!=0:
#         l2.append(l[i])
# print(l2)
 
'''71.	Replace each element with factorial value '''
# l=[1,2,3,4,5,6]
# l2=[]
# for i in l:
#     fact=1
#     for j in range(1,i+1):
#         fact=fact*j
#     l2.append(fact)
# print(l2)

'''72.	Replace each element with number of digits '''
# l=[121,4567,2,33]
# l2=[]
# for i in l:
#     count=0
#     while i>0:
#         digit=i%10
#         count=count+1
#         i=i//10
#     l2.append(count)
# print(l2)

'''73.	Replace each element with sum of digits '''
# l=[121,4567,25,33]
# l2=[]
# for i in l:
#     sum=0
#     while i>0:
#         digit=i%10
#         sum=sum+digit
#         i=i//10
#     l2.append(sum)
# print(l2)

'''74.	Replace each element with reverse of number '''
# l=[121,4567,25,33]
# l2=[]
# for i in l:
#     rev=0
#     while i>0:
#         digit=i%10
#         rev=rev*10+digit
#         i=i//10
#     l2.append(rev)
# print(l2)

'''75.	Replace palindrome numbers with 1 else 0 '''
# l=[121,4567,25,33]
# l2=[]
# for i in l:
#     rev=0
#     x=i
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     if i==rev:
#         i=1
#     else:
#         i=0
#     l2.append(i)
# print(l2)


'''76.	Replace prime numbers with square '''
# l=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         i=i**2
#     l2.append(i)
# print(l2)


'''78.	Replace each element with next greater element in list '''
# l=[1,3,2,5]
# l2=[]
# for i in range(len(l)):
#     ans=-1
#     for j in range(i+1,len(l)):
#         if l[j]>l[i] and ans==-1:
#             ans=l[j]
#     l2.append(ans)
# print(l2)

'''79.	Replace each element with previous smaller element '''
# l=[3,1,7,6]
# l2=[]
# for  i in range(len(l)):
#     ans=-1
#     for j in range(i-1,-1,-1):
#         if l[j]<l[i] and ans==-1:
#           ans=l[j]
#     l2.append(ans)
# print(l2)

'''80.	Replace each element with frequency of itself '''
# l=[1,2,3,1,5,3,7]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     l2.append(count)
# print(l2)

'''81.	Find least frequent element '''
# l=[1,2,3,1,5,3,7,5,2]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         print(i)

'''82.	Find all elements with maximum frequency '''
# l=[1,2,3,1,5,3,7,5,2]

'''83.	Find first unique element '''
# l=[2,2,8,44,5,3,3]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         break
# print(i)

'''84.	Find second repeating element '''
# l=[2,2,8,3,3,44,5]
# c=0
# for i in range(len(l)):
#     count=0
#     for j in l:
#         if l[i]==j:
#             count=count+1
#     if count>1 and l[i] not in l[:i]:
#         c=c+1
#         if c==2:
#             print(l[i])

'''86.	Print frequency of each element without using dictionary '''
# l=[2,2,8,3,3,44,5]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     print(f"{i} Frequency = {count}")
    



   








    



        










