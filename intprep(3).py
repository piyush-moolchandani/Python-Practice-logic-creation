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
# while i<len(l1):
#     l3.append(l1[i])
#     i+=1
# while j<len(l2):
#     l3.append(l2[j])
#     j+=1
# print(l3)

'''Remove Duplicates from Sorted Array using 2 pointers'''
# l=[1,1,2,2,3,3,4,5,5]
# i=0
# for j in range(1,len(l)):
#     if l[i]!=l[j]:
#         i+=1
#         l[i]=l[j]
# print(l[:i+1])

'''move zeros using two pointers'''
# l=[0,1,0,3,12]
# l2=[]
# i=0
# for j in range(1,len(l)):
#     if l[j]!=0:        
#         l[i],l[j]=l[j],l[i]
#         i+=1
# print(l)

'''Remove a Given Element (LeetCode 27)'''
# l=[3,2,2,3,4,3,5]
# x=3
# i=0
# for j in range(len(l)):
#     if l[j]!=x:
#         l[i]=l[j]
#         i+=1
# print(l[:i])

'''103.	Next Greater Element '''
# l=[4,5,2,25]
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
# l=[10,4,2,20,40,12,30]
# l2=[]
# for i in range(len(l)):
#     found=-1
#     for j in range(i-1,-1,-1):
#         if l[j]<l[i]:
#             found=l[j]
#             break
#     l2.append(found)
# print(l2)

'''106.	Leaders in Array '''
# l=[16,17,4,3,5,2]
# for i in range(len(l)):
#     leader=True
#     for j in range(i+1,len(l)):
#         if l[j]>l[i]:
#             leader=False
#             break
#     if leader:
#         print(l[i])

'''107.	Equilibrium Index '''
# l=[1,3,5,2,2]
# for i in range(len(l)):
#     left=0
#     right=0
#     for j in range(0,i):
#         left+=l[j]
#     for k in range(i+1,len(l)):
#         right+=l[k]
#     if left==right:
#         print(i)

'''108.	Longest Consecutive Sequence '''
# l=[100,4,200,1,3,2]
# max_len=0
# ans=[]
# for i in l:
#     temp=[]
#     num=i
#     while num in l:
#         temp.append(num)
#         num=num+1
#     if len(temp)>max_len:
#         max_len=len(temp)
#         ans=temp
# print(ans)
'''"I iterate over every element of the array and treat each element as a possible starting point 
of a consecutive sequence. From that starting value, I keep checking whether the next integer 
(num + 1) exists in the array. As long as consecutive numbers are present, I build the current 
sequence in a temporary list. After the sequence ends, I compare its length with the maximum length 
found so far. If it is longer, I update the answer."'''

# optimized
'''"Yes. In my brute-force approach, the same sequence is explored multiple times. 
For example, if the sequence is 1,2,3,4, then I start from 1, then again from 2, then from 3, 
causing repeated work. By using a HashSet and starting only from numbers whose previous element 
(num-1) is absent, this duplicate work can be eliminated, reducing the complexity to O(n)."'''

# l=[100,4,200,1,3,2]
# s=set(l)
# max_len=0
# ans=[]
# for i in s:
#     if i-1 not in s:
#         temp=[]
#         num=i
#         while num in s:
#             temp.append(num)
#             num+=i
#         if len(temp)>max_len:
#             max_len=len(temp)
#             ans=temp
# print(ans)

'''113.	Find Triplet Sum = Target '''
# l=[1,2,3,4,5,6,7]
# target=12
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         for k in range(j+1,len(l)):
#             if l[i]+l[j]+l[k] == target:
#                 print((l[i],l[j],l[k]))

# optimized hashmap approach
# l=[1,2,3,4,5,6,7]
# k=12
# for i in range(len(l)-2):
#     d={}
#     Target=k-l[i]
#     for j in range(i+1,len(l)):
#         need=Target-l[j]
#         if need in d:
#             print(l[i],need,l[j])
#         d[l[j]]=1

'''114.	Find Triplet Sum = Zero '''
# l=[-1,0,1,2,-1,-4]
# target=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         for k in range(j+1,len(l)):
#             if l[i]+l[j]+l[k] == target:
#                 print((l[i],l[j],l[k]))


