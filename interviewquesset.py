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

'''43.	Swap first and last element '''
# l=[1,2,3,4,5]
# l[0],l[-1]=l[-1],l[0]
# print(l)

'''44.	Swap largest and smallest element '''
# l=[4,5,7,1,5,8,9,2]
# large=l[0]
# small=l[0]
# for i in range(len(l)):
#     if l[i]>large:
#         large=l[i]
#         large_index=i
#     elif l[i]<small:
#         small=l[i]
#         small_index=i
# l[large_index],l[small_index]=l[small_index],l[large_index]
# print(l)

'''91.	Rotate list left by 1 position '''
# l=[1,2,3,4,5]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)

'''92.	Rotate list right by k positions '''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     lv=l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=lv
# print(l)

'''98.	Zigzag arrange (small > big < small > big...) '''
'''98. Zigzag arrange (> < > <)'''

# l=[4,7,1,9,2]

# for i in range(len(l)-1):

#     if i%2==0:

#         if l[i]<l[i+1]:

#             l[i],l[i+1]=l[i+1],l[i]

#     else:

#         if l[i]>l[i+1]:

#             l[i],l[i+1]=l[i+1],l[i]

# print(l)

'''99.	Sort only even elements, keep odd positions same '''
# l=[9,8,7,6,5,4,3,2,1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if ((l[j]%2==0) > (l[i])%2==0):
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)


'''100.	Merge two sorted lists into one sorted list '''
# l1=[1,3,5]
# l2=[2,4,6]
# l3=[]
# i=0
# j=0
# while i<len(l1) and j<(len(l2)):
#     if l1[i]<l2[j]:
#         l3.append(l1[i])
#         i+=1
#     else:
#         l3.append(l2[j])
#         j+=1
# print(l3)

'''111.	Find element with second least frequency '''
# l=[1,3,3,2,2,2,4,4,4,4]
# min=9
# se_min=9
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count<min:
#         se_min=min
#         min=count
#     elif count<se_min and count!=min:
#         se_min=count
#         x=i
# print(x)
   

'''112.	Find all elements appearing odd number of times '''
# l=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count%2!=0 and i not in l2:
#         l2.append(i)
# print(l2)

'''115.	Remove first repeating element only '''
# l=[1,2,2,3,3,3]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count>1:
#         l.remove(i)
#         break
# print(l)

'''116.	Remove last repeating element only '''
# l=[1,2,2,3,3,3]
# for i in range(len(l)-1,-1,-1):
#     count=0
#     for j in l:
#         if l[i]==j:
#             count+=1
#     if count>1:
#         x=l[i]
#         while x in l:
#             l.remove(x)
#         break
# print(l)

'''117.	Find first element whose frequency > average frequency '''
# l=[4,4,5,5,5,6]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count not in l2:
#         l2.append(count)
# sum=0
# for i in l2:
#     sum=sum+i
# avg=sum/len(l2)
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count>int(avg):
#         print(i)
#         break

'''118.	Count how many distinct repeated elements exist '''
# l=[1,2,2,3,3,3,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count>1 and i not in l2:
#         l2.append(i)
# print(l2)
# print(len(l2))

