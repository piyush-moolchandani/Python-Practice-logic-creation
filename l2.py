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
# l=[1,2,2,3,3,3,4]
# l2=[]
# sum=0
# unique=0
# for i in l:
#     if i not in l2:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         sum=sum+count
#         unique=unique+1
#         l2.append(i)
# avg=sum/unique
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>avg:
#         print(i)
#         break

'''111.	Keep only numbers whose product of digits is odd '''
# l=[234,54,36,26,78,12,13,56]
# l2=[]
# for i in l:
#     prod=1
#     x=i
#     while i>0:
#         digit=i%10
#         prod=prod*digit
#         i=i//10
#     if prod%2!=0:
#         l2.append(x)
# print(l2)

'''112.	Remove numbers having equal even and odd digits '''
# l=[2233,435,2543,433,123,45436,65,4477]
# l2=[]
# for i in l:
#     x=i
#     count=0
#     count2=0
#     while x>0:
#         digit=x%10
#         if digit%2==0:
#             count=count+1
#         else:
#             count2=count2+1
#         x=x//10
#     if count!=count2:
#         l2.append(i)
# print(l2)


'''113.	Replace numbers divisible by reverse(number) with 0 '''
# l=[123,22,323,565,34,81]
# l2=[]
# for i in l:
#     rev=0
#     x=i
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     if i%rev==0:
#         i=0
#     l2.append(i)
# print(l2)


'''114.	Keep only numbers whose largest digit is prime '''
# l=[157,102,468,244,345]
# l2=[]
# for i in l:
#     x=i
#     large=0
#     while x>0:
#         digit=x%10
#         if digit>large:
#             large=digit
#         x=x//10
#         count=0
#     for j in range(1,large+1):
#         if large%j==0:
#             count=count+1
#     if count==2:
#         l2.append(i)
# print(l2)

'''115.	Remove numbers whose sum of factors is even '''
# l=[4,5,6]
# l2=[]
# for i in l:
#     sum=0
#     for j in range(1,i+1):
#         if i%j==0:
#             sum=sum+j
#     if sum%2!=0:
#         l2.append(i)
# print(l2)

'''116.	Replace negatives whose digit sum is odd with absolute value '''
# l=[-452,-765,455,-245,-789]
# l2=[]
# for i in l:
#     sum=0
#     x=abs(i)
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     if sum%2!=0 and i<0:
#         i=abs(i)
#     l2.append(i)
# print(l2)


'''117.	Keep only numbers appearing odd number of times '''
# l=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count%2!=0:
#         l2.append(i)
# print(l2)
    
# '''118.	Remove elements whose index is Fibonacci number '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)):
#     fi=0
#     se=1
#     for j in range(i):
#         nx=fi+se
#         l2.append(i)
#         fi=se
#         se=nx
# print(l2)

    
'''119.	Replace zeros with nearest non-zero on left or right '''
# l=[1,2,0,4,3]

'''120.	Count numbers whose binary form has more 1s than 0s '''
# l=[1,2,3,4,5,6,7,8,9]
# count=0
# for i in l:
#     ch=bin(i)[2:]
#     count2=0
#     count3=0
#     for j in ch:
#         if j=="1":
#             count2=count2+1
#         elif j=="0":
#             count3=count3+1
#     if count2>count3:
#         count=count+1
# print(count)
        