'''115.	Maximum Product Pair '''
# l=[-10,-20,5,6,-2]
# max_prod=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         prod=l[i]*l[j]
#         if prod>max_prod:
#             max_prod=prod
#             x=l[i]
#             y=l[j]
# print((x,y))

'''optimized approach 1 using sorting '''
# l=[-10,-20,5,6,-2]
# l.sort()
# prod1 = l[0]*l[1]
# prod2 = l[-1]*l[-2]
# if prod1>prod2:
#     print(l[0],l[1])
# else:
#     print(l[-1],l[-2])
'''Maximum product sirf do largest ya do smallest numbers se hi aa sakta hai. 
Isliye poore array ke har pair ko check karne ki zarurat nahi hai.'''

'''optimized approach 2 more good without sorting '''
# l=[-10,-20,5,6,-2]
# max1=max2=float('-inf')
# min1=min2=float('inf')
# for i in l:
#     if i>max1:
#         max2=max1
#         max1=i
#     elif i>max2:
#         max2=i
#     if i<min1:
#         min2=min1
#         min1=i
#     elif i<min2:
#         min2=i
# if min1 * min2 > max1 * max2:
#     print((min1,min2))
# else:
#     print(max1,max2)

'''116.	Maximum Difference '''
# l=[2,3,10,6,4,8,1]
# max_diff=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         diff=l[j]-l[i]
#         if diff>max_diff:
#             max_diff=diff
#             x=l[i]
#             y=l[j]
# print((x,y))

'''optimized version '''
# l=[2,3,10,6,4,8,1]
# min_so_far=l[0]
# max_diff=0
# for i in range(1,len(l)):
#     diff=l[i]-min_so_far
#     if diff>max_diff:
#         max_diff=diff
#         x=min_so_far
#         y=l[i]
#     if l[i]<min_so_far:
#         min_so_far=l[i]
# print((x,y))
'''"While traversing the array, I maintain the smallest element seen so far. 
For every current element, I calculate the difference between the current element and that minimum. 
If this difference is larger than the previous maximum, I update the answer. After that, 
I check whether the current element itself becomes the new minimum for future iterations."'''

'''118.	Rearrange Array in Wave Form '''
# l=[1,2,3,4,5]
# for i in range(0,len(l)-1,2):
#     l[i],l[i+1]=l[i+1],l[i]
# print(l)         

# optimized approach
# l=[1,5,2,6,3]
# for i in range(len(l)-1):
#     if i%2==0:
#         if l[i]<l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
#         else:
#             if l[i]>l[i+1]:
#                 l[i],l[i+1]=l[i+1],l[i]
# print(l)

'''120.	Search + Pagination Logic (useful for Django interviews) '''
# l=[
# "apple",
# "banana",
# "mango",
# "grapes",
# "pineapple",
# "orange",
# "apple juice",
# "apple pie"
# ]
# search="apple"
# page=2
# page_size=2
# # search
# filter=[]
# for i in l:
#     if search.lower() in i.lower():
#         filter.append(i)
# # pagination
# start = (page-1)*page_size
# end = start+page_size
# print(filter[start:end])

''' interviewer favourite function version '''
# def search_pagination(l,search,page,page_size):
#     filtered=[]
#     for i in l:
#         if search.lower() in i.lower():
#             filtered.append(i)
#     start=(page-1)*page_size
#     end=start+page_size
#     return filtered[start:end]
# l=[
# "apple",
# "banana",
# "mango",
# "grapes",
# "pineapple",
# "orange",
# "apple juice",
# "apple pie"
# ]
# print(search_pagination(l,'apple',2,2))
'''"I first filter the complete dataset based on the search keyword. 
After obtaining the filtered results, I calculate the starting and ending 
indices using the page number and page size, and return only that portion 
of the filtered list. Searching is done before pagination because paginating 
first may hide matching records that exist on later pages. The overall time 
complexity is O(n), and the extra space is O(n) due to the filtered list."'''
 





            














           



            
            
            




    
        

    
    