'''119.	Print elements sorted by frequency descending '''
'''27.	Replace elements whose binary 1-count frequency is prime with 6 '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     count=0
#     ch=bin(i)[2:]
#     for j in ch:
#         if j=='1':
#             count+=1
#     c=0
#     for k in range(1,count+1):
#         if count%k==0:
#             c+=1
#     if c==2:
#         i=6
#     l2.append(i)
# print(l2)

'''131.	Find pair whose sum is closest to k '''
# l=[1,4,7,10]
# l2=[]
# k=15
# small=9
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         diff=abs(k-sum)
#         if diff<small:
#             small=diff
#             x=l[i]
#             z=l[j]
# print(x,z)

'''132.	Find pair whose product is minimum '''
# l=[1,4,7,10]
# min_prod=999999
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         prod=l[i]*l[j]
#         if prod<min_prod:
#             min_prod=prod
#             x=l[i]
#             z=l[j]
# print((x,z))

'''133.	Count pairs with both numbers prime '''
# l=[2,3,4,5,6,7]
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         pr=(l[i],l[j])
#         x=pr[0]
#         z=pr[1]
#         c=0
#         for k in range(1,x+1):         ----------> {damn great work}
#             if x%k==0:
#                 c+=1
#         c2=0
#         for m in range(1,z+1):
#             if z%m==0:
#                 c2+=1
#         if c==2 and c2==2:
#             count+=1
# print(count)

'''134.	Find pair with same last digit '''
# l=[12,25,37,42,55]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         pair=(l[i],l[j])
#         x=pair[0]%10
#         z=pair[1]%10
#         if x==z:
#             print(pair)

'''135.	Count pairs where one is square of another '''
# l=[2,4,3,9,5]
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         pair=(l[i],l[j])
#         if pair[0]**2==pair[1]:
#             count+=1
# print(count)

'''136.	Find triplet with maximum sum '''
# l=[1,4,7,10,5]
# max_sum=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         for k in range(j+1,len(l)):
#             sum=l[i]+l[j]+l[k]
#             if sum>max_sum:
#                 max_sum=sum
#                 x=l[i]
#                 y=l[j]
#                 z=l[k]
# print((x,y,z))

'''137.	Count triplets with all distinct values '''
'''151.	Find first element whose frequency is odd and > average frequency '''
# l=[1,2,2,3,3,3,4,4,4,4,5,5,5]
# l1=[]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if i not in l1:
#         l2.append(count)
#         l1.append(i)
# sum=0
# for i in l2:
#     sum=sum+i
# avg=sum/len(l2)
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count%2!=0 and count>avg:
#         print(i)
#         break

'''137.	Count triplets with all distinct values '''
# l=[1,2,2,3]
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         for k in range(j+1,len(l)):
#             triplets=(l[i],l[j],l[k])
#             a=l[i]
#             b=l[j]
#             c=l[k]
#             if a!=b and a!=c and b!=c:
#                 count+=1
# print(count)


'''138.	Find pair with gcd > 1 '''
# l=[2,3,4,9,6]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         a=l[i]
#         b=l[j]
#         gcd=1
#         small=min(a,b)
#         for k in range(1,small+1):
#             if a%k==0 and b%k==0:
#                 gcd=k
#         if gcd>1:
#             print((a,b))

'''139.	Find pair with minimum absolute difference '''
# l=[1,4,7,10]
# small=999
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         a=l[i]
#         b=l[j]
#         diff=abs(a-b)
#         if diff<small:
#             small=diff
#             x=a
#             y=b
# print((x,y))
        

'''140.	Print all pairs with equal sum'''
# l=[1,2,3,4,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         sum1=l[i]+l[j]
#         for k in range(i+1,len(l)):
#             for m in range(k+1,len(l)):
#                 sum2=l[k]+l[m]
#                 if sum1==sum2:
#                     if i!=k and i!=m and j!=k and j!=m:
#                         print((l[i],l[j]),(l[k],l[m]))
           

'''41.	Rotate left by 2 positions '''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)

'''42.	Rotate right by 2 positions '''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     lv=l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=lv
# print(l)    

'''43.	Reverse only first half of list '''
# l=[1,2,3,4,5,6]
# mid=len(l)//2
# l2=l[0:mid]
# l3=l[mid:]
# l4=[]
# for i in range(len(l2)-1,-1,-1):
#     l4.append(l2[i])
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
# l=[1,2,3,4,5,6,7,8,9]
# l2=[i for i in l if i%2==0]          -------->[list comphrension]
# l3=[i for i in l if i%2!=0]
# print(l2+l3)

'''47.	Arrange positives first, negatives later '''
# l=[1,-2,3,-4,5,-6,7,-8,-9]
# l2=[i for i in l if i>0] + [i for i in l if i<0]
# print(l2)

'''49.	Merge two sorted lists into one sorted list '''
# l=[1,3,5]
# l2=[2,4,6]
# l3=[]
# i=0
# j=0
# while i<len(l) and j<(len(l2)):
#     if l[i]<l2[j]:
#         l3.append(l[i])
#         i+=1
#     else:
#         l3.append(l2[j])
#         j+=1
# print(l3)

'''61.	Find all subarrays with sum = k '''
# l=[1,2,3,4,5]
# k=5
# for i in range(len(l)):
#     sum=0
#     for j in range(i,len(l)):
#         sum=sum+l[j]
#         if sum==k:
#             print(l[i:j+1])


'''62.	Find longest subarray with equal 0s and 1s '''
# l=[0,1,0,1,1]
# max_len=0
# for i in range(len(l)):
#     count=0
#     count2=0
#     for j in range(i,len(l)):
#         if l[j]==1:
#             count+=1
#         elif l[j]==0:
#             count2+=1
#         if count==count2:
#             length=j-i+1
#             if length>max_len:
#                 max_len=length
#                 z=l[i:j+1]
# print(z)
# print(max_len)

'''11.	Print elements greater than left neighbor only '''
# l=[3,5,2,8,1]
# l2=[]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         l2.append(l[i+1])
# print(l2)

'''12.	Print elements smaller than right neighbor only '''
# l=[3,5,2,8,1]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         print(l[i])

'''13.	Remove only first duplicate occurrence of each repeated value '''
# l=[1,2,2,3,3,3,4,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l2:
#         if i==j:
#             count+=1
#     if count!=1:
#         l2.append(i)
# print(l2)

'''14.	Keep only values appearing exactly twice '''
# l=[1,2,2,3,3,4,4,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count==2 and i not in l2:
#         l2.append(i)
# print(l2)
 
'''17.	Keep only composite numbers '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count>2:
#         l2.append(i)
# print(l2)

