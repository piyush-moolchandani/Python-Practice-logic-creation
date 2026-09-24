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
# for i in range(len(l)):
#     left_sum = 0
#     right_sum = 0
#     for j in range(0,i):
#         left_sum+=l[j]
#     for k in range(i+1,len(l)):
#         right_sum+=l[k]
#     if left_sum==right_sum:
#         print(i)

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