'''121.	Replace each element with second largest digit '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# large=0
# se_large=0
# for i in l:
#     if i>large:
#         se_large=large
#         large=i
#     elif i>se_large and i!=large:
#         pass
# for i in l:
#     i=se_large
#     l2.append(i)
# print(l2)


'''122.	Replace each element with second smallest digit '''  
# l=[428,345,123,784,234]
# l2=[]
# for i in l:
#     x=i
#     small=9
#     se_small=9
#     while x>0:
#         digit=x%10
#         if digit<small:
#             se_small=small
#             small=digit
#         elif digit<se_small and digit!=small:
#             se_small=digit
#         x=x//10
#     l2.append(se_small)
# print(l2)

'''123.	Replace each element with count of prime digits '''
# l=[428,345,123,784,234]
# l2=[]
# for i in l:
#     x=i
#     c2=0
#     while x>0:
#         digit=x%10
#         count=0
#         for j in range(1,digit+1):
#             if digit%j==0:
#                 count=count+1
#         if count==2:
#             c2=c2+1
#         x=x//10
#     l2.append(c2)
# print(l2)

'''124.	Replace each element with count of composite digits '''
# l=[428,345,492,784,234]
# l2=[]
# for i in l:
#     x=i
#     c=0
#     while x>0:
#         digit=x%10
#         count=0
#         for j in range(1,digit+1):
#             if digit%j==0:
#                 count=count+1
#         if count>2:
#             c=c+1
#         x=x//10
#     l2.append(c)
# print(l2)
    

'''125.	Replace each element with sum of prime digits '''
# l=[321,457,897,123]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         count=0
#         for j in range(1,digit+1):
#             if digit%j==0:
#                 count=count+1
#         if count==2:
#             sum=sum+digit
#         x=x//10
#     l2.append(sum)
# print(l2)
          
'''126.	Replace each element with product of odd digits '''
# l=[123,432,756,2356,794]
# l2=[]
# for i in l:
#     prod=1
#     while i>0:
#         digit=i%10
#         if digit%2!=0:
#             prod=prod*digit
#         i=i//10
#     l2.append(prod)
# print(l2)

'''127.	Replace each element with difference of even-digit sum and odd-digit sum '''
l=[123,432,756,2356,794]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     sum2=0
#     while x>0:
#         digit=x%10
#         if digit%2==0:
#             sum=sum+digit
#         else:
#             sum2=sum2+digit
#         x=x//10
#     diff=abs(sum-sum2)
#     l2.append(diff)
# print(l2)
        
'''128.	Replace each element with nearest perfect square '''
# l = [12,20,27,35,50]
# l2=[]
# for i in l:
#     small=0
#     big=0
#     x=0
#     while x*x<=i:
#         small=x*x
#         x=x+1
#     big=x*x
#     if i-small<big-i:
#         l2.append(small)
#     else:
#         l2.append(big)
# print(l2)

 
'''129.	Replace each element with count of factors '''
# l=[24,12,56,8,45]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     l2.append(count)
# print(l2)
    
'''130.	Replace each element with largest factor less than itself '''
# l=[24,12,56,8,45]
# l2=[]
# for i in l:
#     large=0
#     for j in range(1,i):
        #  if i%j==0:                      --> {great work}
#             if j>large:
#                 large=j
#     l2.append(large)
# print(l2)

'''131.	Find first element appearing exactly 3 times '''
# l=[1,2,2,2,4,5,5,5,7,8,8,8]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==3:
#         print(i)
#         break


'''131.	Find last element appearing exactly 3 times '''
# l=[1,2,2,2,4,5,5,5,7,8,8,8]
# for i in range(len(l)-1,-1,-1):
#     count=0
#     for j in l:
#         if l[i]==j:
#             count=count+1
#     if count==3:
#         print(l[i])
#         break

'''132.	Find last element appearing odd number of times '''
# l=[1,1,2,5,4,4,4,7,8,9,9,9]
# for i in range(len(l)-1,-1,-1):
#     count=0
#     for j in l:
#         if l[i]==j:
#             count=count+1
#     if count%2!=0:
#         print(l[i])
#         break

'''134.	Replace elements with their rank by frequency '''
# l = [2,2,3,3,3,5]
# vals = []
# freq = []
# for i in l:
#     if i not in vals:
#         vals.append(i)
#         count = 0
#         for j in l:
#             if i == j:
#                 count = count + 1
#         freq.append(count)
# rank = []
# for i in range(len(freq)):
#     r = 1
#     for j in range(len(freq)):
#         if freq[j] > freq[i]:
#             r = r + 1
#     rank.append(r)
# l2 = []
# for i in l:
#     for j in range(len(vals)):
#         if i == vals[j]:
#             l2.append(rank[j])
#             break
# print(l2)


'''141.	Move all prime numbers to front '''
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         l2.append(i)
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count!=2:
#         l2.append(i)
# print(l2)
   

'''146.	Rotate list left by count of zeros '''
# l=[1,0,2,0,3,0,4,0]
# count=0
# for i in l:
#     if i==0:
#         count=count+1
# k=count
# for j in range(k):
#     fi=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=fi
# print(l)


'''146.	Rotate list right by count of zeros '''
# l=[1,0,2,0,3,0,4,0]
# count=0
# for i in l:
#     if i==0:
#         count=count+1
# k=count
# for j in range(k):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''147.	Rotate list right by largest element value '''
# l=[1,2,3,4,5,6,7,8,9]
# large=0
# for i in l:
#     if i>large:
#         large=i
# k=large%len(l)
# for j in range(k):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''150.	Merge two lists alternately, extras at end '''
# l = [1,2,3]
# l2 = [10,20,30]
# for i in l:
#     l2.append(i)
# print(l2)

'''131.	Keep only numbers whose sum of prime digits is even '''
# l=[453,222,218,304,422]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         count=0
#         for j in range(1,digit+1):
#             if digit%j==0:
#                 count=count+1
#         if count==2:
#             sum=sum+digit
#         x=x//10
#     if sum%2==0:
#         l2.append(i)
# print(l2)
   
            
'''132.	Remove numbers whose largest digit equals smallest digit '''
l=[111,232,777,454,9]
# l2=[]
# for i in l:
#     x=i
#     large=0
#     small=9
#     while x>0:
#         digit=x%10
#         if digit>large:
#             large=digit
#         elif digit<small:
#             small=digit
#         x=x//10
#     if large!=small:
#         l2.append(i)
# print(l2)

'''133.	Keep only numbers divisible by sum of their digits '''
# l=[120,424,450,123,57,8464,460]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     if i%sum==0:
#         l2.append(i)
# print(l2)


'''134.	Remove numbers whose reverse is prime '''
# l=[17,20,71,99]
# l2=[]
# for i in l:
#     x=i
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     count=0
#     for j in range(1,rev+1):
#         if rev%j==0:
#            count=count+1
#     if count!=2:
#         l2.append(i)
# print(l2)


