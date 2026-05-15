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

'''Find fourth largest element'''
# l=[1,2,3,4,5,6,7,8,9]
# large=0
# se_large=0
# th_large=0
# fo_large=0
# for i in l:
#     if i>large:
#         fo_large=th_large
#         th_large=se_large
#         se_large=large
#         large=i
#     elif th_large>i and i!=large:
#         fo_large=th_large
#     elif i>fo_large and i!=large and i!=se_large and i!=th_large:
#         fo_large=i 
# print(fo_large)

'''Find difference between sum of max 2 and min 2 elements'''
# l=[4,1,9,3,7]
# large=0
# se_large=0
# small=9
# se_small=9
# for i in l:
#     if i>large:
#         se_large=large
#         large=i
#     elif i>se_large and i!=large:
#         se_large=i
# for i in l:
#     if i<small:
#         se_small=small
#         small=i
#     elif i<se_small and i!=small:
#         se_small=i
# diff=(large+se_large)-(small+se_small)
# print(diff)

'''4.Find sum of numbers divisible by both 2 and 3 '''
# l=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in l:
#     if i%2==0 and i%3==0:
#         sum=sum+i
# print(sum)

'''Find sum of absolute values of negative numbers'''
# l=[3, -4, 7, -2, -5]
# sum=0
# for i in l:
#     if i<0:
#         sum=sum+abs(i)
# print(sum)

'''6.Count perfect square numbers in list '''
# l=[4,9,25,64,5,16]
# count=0
# for i in l:
#     root=i**0.5
#     sq=root**2
#     if int(i)==sq:
#         count=count+1
# print(count)

'''7.	Count numbers having exactly 3 divisors '''
# l=[21,4,8,64,21]
# c=0
# for i in l:
#     count=0
#     for j in l:
#         if i%j==0:
#             count=count+1
#     if count==3:
#         c=c+1
# print(c)

'''8.	Find average of prime numbers only '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         l2.append(i)
# sum=0
# for i in l2:
#     sum=sum+i
# avg=sum/len(l2)
# print(avg)


'''10.	Print elements nearest to average '''
# l=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in l:
#     sum=sum+i
# avg=sum/len(l)
# small_diff=abs(l[0] - avg)
# for i in l:
#     diff=abs(i - avg)
#     if diff<small_diff:
#         small_diff=diff
# for i in l:
#     if abs(i - avg)==small_diff:
#         print(i)

'''11.	Print elements greater than left neighbor only '''
# l=[1,2,3,4,5,6,7,8,9]
# for i in range(1,len(l)-1):
#     if l[i]>l[i-1]:
#         print(l[i])

'''12.	Print elements smaller than right neighbor only '''
# l=[1,2,3,4,8,3,9]
# for i in range(1,len(l)-1):
#     if l[i]<l[i+1]:
#         print(l[i])

'''13.	Remove only first duplicate occurrence of each repeated value '''
l=[1,2,2,2,3,3,3,3,4,5,5,5]

# '''14.	Keep only values appearing exactly twice '''
# l=[1,2,2,3,3,4,5,5,5]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==2:
#         l2.append(i)
# print(l2)

'''15.	Replace multiples of both 2 and 5 with 10 '''
# l=[2,11,25,4,40,55,23]
# l2=[]
# for i in l:
#     if i%2==0:
#         i=10
#     elif i%5==0:
#         i=10
#     l2.append(i)
# print(l2)
    
'''16.	Replace numbers divisible by 3 or 5 with -1 '''
# l=[25,3,46,9,54,33,1]
# l2=[]
# for i in l:
#     if i%3==0 or i%5==0:
#         i=-1
#     l2.append(i)
# print(l2)

'''21.	Replace each element with triple value '''
# l=[1,2,3,4,5,6,7,8]
# l2=[]
# for i in l:
#     tr=i*3
#     l2.append(tr)
# print(l2)

''' 53.	Find missing number from 1 to n '''
# l=[1,2,4,5]
# n = len(l)+1
# sum_2=0
# for i in range(1,n):
#     sum=n*(n+1)/2
# for i in l:
#     sum_2=sum_2+i
# missing_number= int(sum)-sum_2
# print(missing_number)


'''54.	Find repeated number from 1 to n '''
# l=[1,2,3,4,4]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
# if count>1:
#     print("repeated digit is ", i)

 
'''156.	Move all elements with even frequency to front '''
# l=[1,2,2,3,3,3,4,4,4,4]
# l2=[]
# l3=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count%2==0:
#         l2.append(i)
#     else:
#         l3.append(i)
# print(l2+l3)
        

'''22.	Replace each element with square root (perfect squares only) '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     root=i**0.5
#     sq=root**2
#     if i==sq:
#         i=int(root)
#     l2.append(i)
# print(l2)

'''24.	25.	Replace even numbers with previous even number  '''
# l=[3,4,6,8,5]
# l2=[]
# for i in l:
#     if i%2==0:
#         i=i-2
#     l2.append(i)
# print(l2)
    
