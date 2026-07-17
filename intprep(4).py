# Nested Loops (Brute Force) 
'''•	Reverse List '''
# l=[1,2,3,4,5]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

'''•	Rotate Left/Right '''
'''left rotate by 2 and 1'''
# 1
# l=[1,2,3,4,5]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)
'''optimized version'''
# l=[1,2,3,4,5]
# l=l[1:]+l[:1]
# print(l)

# 2
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)
'''optimized version'''
# l=[1,2,3,4,5]
# k=2
# l=l[k:]+l[:k]
# print(l)
# --------------------------------------------------------------------------------------------------
'''right rotaion by 1 and 2'''
# 1
# l=[1,2,3,4,5]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)
'''optimized version'''
# l=[1,2,3,4,5]
# l=l[-1:]+l[:-1]
# print(l)

'''•	Bubble Sort ascending order'''
# l=[1,5,4,2,8]
# for i in range(len(l)-1):
#     for j in range(len(l)-1-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

'''•	Selection Sort '''
# l=[1,5,4,2,8]
# for i in range(len(l)):
    # minimum = i                 min stored current index  like l[0]
#     for j in range(i+1,len(l)):
#         if l[j]<l[minimum]:
#             minimum = j
#     l[i],l[minimum]=l[minimum],l[i]
# print(l)

'''•	Pair Sum '''
# l=[1,2,3,4,5]
# target=7
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j] == target:
#             print((l[i],l[j]))

'''•	Pair Product '''
# l=[10,5,2,6]
# target=30
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]*l[j] == target:
#             print((l[i],l[j]))

'''•	Pair Difference '''
# l=[5,20,3,2,50,80]
# target=78
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if abs(l[i]-l[j]) == target:
#             print((l[i],l[j]))

'''•	Pair with GCD > 1 '''
# l=[2,3,4,9]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         x=l[i]
#         y=l[j]
#         gcd=1
#         small=min(x,y)
#         for k in range(1,small+1):
#             if x%k==0 and y%k==0:
#                gcd=k
#         if gcd>1:
#             print((x,y))

'''•	Pair with Same Last Digit '''
# l=[27,45,17,62,82,97]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]%10 == l[j]%10:
#             print((l[i],l[j]))

# optimized
# l=[27,45,17,62,82,97]
# d={}
# for i in l:
#     temp=i
#     key=temp%10
#     if key in d:
#         print(d[key],temp)
#     else:
#         d[key]=temp

'''•	Pair with Same Digit Sum '''
# l=[123,240,330,411,78]
# for i in range(len(l)):
#     sum1=0
#     x=l[i]
#     while x>0:
#         digit=x%10
#         sum1+=digit
#         x=x//10
#     for j in range(i+1,len(l)):
#         sum2=0
#         y=l[j]
#         while y>0:
#             digit=y%10
#             sum2+=digit
#             y=y//10
#         if sum1==sum2:
#             print((l[i],l[j]))

# optimized
# l=[123,240,330,411,78]
# d={}
# for i in l:
#     temp=i
#     digit_sum=0
#     while temp>0:
#         digit=temp%10
#         digit_sum+=digit
#         temp=temp//10
#     if digit_sum in d:
#         print(d[digit_sum],i)
#     else:
#         d[digit_sum]=i

'''•	Pair with Prime Sum '''
# l=[5,8,11,14]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         pr_check=0
#         for k in range(1,sum+1):
#             if sum%k==0:
#                 pr_check+=1
#         if pr_check==2:
#             print(l[i],l[j])

'''•	Zigzag Array '''
# l=[1,2,3,4,5]
# for i in range(len(l)-1):
#     if i%2==0:
#         if l[i]<l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
#     else:
#         if l[i]>l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
# print(l)
    

'''•	Count Inversions '''
# l=[8,4,2,1]
# inversion_count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             inversion_count+=1
# print(inversion_count)
'''"I fix one element using the outer loop. Then I compare it with every element to its right
using the inner loop. Whenever the left element is greater than the right element, it forms an 
inversion because the larger element appears before a smaller one. I increment the inversion count
for every such pair. Finally, the count gives the total number of inversions."'''



'''•	Equilibrium Index '''
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