'''136.	Keep only numbers whose binary form ends with 1 and has exactly 2 ones '''
# l=[5,6,9,10,3]
# l2=[]
# for i in l:
#     x=bin(i)[2:]
#     count=0
#     for j in x:
#         if j=="1":
#             count=count+1
#     if count==2 and j[-1]=="1":
#         l2.append(i)
# print(l2)


'''137.	Remove elements whose index is prime and value is even '''
# l=[5,8,4,7,6,10]
# l2=[]
# for i in range(len(l)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count!=2 or l[i]%2!=0:
#         l2.append(l[i])
# print(l2)

'''135.	Replace negatives whose count of odd digits is even with absolute value '''
# l=[-435,-432543,-324,343,-765]
# l2=[]
# for i in l:
#     x=abs(i)
#     count=0
#     while x>0:
#         digit=x%10
#         if digit%2!=0:
#             count=count+1
#         x=x//10
#     if i<0 and count%2==0:
#         l2.append(abs(i))
# print(l2)

'''139.	Remove numbers whose count of factors is odd '''
# l=[24,45,56,78,81,9,30]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count%2==0:
#         l2.append(i)
# print(l2)

'''140.	Count numbers whose reverse is greater than original '''
# l=[123,459,321,45,423,34]
# count=0
# for i in l:
#     x=i
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     if rev>i:
#         count=count+1
# print(count)
    

'''141.	Replace each element with third largest digit '''
# l=[1234,478,235,74234,6436]
# l2=[]
# for i in l:
#     x=i
#     large=0
#     se_large=0
#     th_large=0
#     while x>0:
#         digit=x%10
#         if digit>large:
#           th_large=se_large
#           se_large=large
#           large=digit
#         elif digit>se_large and digit!=large:
#            th_large=se_large
#            se_large=digit
#         elif digit>th_large and digit!=se_large and digit!=large:
#            th_large=digit
#         x=x//10
#     l2.append(th_large)
# print(l2)


'''143.	Replace each element with sum of composite digits '''
# l=[462,789,843,556,469]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         count=0
#         for j in range(1,digit+1):
#             if digit%j==0:
#                 count=count+1
#         if count>2:
#             sum=sum+digit
#         x=x//10
#     l2.append(sum)
# print(l2)


'''145.	Replace each element with difference of largest and second largest digit '''
# l=[462,789,843,556,469]
# l2=[]
# for i in l:
#     x=i
#     large=0
#     se_large=0
#     while x>0:
#         digit=x%10
#         if digit>large:
#             se_large=large
#             large=digit        
#         elif digit>se_large and digit!=large:
#             se_large=digit
#         x=x//10
#     diff=large-se_large
#     l2.append(diff)
# print(l2)

'''146.	Replace each element with nearest cube number '''
# l = [10,20,30,50,70]
# l2 = []
# for i in l:
#     small = 0
#     big = 0
#     x = 0
#     while x**3 <= i:
#         small = x**3
#         x = x + 1
#     big = x**3
#     if i - small < big - i:
#         l2.append(small)
#     else:
#         l2.append(big)
# print(l2)
           

'''147.	Replace each element with count of odd factors '''
# l=[24,56,48,45,9,8]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0 and j%2!=0:
#             count=count+1
#     l2.append(count)
# print(l2)

'''148.	Replace each element with smallest factor greater than 1 '''
# l=[24,56,48,45,9,8]
# l2=[]
# for i in l:
#     small=9
#     for j in range(1,i+1):
#         if i%j==0:
#             if j<small and j>1:
#                 small=j
#     l2.append(small)
# print(l2)

'''149.	Replace each element with sum of digits of reverse(number) '''
# l=[24,56,48,45]
# l2=[]
# for i in l:
#     x=i
#     rev=0
#     sum=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#         while rev>0:
#             digit=rev%10
#             sum=sum+digit
#             rev=rev//10
#     l2.append(sum)
# print(l2)
  

'''150.	Replace each element with count of digits greater than average digit '''
# l = [4725,111,908]
# l2 = []
# for i in l:
#     x = i
#     div = len(str(i))
#     total = 0
#     while x > 0:
#         digit = x % 10
#         total = total + digit
#         x = x // 10
#     avg = total / div
#     x = i
#     count = 0
#     while x > 0:
#         digit = x % 10
#         if digit > avg:
#             count = count + 1
#         x = x // 10
#     l2.append(count)
# print(l2)


'''151.	Find first element whose frequency is odd and > average frequency '''
# l=[3,3,3,2,2,44,5,5,5]
# l2=[]
# sum=0
# for i in l:
#     if i not in l2:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         sum=sum+count
#         l2.append(i)
# avg=sum/len(l2)
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count%2!=0 and count>avg:
#         print(i)
#         break

'''Rotate left by count of prime numbers'''
# l=[1,2,3,4,5,6,7,8,9]
# c=0
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         c=c+1
# k=c
# for j in range(k):
#     fi=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=fi
# print(l)





            
        
   
        
    

     










        
    





        
       






   









    



        