'''19.	Replace negative even numbers with 0 '''
# l=[1,-2,3,-4,5,6]
# l2=[]
# for i in l:
#     if i%2==0 and i<0:
#         l2.append(0)
#     else:
#         l2.append(i)
# print(l2)

'''27.	Replace each element with distance from max '''
# l=[1,2,3,4,5,6,7,40,8,9]
# l2=[]
# for i in l:
#     diff=abs(i-max(l))
#     l2.append(diff)
# print(l2)

'''51.	Check if list can become sorted by one swap '''
# l=[1,5,3,4,2]  
# l[1],l[4]=l[4],l[1]
# print(l)

'''52.	Find pair whose sum is closest to zero '''
# l=[-8,-3,2,4,7]
# small=999
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         diff=abs(sum)
#         if diff<small:
#             small=diff
#             x=l[i]
#             y=l[j]
# print((x,y))

'''53.	Find all triplets with sum = 0 '''
# l=[-1,0,1,2,-1,-4]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         for k in range(j+1,len(l)):
#             if l[i]+l[j]+l[k]==0:
#                 print((l[i],l[j],l[k]))

'''54.	Find maximum product of any two elements '''
# l=[1,4,7,10]
# max_check=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         prod=l[i]*l[j]
#         if prod>max_check:
#             max_check=prod
#             x=l[i]
#             y=l[j]
# print((x,y))

'''56.	Find longest consecutive increasing subarray '''
# l=[1,2,3,1,2,3,4]
# max_len=1
# x=[l[0]]
# for i in range(len(l)):
#     temp=[l[i]]
#     for j in range(i+1,len(l)):
#         if l[j]>l[j-1]:
#             temp.append(l[j])
#         else:
#             break
#     if len(temp)>max_len:
#         max_len=len(temp)
#         x=temp
# print(x)
        
'''| Variable | Meaning                     |
| -------- | --------------------------- |
| temp     | current increasing subarray |
| max_len  | maximum length found        |
| x        | longest subarray answer     |
| i        | starting index              |
| j        | moving forward              |
'''

'''57.	Find longest consecutive decreasing subarray '''
# l=[1,2,3,4,3,2,1]
# max_len=1
# x=[l[0]]
# for i in range(len(l)):
#     temp=[l[i]]
#     for j in range(i+1,len(l)):
#         if l[j]<l[j-1]:
#             temp.append(l[j])
#         else:
#             break
#     if len(temp)>max_len:
#         max_len=len(temp)
#         x=temp
# print(x)

'''3.	Count elements whose square root digit sum is even '''
# from math import sqrt
# l=[4,9,16,25,169]
# count=0
# for i in l:
#     root=int(sqrt(i))
#     sum=0
#     while root>0:
#         digit=root%10
#         sum=sum+digit
#         root=root//10
#     if sum%2==0:
#         count+=1
# print(count)

'''58.	Replace each element with next smaller element '''
# l=[5,2,8,6,3]
# l2=[]
# for i in range(len(l)):
#     found=False
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i]=l[j]
#             found=True
#             break
#     if found==False:
#         l[i]=-1
# print(l)

'''59.	Replace each element with previous greater element '''
# l=[5,2,8,6,3]
# l2=[]
# for i in range(len(l)):
#     found=False
#     for j in range(i-1,-1,-1):
#         if l[j]>l[i]:
#             l2.append(l[j])
#             found=True
#             break
#     if found==False:
#         l2.append(-1)
# print(l2)
    