'''27.	Replace each element with distance from max '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# max=0
# for i in l:
#     if i>max:
#         max=i
# for i in l:
#     dis=max-i
#     l2.append(dis)
# print(l2)

'''31.	Find elements with second highest frequency '''
# l=[1,2,2,2,3,3]
# max=0
# se_max=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>max:
#         se_max=max
#         max=count
#     elif count>se_max and count!=max:
#         se_max=count
# print(i)
    
'''43.	Reverse every group of 3 elements '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=l[0:3]
# l3=l[3:6]
# l4=l[6:9]
# sl=l2[::-1]
# sl1=l3[::-1]
# sl2=l4[::-1]
# print(sl+sl1+sl2)

'''47.	Move all positives to end while preserving order '''
# l=[2, -3, 4, -1, 5, -6]
# l2=[]
# for i in l:
#     if i<0:
#         l2.append(i)
# for i in l:
#     if i>0:
#         l2.append(i)
# print(l2)

'''50.	Find symmetric difference of two lists '''
# l1 = [1,2,3]
# l2 = [2,3,4]
# l3 = []
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# for i in l2:
#     if i not in l1:
#         l3.append(i)
# print(l3)

'''53.	Find all triplets with sum = 0 '''
# l=[-1,2,3,2,-1,-1]
# l2=[]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         for k in range(j+1,len(l)):
#             if l[i]+l[j]+l[k]==0:
#                 temp=[l[i],l[j],l[k]]
#                 temp.sort()
#                 if temp not in l2:
#                     l2.append(temp)
# print(l2)

'''58.	Replace each element with next smaller element '''
# l=[4,5,2,10,8]
# l2=[]
# for i in range(len(l)):
#     found=0
#     for j in range(i+1,len(l)):
#         if l[j]<l[i]:
#            l2.append(l[j])
#            found=1
#            break
#     if found==0:
#         l2.append(-1)
# print(l2)


'''37.	Find first element repeating exactly twice '''
# l=[1,2,2,3,3,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==2:
#         print(i)
#         break


'''Find difference between sum of even-index and odd-index elements'''
# l=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# sum2=0
# for i in range(1,len(l)):
#     if i%2==0:
#         sum=sum+l[i]
#     elif i%2!=0:
#         sum2=sum2+l[i]
# diff=abs(sum-sum2)
# print(diff)

'''Find element with maximum absolute value'''
# l=[3, -7, 2, -10, 5]
# max=0
# for i in l:
#     if abs(i)>abs(max):
#         max=i
# print(max)

'''Find sum of elements at prime indexes'''
# l=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in range(len(l)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         sum=sum+l[i]
# print(sum)


'''6.	Find average of elements at odd positions only '''
# l=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# sum=0
# for i in range(len(l)):
#     if i%2!=0:
#         l2.append(l[i])
# sum=0
# for i in l2:
#     sum=sum+i
# avg=sum/len(l2)
# print(avg)

'''7.	Print elements whose value equals index '''
# l=[1,1,3,3,4,5]
# for i in range(len(l)):
#     if l[i]==i:
#         print(l[i])

