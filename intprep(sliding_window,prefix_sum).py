'''•	Maximum Sum Subarray of Size K '''
# l = [2, 1, 5, 1, 3, 2]
# k = 3
# window_sum=0
# for i in range(k):
#     window_sum+=l[i]
# max_sum=window_sum
# for j in range(k,len(l)):
#     window_sum=window_sum-l[j-k]+l[j]
#     if window_sum>max_sum:
#         max_sum=window_sum
#         start = j-k+1
# print(l[start:start+k])
# print(max_sum)

'''•	Minimum Sum Subarray of Size K '''
# l = [2, 1, 5, 1, 3, 2]
# k = 3
# window_sum=0
# for i in range(k):
#     window_sum+=l[i]
# min_sum=window_sum
# start=0
# for j in range(k,len(l)):
#     window_sum=window_sum-l[j-k]+l[j]
#     if window_sum<min_sum:
#         min_sum=window_sum
#         start=j-k+1
# print(min_sum)
# print(l[start:start+k])

'''•	First Negative in Every Window '''
# from collections import deque
# l = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 3
# dq=deque()
# ans=[]
# for i in range(k):
#     if l[i]<0:
#         dq.append(l[i])
# if dq:
#     ans.append(dq[0])
# else:
#     ans.append(0)
# for j in range(k,len(l)):
#     if dq and l[j-k] == dq[0]:
#         dq.popleft()
#     if l[j]<0:
#             dq.append(l[j])
#     if dq:
#         ans.append(dq[0])
#     else:
#         ans.append(0)
# print(ans)


'''•	Longest Substring Without Repeating Characters '''
# n = "abcabcbb"
# left = 0
# max_len = 0
# seen=set()
# for right in range(len(n)):
#    while n[right] in seen:
#       seen.remove(n[left])
#       left+=1
#    seen.add(n[right])
#    max_len = max(max_len, right - left + 1)
# print(max_len)


'''•	Maximum Consecutive Ones '''
# l = [1, 1, 0, 1, 1, 1]
# count = 0
# max_count=0
# for i in l:
#     if i==1:
#         count+=1
#         if count>max_count:
#             max_count=count
#     else:
#         count=0
# print(max_count)

'''Maximum Consecutive Ones III'''
# l = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# k = 2
# left = 0
# zero_count = 0
# max_len = 0
# for right in range(len(l)):
#     if l[right]==0:
#         zero_count+=1
#     while zero_count>k:
#         if l[left]==0:
#             zero_count-=1
#         left+=1
#     max_len = max(max_len, right - left + 1)
# print(max_len)


'''•	Fruits Into Basket '''
# fruits = [1, 2, 1, 2, 3]
# left = 0 
# d={}
# max_len=0
# for right in range(len(fruits)):
#     if fruits[right] in d:
#         d[fruits[right]] = d[fruits[right]] + 1
#     else:
#         d[fruits[right]] = 1
#     while len(d)>2:
#         d[fruits[left]]-=1
#         if d[fruits[left]]==0:
#             del d[fruits[left]]
#         left+=1
#     current_len = right - left + 1
#     if current_len > max_len:
#         max_len = current_len
#         start = left
# print(fruits[start:start+max_len])
# print(max_len)

''' practice-2'''
# l = [1, 2, 1, 2, 3]
# i = 0 
# d={}
# max_len=0
# for j in range(len(l)):
#     if l[j] in d:
#         d[l[j]] = d[l[j]]+1
#     else:
#         d[l[j]] = 1
#     while len(d)>2:
#         d[l[i]]-=1
#         if d[l[i]] == 0:
#             del d[l[i]]
#         i+=1
#     current = j-i+1
#     if current>max_len:
#         max_len=current
#         start = i
# print(max_len)
# print(l[start:start+max_len])

'''•	Prefix Sum '''
# l = [3, 2, 5, 1, 6]
# l2=[]
# total=0
# left = 2
# right = 4
# for i in l:
#     total+=i
#     l2.append(total)
# if left==0:
#     range_sum = l2[right]
# else:
#     range_sum = l2[right] - l2[left-1]
# print(range_sum)

'''•	Running Sum '''
# l = [5, 1, 2, 7, 3]   
# l2=[]
# total=0
# for i in l:
#     total+=i
#     l2.append(total)
# print(l2)

'''•	Running Sum '''
# l=[1,3,5,2,2]
# total_sum = sum(l)
# left_sum=0
# for i in range(len(l)):
#     right_sum = total_sum-left_sum-l[i]
#     if left_sum==right_sum:
#         print("equilibrium index is",i)
#     else:
#         left_sum+=l[i]

'''•	Subarray Sum = K '''
# l = [1, 1, 1]
# k = 2
# prefix_sum = 0
# count = 0
# d = {0: 1}
# for i in l:
#     prefix_sum+=i
#     needed = prefix_sum-k
#     if needed in d:
#         count+=d[needed]
#     if prefix_sum in d:
#         d[prefix_sum]+=1
#     else:
#         d[prefix_sum]=1
# print(count)




