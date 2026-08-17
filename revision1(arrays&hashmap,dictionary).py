'''•	Reverse Array '''
# l=[1,2,3,4,5,6]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

'''optimized approach using two pointers'''
# l=[1,2,3,4,5,6]
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# print(l)
# ----------------------------------------------------------------------------------------------
'''•	Rotate Array '''
# l=[1,2,3,4,5]
# fi = l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)

'''optimized aprroach right '''
# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4,5,6]
# k=3
# k=k%len(l)
# reverse(l,0,len(l)-1)
# reverse(l,0,k-1)
# reverse(l,3,len(l)-1)
# print(l)

'''optimized aprroach left '''
# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4,5,6,7]
# k=2
# k=k%len(l)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# reverse(l,0,len(l)-1)

''' right rotate only no k '''
# def rev(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4]
# rev(l,0,len(l)-1)
# rev(l,1,len(l)-1)
# print(l)


'''left rotate only no k'''
# def rev(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4]
# rev(l,0,len(l)-1)
# rev(l,0,len(l)-2)
# print(l)
# --------------------------------------------------------------------------------------------------
'''•	Move Zeroes '''
# l=[1,0,2,0,3,0,4]
# left = 0
# for right in range(len(l)):
#     if l[right]!=0:
#         if l[left]!=l[right:]:
#             l[left],l[right]=l[right],l[left]
#         left+=1
# print(l)
# ----------------------------------------------------------------------------------------------------
'''•	Merge Two Sorted Arrays '''
# l1=[1,3,5]
# l2=[2,4,6]
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
# --------------------------------------------------------------------------------------------------
'''pair sum/Two sum'''
# l=[4,7,2,3]
# target = 10
# d={}
# for i in l:
#     need = target-i
#     if need in d:
#         print((need,i))
#     d[i]=1

''' two sum but in output indices'''
# l = [4, 7, 2, 3]
# target = 10
# d = {}
# for index, i in enumerate(l):
#     need = target - i
#     if need in d:
#         print((d[need], index))
#     d[i] = index

'''for index, value in enumerate(l):
ok so enumerate gives indices with their respected values for example it will create 
a pair like this 
(0,4),(1,7),(2,2),(3,3)'''
# ----------------------------------------------------------------------------------------------------

'''•	Majority Element '''
# l=[3, 3, 4, 2, 3, 3, 3]
# n = len(l)/2
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>n:
#         print("The Majority Element is",i)

''' booyer morre  algorithm '''
# l=[3, 3, 4, 2, 3, 3, 3]
# candidate = None
# count = 0
# for i in l:
#     if count == 0:
#         candidate = i
#     if i==candidate:
#         count+=1
#     else:
#         count-=1
# print("The Majority Element is",candidate)
# ---------------------------------------------------------------------------------------------------
'''•	Leaders in Array '''
# l = [16,17,4,5,2]
# for i in range(len(l)):
#     leader = True
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             leader = False
#     if leader:
#         print(l[i])

'''optimized approach'''
# l = [16,17,4,5,2]
# max_right = l[-1]
# ans=[l[-1]]
# for i in range(len(l)-2,-1,-1):
#     if l[i]>max_right:
#         ans.append(l[i])
#         max_right=l[i]
# ans.reverse()
# print(ans)
# for i in range(len(l)-2,-1,-1):
# Matlab
# Second last element se start.
# Example
#    16 17 4 3 5 2
#                ↑
# Already handled
# ------------------------------------------------------------------------------------------------------------
'''•	Equilibrium Index '''
# l=[3,1,5,2,2]
# for i in range(len(l)):
#     left_sum=0
#     right_sum=0
#     for j in range(0,i):
#         left_sum+=l[j]
#     for k in range(i+1,len(l)):
#         right_sum+=l[k]
#     if left_sum==right_sum:
#         print("The Equilibrium Index is",i)

''' optimized approach'''
# l=[3,1,5,2,2]
# total_sum=sum(l)
# left_sum=0
# for i in range(len(l)):
#     right_sum = total_sum-left_sum-l[i]
#     if left_sum==right_sum:
#         print("The Equilibrium Index is",i)
#     left_sum+=l[i]
# --------------------------------------------------------------------------------------------------
'''•	Stock Buy and Sell '''
'''brute force '''
# l=[7,1,5,3,6,4]
# max_profit = 0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         profit = j-i
#         if profit>max_profit:
#             max_profit=profit
# print(max_profit)