'''8.	Find sum of elements excluding max and min '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# max=l[0]
# min=l[0]
# for i in l:
#     if i>max:
#         max=i
#     elif i<min:
#         min=i
# sum=0
# for i in l:
#     if i!=max and i!=min:
#         sum=sum+i
# print(sum)

   
'''9.	Count elements strictly between min and max '''
# l=[1,2,3,4,5,6,7,8,9,10]
# count=0
# for i in l:
#     if i>min(l) and i<max(l):
#         count=count+1
# print(count)

'''10.	Find element farthest from average '''
# l=[2, 4, 6, 8]
# l2=[]
# sum=0
# for i in l:
#     sum=sum+i
# avg=sum/len(l)
# max=0
# res=l[0]
# for i in l:
#     dis=abs(i-avg)
#     if dis>max:
#         max=dis
#         res=i
# print(res)

'''11.	Keep only elements whose digit sum is divisible by 3 '''
# l=[15,21,22,46,84]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     if sum%3==0:
#         l2.append(i)
# print(l2)

'''12.	Remove elements whose last digit is even '''
# l=[132,456,433,566,782,654]
# l2=[]
# for i in l:
#     ld=i%10
#     if ld%2!=0:
#         l2.append(i)
# print(l2)

'''13.	Keep numbers where first digit > last digit '''
# l=[132,456,433,566,782,654]
# l2=[]
# for i in l:
#     x=i
#     while x>10:
#         x=x//10
#         fd=x
#         ld=i%10
#     if fd>ld:
#         l2.append(i)
# print(l2)

'''14.	Remove elements whose square is > 100 '''
# l=[9,45,23,1,2,6,43]
# l2=[]
# for i in l:
#     if i**2<100:
#         l2.append(i)
# print(l2)

'''16.	.Keep only numbers having unique digits  '''
# l=[123,223,567,432,677,322,549,213]
# l2=[]
# for i in l:
#     x=i
#     count_repeat=0
#     rem=x
#     while x>0:
#         digit=x%10
#         a=rem
#         count=0
#         while a>0:
#             digit2=a%10
#             if digit==digit2:
#                 count=count+1
#             a=a//10
#         if count>1:
#             count_repeat=1
#             break
#         x=x//10
#     if count_repeat==0:
#         l2.append(i)
# print(l2)

'''15.	Replace elements divisible by 4 but not 8 with -1 '''    
# l=[1,16,4,24,20]
# l2=[]
# for i in l:
#     if i%4==0 and i%8!=0:
#         i=-1
#         l2.append(i)
#     else:
#         i=i
#         l2.append(i)
# print(l2)

'''17.	Remove numbers containing digit ‘0’ '''
# l=[102,456,220,679]
# l2=[]
# for i in l:
#     x=i
#     zero=False
#     while x>0:
#         digit=x%10
#         if digit==0:
#             zero=True
#         x=x//10
#     if not zero:
#         l2.append(i)
# print(l2)


'''18.	Keep numbers whose reverse is greater than original '''
# l=[102,456,220,679]   
# l2=[]
# for i in l:
#     x=i
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     if rev>i:
#         l2.append(i)
# print(l2)


'''19.	Count numbers whose digits are strictly increasing '''
# l=[123, 321, 456, 455, 789]
# l2=[]
# for i in l:
#     x=str(i)
#     valid=True
#     for j in range(len(x)-1):
#         if x[j]>=x[j+1]:
#             valid=False
#             break
#     if valid:
#         l2.append(i)
# print(l2)
   

'''20.	Replace numbers having repeated digits with 0 '''
# l=[121,223,567,477,123,321]
# l2=[]
# for i in l:
#     x=str(i)
#     if len(x)==len(set(x)):
#         l2.append(i)
#     else:
#         l2.append(0)
# print(l2)

'''21.	Replace each element with sum of squares of its digits '''
# l=[121,223,567,477,123,321]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sq=digit**2
#         sum=sum+sq
#         x=x//10
#     l2.append(sum)
# print(l2)

   
'''22.	Replace each element with product of non-zero digits''' 
# l=[105, 2304, 111, 100]
# l2=[]
# for i in l:
#     x=i
#     prod=1
#     while x>0:
#         digit=x%10
#         if digit!=0:
#             prod=prod*digit
#         x=x//10
#     l2.append(prod)
# print(l2)


'''23.	Replace each element with difference between first and last digit '''
# l=[121,223,567,477,123,321]
# l2=[]
# for i in l:
#     x=i
#     while x>10:
#         x=x//10
#     fd=x
#     ld=i%10
#     diff=abs(fd-ld)
#     l2.append(diff)
# print(l2)

'''25.	Replace each element with count of divisors '''
# l=[24,12,56,44]
# l2=[]
# count=0
# for i in l:
#     for j in range(1,i+1):
#         if i%j:
#             count=count+1
#     l2.append(count)
# print(l2)


'''26.	Replace each element with sum of proper divisors '''
# l=[24,12,56,44]
# l2=[]
# sum=0
# for i in l:
#     for j in range(1,i):
#         if i%j==0:
#             sum=sum+j
#     l2.append(sum)
# print(l2)

'''27.	Replace each element with nearest multiple of 5 '''
# l = [12, 23, 37, 40, 42]
# l2=[]
# for i in l:
#     lower=(i//5)*5
#     upper=lower+5
#     if (i-lower)<=(upper-i):
#         l2.append(lower)
#     else:
#         l2.append(upper)
# print(l2)

'''28.	Replace each element with next prime number '''
# l = [10, 14, 17, 20, 23]
# l2 = []
# for i in l:
#     num=i+1
#     while True:
#         count=0
#         for j in range(1,num+1):
#             if num%j==0:
#                 count=count+1
#         if count==2:
#             l2.append(num)
#             break
#         else:
#             num+=1
# print(l2)

'''30.	Replace each element with number of trailing zeros in factorial '''
# l=[5, 10, 6]
# l2=[]
# for i in l:
#     fact=1
#     for j in range(1,i+1):
#         fact=fact*j
#     count=0
#     while fact%10==0:
#         count=count+1
#         fact=fact//10
#     l2.append(count)
# print(l2)

'''31.	Find elements whose frequency equals their value '''
# l=[1,2,2,3,3,4,4,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==i:
#         l2.append(i)
# print(l2)

# '''32.	Count elements with prime frequency '''
# l=[1,2,2,3,3,3,4,4,4,4]
# l2=[]
# c2=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     c=0
#     for k in range(1,count+1):
#         if count%k==0:
#             c=c+1
#     if c==2:
#         c2=c2+1
# print(c2)


'''37.	Find element with maximum frequency but smallest value '''
# l=[1,1,2,2,3]
# max_freq=0
# small=l[0]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>max_freq :
#         max_freq=count
#         small=i
#     elif count==max_freq and i<small:
#         small=i
# print(small)]


'''39.	Count how many elements appear in consecutive positions '''
# l=[1,1,2,2,2,3,4,4]
# count=0
# l2=[]
# for i in range(len(l)-1):
#     if l[i]==l[i+1] and l[i] not in l2:
#         count=count+1
#         l2.append(l[i])
# print(count)

'''41.	Rearrange array such that positives and negatives alternate (stable) '''
# l=[-5, 1, -2, 2, 3, -8]


# pos = []
# neg = []
# result = []

# # separate positives and negatives
# for i in l:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# # alternate them
# i = 0
# j = 0

# while i < len(pos) and j < len(neg):
#     result.append(pos[i])
#     result.append(neg[j])

#     i += 1
#     j += 1

# # remaining positives
# while i < len(pos):
#     result.append(pos[i])
#     i += 1

# # remaining negatives
# while j < len(neg):
#     result.append(neg[j])
#     j += 1

# print(result)
        


'''Find elements whose frequency equals sum of digits'''
# l=[11,11,2,2,2,3,3]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
#         x=i
#         sum=0
#         while x>0:
#             digit=x%10
#             sum=sum+digit
#             x=x//10
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         if count==sum:
#             print(i)


'''1.	Replace elements whose digit sum is prime with their reverse '''
# l=[21,23,44,14,78]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     count=0
#     rev=0
#     for j in range(1,sum+1):
#         if sum%j==0:
#             count=count+1
#     if count==2:
#         rev=0
#         while i>0:
#             digit=i%10
#             rev=rev*10+digit
#             i=i//10
#         l2.append(rev)
#     else:
#         l2.append(i)
# print(l2)
   

'''2.	Keep numbers where product of digits > sum of digits '''
# l=[21,23,44,14,78]
# l2=[]
# for i in l:
#     y=i
#     x=i
#     prod=1
#     while x>0:
#         digit=x%10
#         prod=prod*digit
#         x=x//10
#     sum=0
#     while i>0:
#         digit=i%10
#         sum=sum+digit
#         i=i//10
#     if prod>sum:
#         l2.append(y)
# print(l2)


'''3.	Replace elements ending with 5 by nearest prime '''
# l = [12,15,67,45,34,65,33,75]
# l2 = []
# for i in l:
#     if i % 10 == 5:
#         # previous prime
#         prev = i - 1
#         while prev > 1:
#             count = 0
#             for j in range(1, prev + 1):
#                 if prev % j == 0:
#                     count += 1
#             if count == 2:
#                 break
#             prev -= 1
#         # next prime
#         nxt = i + 1
#         while True:
#             count = 0
#             for j in range(1, nxt + 1):
#                 if nxt % j == 0:
#                     count += 1
#             if count == 2:
#                 break
#             nxt += 1
#         # choose nearest
#         if (i - prev) <= (nxt - i):
#             l2.append(prev)
#         else:
#             l2.append(nxt)
#     else:
#         l2.append(i)
# print(l2)



'''4.	Count numbers having exactly 3 divisors '''
# l=[9,4,24,6]
# count=0
# for i in l:
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c=c+1
#     if c==3:
#         count=count+1
# print(count)

'''5.	Keep elements whose first digit is even and last digit is odd '''
# l=[235,222,479,567]
# l2=[]
# for i in l:
#     x=i
#     while x>10:
#         x=x//10
#         fd=x
#         ld=i%10
#     if fd%2==0 and ld%2!=0:
#         l2.append(i)
# print(l2)


'''6.	Replace numbers containing repeated odd digits with -1 '''
# l=[151,565,334,123,456]
# l2=[]
# for i in l:
#     x=i
#     rem=x
#     while x>0:
#         digit=x%10
#         a=rem//10
#         while a>0:
#             digit2=a%10
#             if digit==digit2 and digit%2!=0:
#                 i=-1
#             a=a//10
#         x=x//10
#     l2.append(i)
# print(l2)

# l = [151,565,334,123,456]
# l2 = []
# for i in l:
#     x = i
#     while x > 0:
#         digit = x % 10
#         a = x // 10
#         while a > 0:
#             digit2 = a % 10
#             if digit == digit2 and digit % 2 != 0:
#                 i = -1
#             a = a // 10
#         x = x // 10
#     l2.append(i)
# print(l2)
    

'''7.	Find elements whose reverse is divisible by original '''
# l=[42,101,56,11]
# l2=[]
# for i in l:
#     x=i
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     if rev%i==0:
#         l2.append(i)
# print(l2)


'''8.	Count elements whose digit product is divisible by 7 '''
# l=[71,72,45,26,78]
# count=0
# for i in l:
#     prod=1
#     while i>0:
#         digit=i%10
#         prod=prod*digit
#         i=i//10
#     if prod%7==0:
#         count=count+1
# print(count)


'''9.	Replace each element with largest digit minus smallest digit '''
# l=[657,352,634,179,367]
# l2=[]
# for i in l:
#     x=i
#     small=9
#     large=0
#     while x>0:
#         digit=x%10
#         if digit>large:
#             large=digit
#         elif digit<small:
#             small=digit
#         x=x//10
#     diff=large-small
#     l2.append(diff)
# print(l2)


'''10.	Keep numbers whose digits form a palindrome after squaring '''
# l=[11,12,26]
# l2=[]
# for i in l:
#     sq=i**2
#     x=sq
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     if rev==sq:
#         l2.append(i)
# print(l2)


'''11.	Replace digits where digit × position is even with 0 '''
# l=[3,5,2,7]
# l2=[]
# for i in range(len(l)):
#     if (l[i]*i)%2==0:
#         l[i]=0
#     l2.append(l[i])
# print(l2)

'''12.	Replace digits where digit + reverse(position) is prime with 5 '''
# l=[3,5,2,7]
# l2=[]
# for i in range(len(l)):
#     x=i
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     ch=l[i]+rev
#     count=0
#     for j in range(1,ch+1):
#         if ch%j==0:
#             count=count+1
#     if count==2:
#         l[i]=5
#     l2.append(l[i])
# print(l2)

'''13.	Count digits whose factorial is divisible by position '''
# l=[3,5,2,7]
# l2=[]
# count=0
# for i in range(1,len(l)):
#     fact=1
#     for j in range(1,l[i]+1):
#         fact=fact*j
#     if fact%i==0:
#         count=count+1
# print(count)


'''14.	Replace digits where digit² + position is palindrome with 9 '''
# l=[2,3,4,5]
# l2=[]
# for i in range(len(l)):
#     sq=l[i]**2+i
#     x=sq
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     if rev==sq:
#         l[i]=9
#     l2.append(l[i])
# print(l2)


'''15.	Keep digits whose cube ends with same digit '''
# l=[2,4,5,9]
# l2=[]
# for i in l:
#     cube=i**3
#     if cube%10==i:
#         l2.append(i)
# print(l2)

'''16.	Replace digits where (digit + position) is divisible by 4 with 7 '''
# l=[2,4,5,9]
# l2=[]
# for i in range(len(l)):
#     if (l[i]+i)%4==0:
#         l[i]=7
#     l2.append(l[i])
# print(l2)

'''17.	Count positions where digit equals factorial of position '''
# l=[1,1,2,6,5]
# count=0
# for i in range(len(l)):
#     fact=1
#     for j in range(1,i+1):
#         fact=fact*j
#     if fact==l[i]:
#         count=count+1
# print(count)

'''18.	Replace digits whose XOR with position is odd with 3 '''
# l=[1,1,2,6,5]
# l2=[]
# for i in range(len(l)):
#     if (l[i]^i)%2!=0:
#         l[i]=3
#     l2.append(l[i])
# print(l2)

''' 21.	Find elements whose frequency is a perfect square '''
# l=[1,1,2,6,5,5,5,5]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     root=count**0.5
#     sq=root**2
# if sq==count:
#     print(i)

'''22.	Replace elements having odd frequency with their negative '''
# l=[1,2,2,3,3,3,4,4,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count%2!=0:
#         i=-i
#     l2.append(i)
# print(l2)

'''23.	Keep only elements whose frequency equals number of digits '''
# l=[12,3,5,12,567,343,567,567]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==len(str(i)) and i not in l2:
#         l2.append(i)
# print(l2)

'''24.	Count elements appearing consecutively more than twice '''
# l=[1,1,2,2,2,3,4,4,4]
# count=0
# for i in range(len(l)-2):
#     if l[i]==l[i+1]==l[i+2]:
#         count+=1
# print(count)

'''25.	Find longest streak of same element '''
# l=[5,5,5,5,2,2,7]
# max=1
# current=1
# for i in range(len(l)-1):
#     if l[i]==l[i+1]:
#         current+=1
#     else:
#         if current>max:
#             max=current
#         current=1
# if current>max:
#     max=current
# print(max)


'''find longest streak of even numbers '''
# l=[2,4,8,6,2,3,4,7,6,4,2,10]
# current=1
# max=1
# for i in range(len(l)-1):
#     if (l[i]%2==0) and (l[i+1]%2==0):
#         current+=1
#     else:
#        if current>max:
#         max=current
#        current=1
# if current>max:
#     max=current
# print(max)

'''26.	Replace elements whose frequency is divisible by their value with 0 '''
# l=[4,4,1,4,27,27,27,1,1,9,9]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if i%count==0:
#         i=0
#     l2.append(i)
# print(l2)

'''27.	Find element with second highest frequency '''
# l=[4,4,4,4,27,27,27]
# max_freq=0
# se_max_freq=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>max_freq:
#         se_max_freq=max_freq
#         max_freq=count
#     elif count>se_max_freq and count!=max_freq:
#         se_max_freq=count
# print(f"so the second highest frequency is {se_max_freq} of element {i}")


'''29.	Keep elements whose frequency is prime and value is even '''
# l=[2,4,2,8,8,8,6,9,9,9]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     c=0
#     for k in range(1,count+1):
#         if count%k==0:
#             c+=1
#     if c==2 and i%2==0 and i not in l2:
#         l2.append(i)
# print(l2)


'''30.	Find element with highest frequency among prime numbers '''
# l=[1,2,3,3,4,5,5,5,7,7,9]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=count+1
#     if count==2:
#         l2.append(i)
# max_prime_freq=0
# ans=0
# for i in l2:
#     count=0
#     for j in l2:
#         if i==j:
#             count=count+1
#     if count>max_prime_freq:
#         max_prime_freq=count
#         ans=i
# print(ans)


'''33.	Replace each element with binary equivalent count of 1s '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     binary=bin(i)
#     count=0
#     for i in binary:
#         if i=="1":
#             count=count+1
#     l2.append(count)
# print(l2)

