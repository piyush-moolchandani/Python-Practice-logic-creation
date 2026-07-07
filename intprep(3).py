'''91.	Keep only composite numbers '''
# l=[1,2,3,4,5,6,7,8,9,0]
# l2=[]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count>2:
#         l2.append(i)
# print(l2)

'''92.	Count pairs where both numbers are prime '''
# l=[2,3,4,5]
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         x=l[i]
#         y=l[j]
#         prime_ch=0
#         for k in range(1,x+1):
#             if x%k==0:
#                 prime_ch+=1
#         prime_ch2=0
#         for m in range(1,y+1):
#             if y%m==0:
#                 prime_ch2+=1
#         if prime_ch==2 and prime_ch2==2:
#             count+=1
# print(count)

'''93.	Rotate only prime numbers '''
# l=[2,4,3,6,5,8,7]
# l2=[]
# l3=[]
# for i in range(len(l)):
#     prime=0
#     for j in range(1,l[i]+1):
#         if l[i]%j==0:
#             prime+=1
#     if prime==2:
#         l2.append(l[i])
#         l3.append(i)
# ans=l2[1:]+l2[:1]
# for i in range(len(l3)):
#     l[l3[i]]=ans[i]
# print(l)

'''94.	Replace elements whose binary 1-count is prime  with "PRIME" '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     bin_ch=bin(i)[2:]
#     count=0
#     for j in bin_ch:
#         if j=="1":
#             count+=1
#     prime_ch=0
#     for k in range(1,count+1):
#         if count%k==0:
#             prime_ch+=1
#     if prime_ch==2:
#         i="PRIME"
#     l2.append(i)
# print(l2)

'''95.	Reverse elements at prime indexes '''
# l=[10,20,30,40,50,60,70]
# l2=[]
# l3=[]
# for i in range(len(l)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         l2.append(i)
#         l3.append(l[i])
# rev=l3[::-1]
# for i in range(len(l3)):
#     l[l2[i]]=rev[i]
# print(l)

'''96.	Count square-root digit sums that are even '''
# l=[16,25,36,144,400]
# count=0
# for i in l:
#     sq_root=int(i**0.5)
#     x=sq_root
#     digit_sum=0
#     while x>0:
#         digit=x%10
#         digit_sum+=digit
#         x=x//10
#     if digit_sum%2==0:
#         count+=1
# print(count)

'''97.	Find pair with GCD > 1 '''
# l=[8,12,15]
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

'''98.	Move perfect squares to front '''
# l=[4,7,9,10,16,18,25]
# l2=[]
# l3=[]
# for i in l:
#     root=int(i**0.5)
#     sq=root**2
#     if i==sq:
#         l2.append(i)
#     else:
#         l3.append(i)
# print(l2+l3)

'''99.	Reverse subarrays whose sum is prime '''
# l=[2,5,1,4,3,6,7]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         sub_sum=0
#         for k in sub:
#             sub_sum+=k
#         prime=0
#         for m in range(1,sub_sum+1):
#             if sub_sum%m==0:
#                 prime+=1
#         if prime==2:
#             print(sub[::-1])

'''100.	Prime frequency-based replacement with (-1)'''
# l=[5,5,5,8,8,9,9,9,9]
# l2=[]
# for i in l:
#     frq=0
#     for j in l:
#         if i==j:
#             frq+=1
#     count=0
#     for k in range(1,frq+1):
#         if frq%k==0:
#             count+=1
#     if count==2:
#         i=-1
#     l2.append(i)
# print(l2)

'''101.	Two Sum '''
# l=[1,2,3,4]
# k=6
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j] == k:
#             print((l[i],l[j]))
'''two sum optimized version'''
# l=[1,2,3,4]
# k=6
# d={}
# for i in l:
#     target=k-i
#     if target in d:
#         print((target,i))
#     d[i]=1

''' three sum using optimized hasing version'''
# l=[1,2,3,4]
# k=9
# d={}
# for i in range(len(l)-2):
#     target=k-l[i]
#     for j in range(i+1,len(l)):
#         need=target-l[j]
#         if need in d:
#             print(l[i],need,l[j])
#         d[l[j]]=1

# l=[1,2,3,4]
# k=9
# d={}
# for i in range(len(l)):
#     # fix value 2 index 0
#     target=k-l[i]
#     # moving to next indexings after 1 the next indexing will be 2,3 elements=3,4
#     for j in range(i+1,len(l)):
#         # next value 4
#         need=target-l[j]
#         if need in d:
#             print((l[i],need,l[j]))
#         d[l[j]]=1

''' four sum '''
# l=[1,2,3,4,5]
# k=14
# for i in range(len(l)):
#     target=k-l[i]
#     for j in range(i+1,len(l)):
#         target2=target-l[j]
#         d={}
#         for m in range(j+1,len(l)):
#             need=target2-l[m]
#             if need in d:
#                 print(l[i],l[j],need,l[m])
#             d[l[m]]=1

'''102.	Merge Sorted Arrays '''
# l1=[1,3,5,7]
# l2=[2,4,6,8]
# l3=[]
# i=0
# j=0
# while i<len(l1) and j<len(l2):
#     if l1[i]<l2[j]:
#         l3.append(l1[i])
#         i+=1
#     else:
#         l3.append(l2[j])
#         j+=1
# print(l3)

'''103.	Next Greater Element '''
# l=[1,3,5]
# l2=[]
# for i in range(len(l)):
#     found=-1
#     for j in range(i+1,len(l)):
#         if l[j]>l[i]:
#             found=l[j]
#             break
#     l2.append(found)
# print(l2)            

'''104.	Previous Smaller Element '''
# l=[1,3,5,8]
# l2=[]
# for i in range(len(l)):
#     found=-1
#     for j in range(i-1,-1,-1):
#         if l[j]<l[i]:
#             found=l[j]
#             break
#     l2.append(found)
# print(l2)

'''105.	Majority Element '''
# l=[1,1,2,1,3]
# half=len(l)/2
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq>half:
#         break
# print("the majority element is",i)

'''106.	Leaders in Array '''
# l=[16,17,4,3,5,2]
# for i in range(len(l)):
#     leader=True
#     for j in range(i+1,len(l)):
#         if l[j]>=l[i]:
#             leader=False
#             break
#     if leader:
#         print(l[i])

'''107.	Equilibrium Index '''
# l=[1,3,5,2,2]
# for i in range(len(l)):
#     left_sum=0
#     right_sum=0
#     for j in range(0,i):
#         left_sum+=l[j]
#     for k in range(i+1,len(l)):
#         right_sum+=l[k]
#     if left_sum==right_sum:
#         print(i)

'''111.	Find Pair Closest to Target '''
# l=[3,8,12,17,21,25,30]
# target=28
# min_target=999
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         diff=abs(target-sum)
#         if diff<min_target:
#             min_target=diff
#             x=l[i]
#             y=l[j]
# print(x,y)

'''112.	Find Pair Closest to Zero '''
# l=[-20,-10,-5,-2,1,4,8,15]
# min_pair=999
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         diff=abs(sum)
#         if diff<min_pair:
#             min_pair=diff
#             x=l[i]
#             y=l[j]
# print(x,y)


           



            
            
            




    
        

    
    





