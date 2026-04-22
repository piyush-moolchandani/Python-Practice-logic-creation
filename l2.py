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
    
'''87.	Find element whose frequency is prime '''
# l=[1,3,3,4,3]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     c2=0
#     for x in range(1,count+1):
#         if count%x==0:
#             c2=c2+1
#     if c2==2:
#         pass
# print(i)

'''88.	Remove elements occurring more than twice '''
# l=[1,1,2,3,4,4,4,5]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count<=2:
#         l2.append(i)
# print(l2)

'''89.	Replace repeated elements with -1 '''
# l=[1,1,2,3,4,4,4,5]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         i=-1
#     l2.append(i)
# print(l2)

'''90.	Find longest streak of same number '''
# l = [1,1,2,3,4,4,4,5]
# current = [l[0]]
# best = [l[0]]
# for i in range(1, len(l)):
#     if l[i] == l[i-1]:
#         current.append(l[i])
#     else:
#         current = [l[i]]
#     if len(current) > len(best):
#         best = current[:]
# print(best)

'''91.	Keep only numbers whose sum of digits is even '''
# l=[22,34,13,78,94,33]
# l2=[]
# for i in l:
#     sum=0
#     x=i
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     if sum%2==0:
#         l2.append(i)
# print(l2)

'''92.	Remove numbers whose reverse is same '''
# l=[121,34,56,22,434,11,56]
# l2=[]
# for i in l:
#     rev=0
#     x=i
#     while i>0:
#         digit=i%10
#         rev=rev*10+digit
#         i=i//10
#     if rev!=x:
#         l2.append(x)
# print(l2)

'''93.	Replace negatives with absolute value only if even '''
# l=[-12,45,-13,-24]
# l2=[]
# for i in l:
#     if i%2==0:
#         l2.append(abs(i))
#     else:
#         i=i
#         l2.append(i)
# print(l2)

'''94.	Keep only numbers having exactly 3 digits '''
# l=[123,45,678,34,56,333,56,4]
# l2=[]
# for i in l:
#     if len(str(i))==3:
#         l2.append(i)
# print(l2)

'''95.	Remove numbers divisible by sum of digits '''
# l=[123,45,678,34,56,333,56,4]
# l2=[]
# for i in l:
#     sum=0
#     x=i
#     while i>0:
#         digit=i%10
#         sum=sum+digit
#         i=i//10
#     if x%sum!=0:
#         l2.append(x)
# print(l2)

'''96.	Print numbers whose square ends with 5 '''
# l=[123,45,678,34,56,333,56,4]
# l2=[]
# for i in l:
#     sq=i**2
#     if sq%5==0:
#         print(i)

'''97.	Count numbers having more even digits than odd digits '''
# l=[221,455,343,885,214]
# c=0
# for i in l:
#     count=0
#     count2=0
#     while i>0:
#         digit=i%10
#         if digit%2==0:
#             count=count+1
#         elif digit%2!=0:
#             count2=count2+1
#         i=i//10
#     if count>count2:
#         c=c+1
# print(c)

'''98.	Replace zeros with next non-zero element '''
# l=[4,0,0,7,2]
# l2=[]
# for i in range(len(l)):
#     if l[i]==0:
#         l[i]=l[i+1]
#     l2.append(l[i])
# print(l2)

# l = [4,0,0,7,2]
# l2 = []
# for i in range(len(l)):
#     if l[i] == 0:
#         value = 0
#         for j in range(i+1, len(l)):
#             if l[j] != 0:
#                 value = l[j]
#                 break
#         l2.append(value)
#     else:
#         l2.append(l[i])
# print(l2)

'''99.	Keep only numbers greater than average and less than max '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# div=len(l)
# max=0
# sum=0
# for i in l:
#     sum=sum+i
# avg=abs(sum/div)
# for j in l:
#     if j>max:
#         max=j
# for j in l:
#     if j>avg and j<max:
#         l2.append(j)
# print(l2)

'''100.	Remove numbers appearing at prime indexes'''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count!=2:
#         l2.append(l[i])
# print(l2)

'''101.	Replace each element with product of digits '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# prod=1
# for i in l:
#     prod=prod*i
#     i=prod
#     l2.append(i)
# print(l2)

'''102.	Replace each element with largest digit '''
# l=[221, 455, 343]
# l2=[]
# for i in l:
#     large=0
#     while i>0:
#         digit=i%10
#         if digit>large:
#             large=digit
#         i=i//10
#     l2.append(large)
# print(l2)

'''104.	Replace each element with count of even digits '''
# l=[221,456,345,785,4,325]
# l2=[]
# for i in l:
#     count=0
#     while i>0:
#         digit=i%10
#         if digit%2==0:
#             count=count+1
#         i=i//10
#     l2.append(count)
# print(l2)

'''106.	Replace numbers with sum of factors '''
# l=[24,56,81,9,4,2]
# l2=[]
# for i in l:
#     sum=0
#     for j in range(1,i+1):
#         if i%j==0:
#             sum=sum+j
#     l2.append(sum)
# print(l2)

'''107.	Replace perfect squares with root value '''
# l=[4,9,16,25]
# l2=[]
# for i in l:
#     sq = i**0.5
#     l2.append(int(sq))
# print(l2)

'''108.	Replace Armstrong numbers with 1 else 0 '''
# l=[153,234,347,2,3,67]
# l2=[]
# for i in l:
#     sum=0
#     power=len(str(i))
#     x=i
#     while i>0:
#         digit=i%10
#         sum=sum+digit**power
#         i=i//10
#     if x==sum:
#         x=1
#     else:
#         x=0
#     l2.append(x)
# print(l2)

'''109.	Replace each element with nearest multiple of 10 '''
# l=[12, 27, 44]
# l2=[]
# for i in l:
#     low=(i//10)*10
#     high=low+10
#     if i-low<high-1:
#         l2.append(low)
#     else:
#         l2.append(high)
# print(l2)

'''110.	Replace each element with difference of max digit and min digit '''
# l=[349,478,456,214]
# l2=[]
# for i in l:
#     max=0
#     min=9
#     while i>0:
#         digit=i%10
#         if digit>max:
#             max=digit
#         elif digit<min:
#             min=digit
#         i=i//10
#     diff=max-min
#     l2.append(diff)
# print(l2)

'''111.	Find element with second least frequency '''
'''112.	Find all elements appearing odd number of times '''
# l=[1,2,2,3,3,3,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count%2!=0:
#         l2.append(i)
# print(l2)        
        
'''114.	Replace elements occurring once with 0 '''
# l=[1,2,2,3,3,3,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         i=0
#     l2.append(i)
# print(l2)

'''115.	Remove first repeating element only '''
# l=[1,2,2,3,3,3,4]
# rv=None
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         rv=i
#         break
# l2=[]
# for i in l:
#     if i!=rv:
#         l2.append(i)
# print(l2)


'''116.	Remove last repeating element only '''
# l=[1,2,2,3,3,3,4]
# rv=None
# for i in range(len(l)-1,-1,-1):
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         rm=i
#         break
# l2=[]
# for i in l:
#     if i!=rm:
#         l2.append(i)
# print(l2)


'''117.	Find first element whose frequency > average frequency '''



     









        
    





        
       






   









    



        