'''31.	Replace each element with sum of factorials of digits '''
# l=[23,145,34]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         fact=1
#         for j in range(1,digit+1):
#             fact=fact*j
#         sum=sum+fact
#         x=x//10
#     l2.append(sum)
# print(l2)
        

'''32.	Replace each element with count of prime digits '''
# l=[2358,149,777]
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
#         if count==2:
#             c+=1
#         x=x//10
#     l2.append(c)
# print(l2)


'''34.	Replace each element with next palindrome number '''
# l = [120,44,98]
# l2 = []
# for i in l:
#     num=i+1
#     while True:
#         x=num
#         rev=0
#         while x>0:
#             digit=x%10
#             rev=rev*10+digit
#             x=x//10
#         if rev==num:
#             l2.append(num)
#             break
#         num+=1
# print(l2)
   

'''36.	Replace each element with sum of cubes of digits '''
# l = [120,44,98]
# l2 = []
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         cube=digit**3
#         sum=sum+cube
#         x=x//10
#     l2.append(sum)
# print(l2)

'''37.	Replace each element with count of trailing zeros in square '''
# l=[10,20,5,50]
# l2=[]
# for i in l:
#     sq=i**2
#     count=0
#     while sq>0:
#         digit=sq%10
#         if digit==0:
#             count=count+1
#         else:
#             break
#         sq=sq//10
#     l2.append(count)
# print(l2)


