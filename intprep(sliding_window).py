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

   


        