# frequency dictionary based
'''•	Frequency Count '''
# l=[1,2,1,3,2,1]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Character Frequency '''
# l="madam"
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Word Frequency '''
# word = "django is very very strong"
# word_list=word.split()
# d={}
# for i in word_list:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Maximum Frequency '''
# l=[1,2,1,3,2,1]
# ch_freq=0
# d={}
# for i in l:
#     if i in d:
#        d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>ch_freq:
#         ch_freq=d[i]
#         key=i
# print(key,':',ch_freq ,'is maximum frequency')

'''•	First Non-Repeating '''
# l=[1,1,2,3,4,4]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in l:
#     if d[i]==1:
#         print(i)
#         break

'''•	Count Anagrams '''
# words=["cat","dog","act","god","rat"]
# d={}
# count=0
# for i in words:
#     wrd = ''.join(sorted(i))
#     if wrd in d:
#         d[wrd]=d[wrd]+1
#     else:
#         d[wrd]=1
# for i in d:
#     if d[i]>1:
#         count+=1
# print(count)

'''print anagram groups'''
# words=["cat","dog","act","god","rat"]
# d={}
# for i in words:
#     wrd=''.join(sorted(i))
#     if wrd in d:
#         d[wrd].append(i)
#     else:
#         d[wrd]=[i]
# print(d)

'''print anagram pairs'''
# words=["cat","dog","act","god","rat"]
# d={}
# for i in words:
#     wrd=''.join(sorted(i))
#     if wrd in d:
#         d[wrd].append(i)
#     else:
#         d[wrd]=[i]
# for i in d:
#     ch_pair=d[i]
#     for j in range(len(ch_pair)):
#         for k in range(j+1,len(ch_pair)):
#             print((ch_pair[j],ch_pair[k]))

'''count all anagram words'''
# words=["cat","dog","act","god","rat"]
# d={}
# for word in words:
#     key=''.join(sorted(word))
#     if key in d:
#         d[key]=d[key]+1
#     else:
#         d[key]=1
# count=0
# for key in d:
#     if d[key]>1:
#         count=count+d[key]
# print(count)

'''•Replace Prime Frequency with -1'''
# l=[1,2,2,3,3,3]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in l:
#     ch_prime=d[i]
#     count=0
#     for j in range(1,ch_prime+1):
#         if ch_prime%j==0:
#             count+=1
#     if count==2:
#         d[i]=-1
# print(d)
# for index in range(len(l)):
#     if d[l[index]] == -1:
#         l[index] = -1

# print(l)

'''•	Even Frequency '''
# l=[1,2,2,3,3,3]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]%2==0:
#         print(i)

'''•	Frequency Sort '''
# l=[1,2,2,3,3,3]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# sort_t = sorted(d.items(),key=lambda x:x[1],reverse=True)
# ans=[]
# for element,frequency in sort_t:
#     for i in range(frequency):
#         ans.append(element)
# print(ans)

'''•	Group By Frequency '''
# l=[4,4,5,5,6]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# d2={}
# for i in d:
#     if d[i] in d2:
#         d2[d[i]].append(i)
#     else:
#         d2[d[i]]=[i]

# print(d2)

'''•	Group By Digit Count '''
# l=[1,22,333,44,5555,6]
# d={}
# for i in l:
#     num=i
#     count=0
#     while num>0:
#         digit=num%10
#         count+=1
#         num=num//10
#     if count in d:
#         d[count].append(i)
#     else:
#         d[count]=[i]
# print(d)

'''•	Group By Digit Sum '''
# l=[123,222,321,444,909,99,81,18]
# d={}
# for i in l:
#     num=i
#     sum=0
#     while num>0:
#         digit=num%10
#         sum+=digit
#         num=num//10
#     if sum in d:
#         d[sum].append(i)
#     else:
#         d[sum]=[i]
# print(d)

'''Two Sum'''
# l=[2,7,11,15]
# target=9
# d={}
# for i in l:
#     need=target-i
#     if need in d:
#         print((need,i))
#     d[i]=1
'''Two Sum

Current

↓

Target-Current

(Only One Need)'''