'''38.	Replace each element with largest prime factor '''
# l=[12,18,20,17]
# l2=[]
# for i in l:
#     large=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=0
#             for k in range(1,j+1):
#                 if j%k==0:
#                     count=count+1
#             if count==2:
#                 if j>large:
#                     large=j
#     l2.append(large)
# print(l2)


'''39.	Replace each element with smallest missing digit '''
# l = [123,567,908,444]
# l2=[]
# for i in l:
#     for j in range(0,10):
#         count=0
#         x=i
#         while x>0:
#             digit=x%10
#             if digit==j:
#                 count+=1
#             x=x//10
#         if count==0:
#             l2.append(j)
#             break
# print(l2)


'''40.	Replace each element with digital root '''
# l=[987,45,999]
# l2=[]
# for i in l:
#     x=i
#     while x>=10:   --> this line checks whether the sum is of 2 digits or greater than 2 digits
#         sum=0
#         while x>0:
#             digit=x%10
#             sum=sum+digit
#             x=x//10
#         x=sum
#     l2.append(x)
# print(l2)

    
'''41.	Find elements whose frequency equals sum of digits '''
# l=[11,11,2,2,2,3,3]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count==sum and i not in l2:
#         l2.append(i)
# print(l2)

'''42.	Replace numbers where reverse is prime with 1 '''
# l=[30,75,44,20]
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
#             count=count+1
#     if count==2:
#         l2.append(1)
#     else:
#         l2.append(i)
# print(l2)


