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
           
    

        





        

      

        
    
    




    









    

