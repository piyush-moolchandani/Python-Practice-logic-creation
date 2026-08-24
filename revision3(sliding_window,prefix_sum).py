'''•	Maximum Sum Subarray of Size K '''
# l = [2,1,5,1,3,2]
# k = 3
# window_sum=0
# max_sum=0
# for i in range(0,k):
#     window_sum+=l[i]
# max_sum=window_sum
# for j in range(k,len(l)):
#     window_sum=window_sum-l[j-k]+l[j]
#     if window_sum>max_sum:
#         max_sum=window_sum
#         start=j-k+1
# print(max_sum)
# print(l[start:start+k])


'''•	Minimum Sum Subarray of Size K '''
# l = [2,1,5,1,3,2]
# k = 4
# window_sum=0
# min_sum=l[0]
# for i in range(0,k):
#     window_sum+=l[i]
# min_sum=window_sum
# start=0
# for j in range(k,len(l)):
#     window_sum=window_sum-l[j-k]+l[j]
#     if window_sum<min_sum:
#         min_sum=window_sum
#         start=j-k+1
# print(l[start:start+k])
# print(min_sum)


'''•	First Negative in Every Window '''
'''Brute force approach'''
# l = [12, -1, -7, 8, -15, 30, 16, 28]
# k=3
# ans=[]
# for i in range(len(l)-k+1):
#         sub=l[i:i+k]
#         for j in sub:
#             if j<0:
#                 ans.append(j)
#                 break
#         else:
#             ans.append(0)
# print(ans)

'''optimized approach '''
# from collections import deque
# l = [12, -1, -7, 8, -15, 30, 16, 28]
# k=3
# dq=deque()
# ans=[]
# for i in range(k):
#     if l[i]<0:
#         dq.append(i)
# ans.append(l[dq[0]] if dq else 0)
# for j in range(k,len(l)):
#     if dq and j-k==dq[0]:
#         dq.popleft()
#     if l[j]<0:
#         dq.append(j)
#     ans.append(l[dq[0]] if dq else 0)
# print(ans)


'''rev2'''
# from collections import deque
# l = [12, -1, -7, 8, -15, 30, 16, 28]
# k=3
# dq=deque()
# ans=[]
# for i in range(k):
#     if l[i]<0:
#         dq.append(i)
# if dq:
#     ans.append(l[dq[0]])
# else:
#     ans.append(0)
# for j in range(k,len(l)):
#     if dq and j-k==dq[0]:
#         dq.popleft()
#     if l[j]<0:
#         dq.append(j)
#     if dq:
#         ans.append(l[dq[0]])
#     else:
#         ans.append(0)
# print(ans)


'''max wnidow sum rev2 '''
# l = [2,1,5,1,3,2]
# k = 3
# max_sum=l[0]
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