'''44.	Keep numbers where alternating digit sum is even '''
# l = [1234,352,245]
# l2 = []
# for i in l:
#     x = str(i)
#     total = 0
#     for j in range(len(x)):
#         digit = int(x[j])
#         if j % 2 == 0:
#             total = total + digit
#         else:
#             total = total - digit
#     if total % 2 == 0:
#         l2.append(i)
# print(l2)


'''
45.	Replace elements whose digit frequency is unique with 0 
🧠 Correct mental process
For each number:
Count frequency of every digit
Compare those frequencies
If no frequency repeats
Replace number with 0

'''
# l=[122333,112233,1223,5557]
# l2=[]

# for i in l:
#     x=i
#     freq=[]
#     rem=i
#     while x>0:
#         digit=x%10
#         z=rem
#         count=0
#         while z>0:
#             digit2=z%10
#             if digit==digit2:
#                 count+=1
#             z=z//10
        

        
'''1.	Replace elements whose digit sum is even with their reverse '''
# l=[28,428,11,597]
# l2=[]
# for i in l:
#     temp=i
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     rev=0
#     if sum%2==0:
#         while i>0:
#             digit=i%10
#             rev=rev*10+digit
#             i=i//10
#         l2.append(rev)
#     else:
#         l2.append(temp)
# print(l2)