'''60.	Find all equilibrium indices '''
# l=[1,3,5,2,2]
# for i in range(len(l)):
#     left_sum=0
#     right_sum=0
#     for j in range(i):
#         left_sum=left_sum+l[j]
#     for k in range(i+1,len(l)):
#         right_sum=right_sum+l[k]
#     if left_sum==right_sum:
#         print(i)


'''43.	Arrange elements by distance from median '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# l.sort()
# n=len(l)
# if n%2!=0:
#     median=l[n//2]
# else:
#     median=(l[n//2]+l[n//2-1])/2
# for i in l:
#     diff=abs(i-median)
#     l2.append(diff)
# print(l2)

'''44.	Reverse elements at prime indexes only '''
# l=[11,12,13,1,4,15,16,17,18,19]
# l2=[]
# for i in range(len(l)):
#     x=l[i]
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         rev=0
#         while x>0:
#             digit=x%10
#             rev=rev*10+digit
#             x=x//10
#         l2.append(rev)
#     else:
#         l2.append(l[i])
# print(l2)


'''45.	Swap elements at even and odd indexes '''
# l=[10,20,30,40,50,60]
# for i in range(len(l)):
#     if i%2==0:
#         l[i],l[i+1]=l[i+1],l[i]
# print(l)

'''46.	Rotate array by number of odd elements (if rotation not given then assume left)'''
# l=[1,2,3,4,5,8]
# count=0
# for i in l:
#     if i%2!=0:
#         count+=1
# k=count
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)

''' rotate array right with number of composite odd  elements'''
# l=[1,2,3,4,5,6,7,8,9,15]
# total_comp=0
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count>2 and i%2!=0:
#         total_comp+=1
# k=total_comp
# for i in range(k):
#     lv=l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=lv
# print(l)

'''47.	Group elements by number of digits '''
# l=[1,22,333,44,5555,6]
# d={}
# for i in l:
#     x=i
#     count=0
#     while x>0:
#         digit=x%10
#         count+=1
#         x=x//10
#     if count not in d:
#         d[count]=[]
#     d[count].append(i)
# print(d)
    
'''48.	Arrange numbers so that even digits come before odd digits (inside number) '''
# l=[123456,573218,482731,914263,785421]
# l2=[]
# for i in l:
#     even=""
#     odd=""
#     for j in str(i):
#         if int(j)%2==0:
#             even=even+j
#         else:
#             odd=odd+j
#     l2.append(even+odd)
# print(l2)


'''49.	Reverse subarray where sum is maximum '''
# l=[1,-2,3,4,-1]
# max_sum=0
# for i in range(len(l)):
#     sum=0
#     for j in range(i,len(l)):
#         sum=sum+l[j]
#         if sum>max_sum:
#             max_sum=sum
#             print(l[i:j+1])

'''50.	Arrange array in wave form (a ≥ b ≤ c ≥ d...) '''
# l=[1,2,3,4,5]
# for i in range(0,len(l)-1,2):
#     l[i],l[i+1]=l[i+1],l[i]
# print(l)

# small<big
# l=[1,2,3,4,5]
# for i in range(1,len(l)-1,2):
#     l[i],l[i+1]=l[i+1],l[i]
# print(l)

'''53.	Rotate only prime numbers in array '''
# l=[2,4,3,6,5,8,7]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         l2.append(i)
# fi=l2[0]
# for i in range(len(l2)-1):
#     l2[i]=l2[i+1]
# l2[-1]=fi
# k=0
# for i in range(len(l)):
#     count=0
#     for j in range(1,l[i]+1):
#         if l[i]%j==0:
#             count+=1
#     if count==2:
#         l[i]=l2[k]
#         k+=1
# print(l)

'''51.	Find subarray where first and last element are equal '''
# l=[4,6,4,2,1]
# for i in range(len(l)):
#     l2=[]
#     for j in range(i,len(l)):
#         l2.append(l[j])
#         if l2[0]==l2[-1]:
#             print(l2)

'''52.	Rearrange array so that all duplicates come together '''
# l=[1,2,3,2,1,4,3]
# l2=[]
# for i in l:
#     if i not in l2:
#         for j in l:
#             if i==j:
#                 l2.append(i)
# print(l2)

# ✅ Condition meaning
# if i not in l2
# means:
# "Agar ye number pehle process nahi hua,
# tabhi uske saare duplicates append karo"
# 🧠 VERY IMPORTANT
# Condition:
# duplicates ko rok nahi rahi
# It only prevents:
# same NUMBER ko dubara process karna
# 💡 SUPER SIMPLE UNDERSTANDING
# Outer loop:
# ek number choose karta
# Inner loop:
# us number ke saare copies dhundta
# Condition:
# same number ko repeat processing se bachati


'''54.	Replace every element with nearest even element '''

'''55.	Reverse only negative numbers positions '''
# l=[1,-2,3,-4,5,-6]
# l2=[]
# for i in l:
#     if i<0:
#         l2.append(i)
# l3=[]
# for j in range(len(l2)-1,-1,-1):
#     l3.append(l2[j])
# k=0
# for i in range(len(l)):
#     if l[i]<0:
#         l[i]=l3[k]
#         k+=1
# print(l)

'''56.	Arrange elements in increasing-decreasing alternate form '''
# l=[8,1,3,7,0,1]
# for i in range(1,len(l)-1,2):
#     l[i],l[i+1]=l[i+1],l[i]
# print(l)

'''57.	Move all perfect square numbers to front '''
# from math import isqrt
# l=[8,4,7,9,10,16]
# l2=[]
# for i in l:
#     if isqrt(i)**2==i:
#         l2.append(i)
# l3=[]
# for i in l:
#     if isqrt(i)**2!=i:
#         l3.append(i)
# print(l2+l3)

'''58.	Find longest alternating even-odd subarray '''
# l=[1,2,3,4,6,7,8]
# for i in range(len(l)):
#     max_array=0
#     for j in range(i,len(l)):
#         if l[j]%2!=0 and l[j+1]%2==0:
#             print(l[i:j+1])

'''59.	Rearrange array so that smallest, largest appear alternately '''
# l=[1,2,3,4,5]
# for i in range(1,len(l)-1,2):
#     l[i],l[i+1]=l[i+1],l[i]
# print(l)

'''Two Sum'''
# l=[1,5,8,2]
# target=10
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print((l[i],l[j]))

'''Reverse string'''
# x='python'
# rev=""
# for i in range(len(x)-1,-1,-1):
#     rev=rev+x[i]
# print(rev)

'''check pallindrome'''
# ch='madam'
# rev=''
# for i in range(len(ch)-1,-1,-1):
#     rev=rev+ch[i]
# if rev==ch:
#     print("The string is pallindrome")

'''Frequency Count'''
# x='aabccddd'
# checked=''
# for i in x:
#     if i not in checked:
#         freq=0
#         for j in x:
#             if i==j:
#                 freq=freq+1
#         print(i,":",freq)
#         checked=checked+i

'''65.	Rearrange array so every element becomes product of neighbors '''
# l=[2,3,4,5]
# l2=[]
# l2.append(l[0]*l[1])
# for i in range(1,len(l)-1):
#     l2.append(l[i-1]*l[i+1])
# l2.append(l[-2]*l[-1])
# print(l2)

'''69.	Rearrange array so odd indexes contain greater elements than neighbors '''
# l=[1,2,3,4,5]
# for i in range(len(l)-1):
#     if i%2!=0:
#         l[i],l[i+1]=l[i+1],l[i]
# print(l)

'''66.	Find longest mountain subarray (increase then decrease) '''
# A simple beginner brute-force approach:
# l=[1,2,1,3,5,4,2]
# max_len=0
# ans=[]
# for i in range(len(l)):
#     for j in range(i+2,len(l)):
#         sub=l[i:j+1]
#         peak=sub.index(max(sub))
#         if peak!=0 and peak!=len(sub)-1:
#             left=True
#             right=True
#             for k in range(peak):
#                 if sub[k]>=sub[k+1]:
#                     left=False
#             for k in range(peak,len(sub)-1):
#                 if sub[k]<=sub[k+1]:
#                     right=False
#             if left and right:
#                 if len(sub)>max_len:
#                     max_len=len(sub)
#                     ans=sub
# print(ans)

'''67.	Arrange elements by closeness to average of array '''
# l=[2,4,6,8,10]
# l2=[]
# l3=[]
# sum=0
# for i in l:
#     sum=sum+i
# avg=sum/len(l)
# for j in l:
#     dis=abs(avg-j)
# ---------x---------

 
    



   

    




  
   
    

  
   




    


     
    



   

            

       

           




    











    



            





        

      

        
    
    




    









    

