'''•	Reverse Array '''
# l = [1,2,3,4,5,6,7]
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right] = l[right],l[left]
#     left+=1
#     right-=1
# print(l)

'''•	Rotate Array 
•	Rotate Array by K 
Right
'''

# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right] = l[right],l[left]
#         left+=1
#         right-=1
# l = [1,2,3,4,5]
# k = 3
# k = k%len(l)
# reverse(l,0,len(l)-1)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# print(l)

'''•	Rotate Array by K 
left'''
# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l = [1,2,3,4,5]
# k = 3
# k = k%len(l)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# reverse(l,0,len(l)-1)
# print(l)

'''•	Move Zeroes '''
# l=[1,0,2,0,3,0]
# left = 0
# for right in range(len(l)):
#     if l[right]!=0:
#         if left!=right:
#             l[left],l[right]=l[right],l[left]
#         left+=1
# print(l)


'''•	Merge Two Sorted Arrays '''
# l1 = [1,3,5]
# l2 = [2,4,6]
# i = 0
# j = 0
# ans = []
# while i<len(l1) and j<len(l2):
#     if l1[i]<l2[j]:
#         ans.append(l1[i])
#         i+=1
#     else:
#         ans.append(l2[j])
#         j+=1
# while i<len(l1):
#     ans.append(l1[i])
#     i+=1
# while j<len(l2):
#     ans.append(l2[j])
#     j+=1
# print(ans)

'''•	Pair Sum 
•	Two Sum 
'''
# l = [4,7,5,6,9]
# target = 11
# d = {}
# for i in l:
#     need = target - i
#     if need in d:
#         print((need,i))
#     d[i] = 1        

'''•	Majority Element '''
# l=[2,2,1,1,1,2,2]
# maj_element = (len(l))/2
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>maj_element:
#         print(i)

'''•	Leaders in Array '''
# l = [16,17,4,3,5,2]
# max_right = l[-1]
# ans = [l[-1]]
# for i in range(len(l)-2,-1,-1):
#     if l[i]>max_right:
#         max_right=l[i]
#         ans.append(l[i])
# ans = ans[::-1]
# print(ans)


'''•	Equilibrium Index '''
# l = [2,2,67,1,3]
# total_sum = sum(l)
# left_sum = 0
# for i in range(len(l)):
#     right_sum = total_sum-left_sum-l[i]
#     if left_sum == right_sum:
#         print(i)
#     left_sum+=l[i]


'''•	Stock Buy and Sell '''
# prices = [7,1,5,3,6,4]
# min_prices = prices[0]
# max_profit = 0
# for i in prices:
#     if i<min_prices:
#         min_prices=i
#     else:
#         profit = i-min_prices
#         if profit>max_profit:
#             max_profit=profit
# print(max_profit)


'''•	Kadane's Algorithm
Ek integer array diya hai. Humein us contiguous subarray ka maximum possible sum find karna hai'''
''' kadane algo'''
# l = [-2,1,-3,4,-1,2,1,-5,4]
# current_sum = 0
# max_sum = 0
# for i in l:
#     current_sum+=i
#     if current_sum>max_sum:
#         max_sum=current_sum
#     else:
#         if current_sum<0:
#             current_sum = 0
# print(max_sum)

# =================================================================================================

'''HashMap / Dictionary '''
'''•	Frequency Count '''
# l = [1,1,2,2,3,3,34,4,5,4,5,3,4,45,5]
# d = {}
# for i in l:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# print(d)

'''•	Character Frequency '''
# s = 'madam'
# d = {}
# for i in s:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# print(d)

'''•	Word Frequency '''
# s = " hi my name is python and my age is 22"
# l = s.split()
# d = {}
# for i in l:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# print(d)

'''•	Maximum Frequency '''
# l = [1,2,2,2,3,3,3,3,3,3,4,4,6]
# d = {}
# max_freq = 0
# for i in l:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# for i in d:
#     if d[i]>max_freq:
#         max_freq=d[i]
#         ans = i
# print(max_freq)
# print(ans)

'''•	First Non-Repeating '''
# l = [1,1,2,3,3,4,5,5]
# d  = {}
# for i in l:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# for i in d:
#     if d[i] == 1:
#         print(i)
#         break

'''•	Remove Duplicates '''
# l = [1,1,2,3,3,3,4,5,5,5,5,5]
# d = {}
# l2 = []
# for i in l:
#     if i not in d:
#         l2.append(i)
#         d[i] = 1
# print(l2)

'''•	•	Group Anagrams  '''
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# d = {}
# for i in words:
#     sorted_words = "".join(sorted(i))
#     if sorted_words not in d:
#         d[sorted_words] = []
#     d[sorted_words].append(i)
# print(d)

'''•	Group By Frequency '''
# l = [1,1,2,2,2,3,3,4]
# d = {}
# d2= {}
# for i in l:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# for key,value in d.items():
#     if value not in d2:
#         d2[value] = []
#     d2[value].append(key)
# print(d2)

'''•	Check Anagram '''
# s1 = "listen"
# s2 = "silent"
# d1 = {}
# d2 = {}
# if len(s1)!=len(s2):
#     print(False)
# else:
#     for i in s1:
#         if i in d1:
#             d1[i] = d1[i]+1
#         else:
#             d1[i] = 1
#     for i in s2:
#         if i in d2:
#             d2[i] = d2[i]+1
#         else:
#             d2[i] = 1
#     if d1==d2:
#         print('anagram')
#     else:
#         print('not anagram')


'''•	Intersection of Arrays '''
# l1 = [4, 9, 5]
# l2 = [9, 4, 9, 8, 4]
# d = {}
# ans = []
# for i in l1:
#     d[i]=1
# for j in l2:
#     if j in d and j not in ans:
#         ans.append(j)
# print(ans)

'''•	Reverse String '''
# s = "RestApi"
# l = list(s)
# left = 0
# right = len(s)-1
# while left<right:
#     l[left],l[right] = l[right],l[left]
#     left+=1
#     right-=1
# s = "".join(l)
# print(s)

'''•	Reverse Words '''
# s = "ForeignKey, ManyToMany, select_related, prefetch_related, aggregation"
# l = s.split()
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right] = l[right],l[left]
#     left+=1
#     right-=1
# s = " ".join(l)
# print(s)

'''•	Palindrome '''
# s = 'madam'
# left = 0
# right = len(s)-1
# is_palindrome = True
# while left<right:
#     if s[left]!=s[right]:
#         is_palindrome = False
#         break
#     left+=1
#     right-=1
# if is_palindrome:
#     print('palindrome')
# else:
#     print('Not palindrome')