'''2.	Keep numbers whose largest digit is prime '''
# l=[523,724,832,670]
# l2=[]
# for i in l:
#     x=i
#     large=0
#     while x>0:
#         digit=x%10
#         if digit>large:
#             large=digit
#         x=x//10
#     count=0
#     for j in range(1,large+1):
#         if large%j==0:
#             count+=1
#     if count==2:
#         l2.append(i)
# print(l2)


'''4.	Count elements whose first and last digit are same '''
# l=[121,876,956,989,567,787]
# count=0
# for i in l:
#     x=i
#     while x>10:
#         x=x//10
#         fd=x
#         if fd==i%10:
#             count+=1
# print(count)

'''5.	Keep numbers where middle digit is even '''
# l=[123,45890,597]
# l2=[]
# for i in l:
#     x=str(i)
#     mid=len(x)//2
#     if int(x[mid])%2==0:
#         l2.append(i)
# print(l2)

'''6.	Replace numbers having more even digits than odd digits with -1 '''
# l = [2481,1357,2468,1234,90876,555,86420,741]
# l2=[]
# for i in l:
#     x=i
#     count=0
#     count2=0
#     while x>0:
#         digit=x%10
#         if digit%2==0:
#             count+=1
#         else:
#             count2+=1
#         x=x//10
#     if count>count2:
#         i=-1
#     l2.append(i)
# print(l2)
 

'''10.	Replace elements whose digits are in decreasing order with 0 '''
# l=[9751,421,544,123]
# l2=[]
# for i in l:
#     x=str(i)
#     valid=True
#     for j in range(len(x)-1):
#         if x[j]<=x[j+1]:
#             valid=False
#     if valid:
#         l2.append(0)
#     else:
#         l2.append(i)
# print(l2)
   

'''11.	Replace elements where element + index is prime with 1 '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)):
#     prime=l[i]+i
#     count=0
#     for j in range(1,prime+1):
#         if prime%j==0:
#             count+=1
#     if count==2:
#         l[i]=1
#     l2.append(l[i])
# print(l2)

'''12.	Count positions where element = square of position '''
# l=[1,1,4,9,8]
# count=0
# for i in range(len(l)):
#     if l[i]==i**2:
#         count+=1
# print(count)

'''13.	Replace elements where element × index ends with 5 by 0 '''
# l=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# for i in range(len(l)):
#     if (l[i]*i)%10==5:
#         l[i]=0
#     l2.append(l[i])
# print(l2)

'''14.	Keep elements where index factorial is even '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)):
#     fact=1
#     for j in range(1,i+1):
#         fact=fact*j
#     if fact%2==0:
#         l2.append(l[i])
# print(l2)

'''18.	Keep elements where element XOR index is prime '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)):
#     prime=l[i]^i
#     count=0
#     for j in range(1,prime+1):
#         if prime%j==0:
#             count+=1
#     if count==2:
#         l2.append(l[i])
# print(l2)

'''41.	Find numbers whose reverse frequency equals original frequency '''
# l=[12,12,21,21]
# l2=[]
# for i in l:
#     c=0
#     for j in l:
#         if i==j:
#             c+=1
#     x=i
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     c2=0
#     for j in l:
#         if rev==j:
#             c2+=1
#     if c==c2:
#         print(i)

'''42.	Replace elements whose square root is integer with 0 '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     root=i**0.5
#     if root==int(root):
#         i=0
#     l2.append(i)
# print(l2)

'''43.	Count elements whose binary form is palindrome '''
# l=[1,2,3,4,5,6,7,8,9]
# count=0
# for i in l:
#     check=bin(i)[2:]
#     rev=check[::-1]
#     if rev==check:
#         count+=1
# print(count)


'''whether some pair of alternate-position digits has an even product.'''
# l = [1234,2468,1357,4826,9753,8642,1111,9081]
# l2=[]
# for i in l:
#     x=str(i)
#     for j in range(1,len(x)-2):
#         if int(x[j])*int(x[j+2]) %2==0:
#             l2.append(i)
# print(l2)

'''44.	Keep numbers whose alternating product of digits is even '''
# l = [1234,2468,1357,4826,9753,8642,1111,9081]
# l2=[]
# for i in l:
#     x=str(i)
#     prod=1
#     for j in range(0,len(x),2):
#         prod=prod*int(x[j])
#     if prod%2==0:
#         l2.append(i)
# print(l2)

'''45.	Replace elements whose digit sum frequency is prime with -1 '''
# l=[23,14,50,32,41]
# l2=[]
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sum=sum+digit
#         x=x//10
#     count=0
#     for j in l:
#         y=j
#         sum2=0
#         while y>0:
#             digit2=y%10
#             sum2=sum2+digit2
#             y=y//10
#         if sum==sum2:
#             count+=1
#     c=0
#     for k in range(1,count+1):
#         if count%k==0:
#             c+=1
#     if c==2:
#         i=-1
#     l2.append(i)
# print(l2)
   