'''optimized version'''
# prices = [7,1,5,3,6,4]
# min_price = prices[0]
# max_profit = 0
# for i in prices:
#     if i<min_price:
#         min_price=i
#     profit = i-min_price
#     if profit>max_profit:
#         max_profit=profit
# print(max_profit)
# ----------------------------------------------------------------------------------------------------
'''•	Kadane's Algorithm '''
'''Maximum  contignuos Subarray Sum
Brute force approach '''
# l=[-2,1,-3,4,-1,2,1,-5,4]
# max_sum=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         total_sum=0
#         for k in sub:
#             total_sum+=k
#         if total_sum>max_sum:
#             max_sum=total_sum
#             ans=sub
# print(max_sum)
# print(ans)

'''optimized approach'''
# l=[-2,1,-3,4,-1,2,1,-5,4]
# current_sum=0
# max_sum=l[0]
# for i in l:
#     current_sum+=i
#     if current_sum>max_sum:
#         max_sum=current_sum
#     else:
#         if current_sum<0:
#             current_sum=0
# print(max_sum)

'''==================================== HASHMAP,DICTIONARY ============================================ '''
'''•	Frequency Count '''
# l=[1,2,2,3,3,3,3,4,4,4,5,5,5,5,5]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Character Frequency '''
# ch = 'madam'
# d={}
# for i in ch:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Word Frequency '''
# word = "if i will meet you then i will teach you python"
# l=word.split()
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Maximum Frequency '''
# l=[1,2,2,2,2,23,3,3,4,4,4]
# d={}
# max_freq=0
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>max_freq:
#         max_freq=d[i]
#         ans=i
# print("the maximum frequency is",max_freq,"and the value is",ans)

'''•	First Non-Repeating '''
# l=[1,1,2,3,4,4]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]==1:
#         print("the first non repeating element is ",i)
#         break

'''•   Last Non-Repeating'''
# l=[1,1,2,3,4,4]
# d={}
# for i in range(len(l)-1,-1,-1):
#     if l[i] in d:
#         d[l[i]] = d[l[i]]+1
#     else:
#         d[l[i]] = 1
# for i in d:
#     if d[i]==1:
#         print(i)
#         break

'''•	Count Duplicates '''
# l=[1,2,2,3,3,4,4,4,5,5,6,6,6]
# d={}
# count=0
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>=2:
#         count+=1
# print(count)

'''•	Remove Duplicates '''
# l=[1,2,2,3,4,4,5,5,5,6]
# d={}
# ans=[]
# for i in l:
#     if i not in d:
#         ans.append(i)
#         d[i]=1
# print(ans)


'''•	Contains Duplicate '''
# l=[1,2,2,3,4,4,5,5,5,6]
# d={}
# for i in l:
#     if i in d:
#         print(True)
#         break
#     else:
#         d[i]=1

'''•	Missing Number '''
# l=[3, 0, 1]
# n=len(l)
# excepted_sum=n*(n+1)//2
# orginal_sum=0
# for i in l:
#     orginal_sum+=i
# missing_no = excepted_sum-orginal_sum
# print(missing_no)

'''•	Group By Frequency '''
# l=[1,22,333,4,55,666]
# d={}
# for i in l:
#     count=0
#     x=i
#     while x>0:
#         digit=x%10
#         count+=1
#         x=x//10 
#     if count not in d:
#         d[count]=[]
#     d[count].append(i)
# print(d)

'''group by sum'''
# l=[1, 22, 333, 4, 55, 666]
# d={}
# for i in l :
#     x=i
#     digit_sum=0
#     while x>0:
#         digit=x%10
#         digit_sum+=digit
#         x=x//10
#     if digit_sum not in d:
#         d[digit_sum]=[]
#     d[digit_sum].append(i)
# print(d)


'''•	Check Anagram '''
# s1 = "listen"
# s2 = "silent"
# d1={}
# d2={}
# if len(s1)!=len(s2):
#     print(False)
# else:
#     for i in s1:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
#     for j in s2:
#         if j in d2:
#             d2[j]=d2[j]+1
#         else:
#             d2[j]=1
#     if d1==d2:
#         print(True,"Anagram")
#     else:
#         print(False,"Not Anagram")

'''•	Group Anagrams '''
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# d={}
# for i in words:
#     sorted_words = "".join(sorted(i))
#     if sorted_words not in d:
#         d[sorted_words]=[]
#     d[sorted_words].append(i)
# print(list(d.values()))

'''•	Intersection of Arrays '''
# l1 = [4, 9, 5]
# l2 = [9, 4, 9, 8, 4]
# d={}
# ans=[]
# for i in l1:
#     d[i]=1
# for j in l2:
#     if j in d and j not in ans:
#         ans.append(j)
# print(ans)


    







       






        