'''•	Two Difference '''
# l=[5,20,3,2,20,80]
# k=78
# d={}
# for i in l:
#     need1=i-k
#     need2=i+k
#     if need1 in d:
#         print((need1,i))
#     elif need2 in d:
#         print((i,need2))
#     d[i]=1
'''"I use a HashMap to store all previously seen numbers. For every current number, 
I check two possible partners: current - k and current + k, because the current number 
can be either the larger or the smaller number in the pair. If either partner already 
exists in the HashMap, I have found a valid pair. Otherwise, I store the current number 
for future lookups."'''
'''Two Difference

Current

↓

Current-K   ← Left Partner

Current+K   ← Right Partner

(Two Needs)'''

'''•	Pair Product '''
# l=[2,4,5,10,8]
# target = 40
# d={}
# for i in l:
#     if target%i==0:
#         need = target//i
#     if need in d:
#         print((i,need))
#     d[i]=True
     
'''•	Pair XOR '''
# l=[2,8,5,7]
# target=10
# d={}
# for i in l:
#     need = i^target
#     if need in d:
#         print(need,i)
#     d[i]=1

'''•	Maximum Sum Subarray of Size K '''
# l=[4,2,1,7,8]
# k=3
# windows_sum=0
# for i in range(k):
#     windows_sum+=l[i]
# max_sum=windows_sum
# for j in range(k,len(l)):
#     windows_sum=windows_sum-l[j-k]+l[j]
#     if windows_sum>max_sum:
#         max_sum=windows_sum
# print(max_sum)

'''•	Minimum Sum Subarray of size k'''
# l = [5,-2,7,1,-4,3]
# k = 3
# window_sum = 0
# for i in range(k):
#     window_sum+=l[i]
# min_sum=window_sum
# for j in range(k,len(l)):
#     window_sum=window_sum-l[j-k]+l[j]
#     if window_sum<min_sum:
#         min_sum=window_sum
# print(min_sum)

'''•	First Negative in Window '''
'''Brute force approach'''
# l = [12,-1,-7,8,-15,30,16,28]
# k=3
# for i in range(len(l)-k+1):
#     store=0
#     for j in range(i,i+k):
#         if l[j]<0:
#             store=l[j]
#             break
#     print(store)

'''optimized approach'''
# l = [12,-1,-7,8,-15,30,16,28]
# k=3
# neg=[]
# # first window
# for i in range(k):
#     if l[i]<0:
#         neg.append(l[i])
# if neg:
#     print(neg[0])
# else:
#     print(0)
# sliding window
# for j in range(k,len(l)):
#     if neg and l[j-k] == neg[0]:
#         neg.pop(0)
#     if l[j]<0:
#         neg.append(l[j])
#     if neg:
#         print(neg[0])
#     else:
#         print(0)
'''"I first process the first window of size k and store all negative numbers in a list. 
The first element of this list always represents the first negative number of the current window. 
As the window slides, I check the element leaving the window. If it is the same as the first negative, 
I remove it from the front of the list. Then I check the new incoming element, and if it is negative, 
I append it to the list. After every slide, if the list is non-empty, its first element is the answer; 
otherwise, I print 0. This avoids scanning every window again and reduces the complexity from O(n×k) 
to O(n) (using a deque for efficient front removal).

1. Build the first window.
2. Store only negative numbers.
3. Window slides → remove outgoing negative if needed.
4. Add incoming negative.
5. Front of the list/deque = First Negative."'''


'''•	Maximum in Window '''
'''Brute force approach'''
# l=[1, 3, -1, -3, 5, 3, 6, 7]
# k=3
# for i in range(len(l)-k+1):
#     max_window = l[i]
#     for j in range(i,i+k):
#         if l[j]>max_window:
#             max_window=l[j]
#     print(max_window)

'''sliding window'''
# from collections import deque
# l=[1, 3, -1, -3, 5, 3, 6, 7]
# k=3
# dq=deque()
# ans=[]
# for i in range(k):
#     while dq and l[dq[-1]]<l[i]:
#         dq.pop()
#     dq.append(i)
# ans.append(l[dq[0]])
# for j in range(k,len(l)):
#     if dq[0]==j-k:
#         dq.popleft()
#     while dq and l[dq[-1]]<l[j]:
#         dq.pop()
#     dq.append(j)
#     ans.append(l[dq[0]])
# print(ans)
    








 

      

 
    



        
  


   











    



    

   


       
       