'''48.	Keep numbers having more prime digits than composite digits '''
# l=[2357,2468,2234,5671,4689,7721,1234,9992]
# l2=[]
# for i in l:
#     x=i
#     c=0
#     c2=0
#     while x>0:
#         digit=x%10
#         count=0
#         for j in range(1,digit+1):
#             if digit%j==0:
#                 count+=1
#         if count==2:
#             c+=1
#         elif count>2:
#             c2+=1
#         x=x//10
#     if c>c2:
#         l2.append(i)
# print(l2)

'''49.	Replace elements whose reverse divisor count is even with 1 '''
# l=[123,21,11,90]
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
#             count+=1
#     if count%2==0:
#         i=1
#     l2.append(i)
# print(l2)

'''13.	Keep elements whose binary form contains more 1s than 0s '''
# l=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# for i in l:
#     count=0
#     count2=0
#     check=bin(i)[2:]
#     for j in check:
#         if j=='1':
#             count+=1
#         elif j=="0":
#             count2+=1
#     if count>count2:
#         l2.append(i)
# print(l2)

'''2.	Replace elements whose binary digit count is prime with -1 '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     binary=bin(i)[2:]
#     count=0
#     for j in binary:
#         count+=1
#     c=0
#     for j in range(1,count+1):
#         if count%j==0:
#             c+=1
#     if c==2:
#         i=-1
#     l2.append(i)
# print(l2)


'''12.	Replace numbers whose alternating digit sum is prime with -1 '''
# l = [1234,352,245,864,975,111,2468,1357]
# l2=[]
# for i in l:
#     x=str(i)
#     sum=0
#     for j in range(0,len(x),2):
#         sum=sum+int(x[j])
#     count=0
#     for k in range(1,sum+1):
#         if sum%k==0:
#             count+=1
#     if count==2:
#         i=-1
#     l2.append(i)
# print(l2)

'''17.	Replace each element with count of unique prime factors '''
# l = [12,18,20,45,7,60,100,84]
# l2=[]
# for i in l:
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count=0
#             for k in range(1,j+1):
#                 if j%k==0:
#                     count+=1
#             if count==2:
#                 temp = i
#                 freq = 0
#                 while temp > 0:
#                     if temp % j == 0:
#                         freq += 1
#                     temp = temp // j
#                 c += 1
#     l2.append(c)
# print(l2)     


'''18.	Keep numbers where even-position digit sum is greater than odd-position digit sum '''
# l=[4826,2468,1230]
# for i in l:
#     x=i
#     pos=1
#     while x>0:
#         digit=x%10
#         if (pos%2==0)>(pos%2!=0):
#             pass
#         x=x//10
#         pos+=1
# print(i)

'''20.	Count elements whose reverse factorial digit sum is prime'''
# l=[1,2,3,4,5,6]
# count=0
# for i in l:
#     fact=1
#     for j in range(1,i+1):
#         fact=fact*j
#     rev=0
#     x=fact
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     sum=0
#     temp=rev
#     while temp>0:
#         digit=temp%10
#         sum=sum+digit
#         temp=temp//10
#     c=0
#     for k in range(1,sum+1):
#         if sum%k==0:
#             c+=1
#     if c==2:
#         count+=1
# print(count)
   

'''Replace each element with count of 1s in binary representation'''
# l=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# for i in l:
#     count=0
#     binary=bin(i)[2:]
#     for j in binary:
#         if j=='1':
#             count+=1
#     l2.append(count)
# print(l2)

'''7.	Replace each element with nearest palindrome prime '''
# l=[121,11,787]
# l2=[]
# for i in l:
#     num=i+1
#     while True:
#         x=num
#         rev=0
#         while x>0:
#             digit=x%10
#             rev=rev*10+digit
#             x=x//10
#         if rev==num:
#             count=0
#             for j in range(1,num+1):
#                 if num%j==0:
#                     count+=1
#             if count==2:
#                 l2.append(num)
#                 break
#         num+=1
# print(l2)

'''10.	Count numbers whose reverse square is palindrome '''
# l=[12,11,13,2,21,10,3]
# count=0
# for i in l:
#     x=i
#     rev=0
#     while x>0:
#         digit=x%10
#         rev=rev*10+digit
#         x=x//10
#     sq=rev**2
#     z=sq
#     rev2=0
#     while z>0:
#         digit2=z%10
#         rev2=rev2*10+digit2
#         z=z//10
#     if sq==rev2:
#         count+=1
# print(count)

''''''























# for i in l:
#     num=i+1
#     while True:
#         x=num
#         rev=0
#         while x>0:
#             digit=x%10
#             rev=rev*10+digit
#             x=x//10
#         if rev==num:
#             l2.append(num)
#             break
#         num+=1
# print(l2)
   
