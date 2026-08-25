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


'''•	Maximum Consecutive Ones '''
# l = [1, 1, 0, 1, 1, 1]
# count=0
# max_count=0
# for i in l:
#     if i==1:
#         count+=1
#         if count>max_count:
#             max_count=count
#     else:
#         count=0
# print(max_count)

'''•	•	Maximum Consecutive Ones III '''
# l = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# k = 2
# left=0
# zero_count=0
# max_len=0
# for right in range(len(l)):
#     if l[right]==0:
#         zero_count+=1
#     while zero_count>k:
#         if l[left]==0:
#             zero_count-=1
#         left+=1
#     curren_len=right-left+1
#     if curren_len>max_len:
#         max_len=curren_len
# print(max_len)


'''•	Longest Substring Without Repeating Characters '''

# s = "abcabcbb"
# left=0
# max_len=0
# seen=set()
# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left+=1
#     seen.add(s[right])
#     curren_len=right-left+1
#     if curren_len>max_len:
#         max_len=curren_len
# print(max_len)


'''•	Fruits Into Basket '''
# fruits = [1, 2, 1, 2, 3]
# left=0
# max_len=0
# d={}
# start=0
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
#     curren_len=right-left+1
#     if curren_len>max_len:
#         max_len=curren_len
#         start=left
# print(max_len)
# print(fruits[start:start+max_len])

'''max con rev2'''
l = [1, 1, 0, 1, 1, 1]
count=0
max_len=0
for i in l:
    if i==1:
        count+=1
        if count>max_len:
            max_len=count
    else:
        count=0
print(max_len)


'''max con 3 rev2'''
l = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
left=0
max_len=0
zero_count=0
for right in range(len(l)):
    if l[right]==0:
        zero_count+=1
    while zero_count>k:
        if l[left]==0:
            zero_count-=1
        left+=1
    curren_len=right-left+1
    if curren_len>max_len:
        max_len=curren_len
print(max_len)


'''long sub unique rev2'''
s = "abcabcbb"
left=0
seen=set()
max_len=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[right])
    curren_len=right-left+1
    if curren_len>max_len:
        max_len=curren_len
print(max_len)


'''fruits into basket rev2'''
fruits = [1, 2, 1, 2, 3]
left=0
max_len=0
d={}
start=0
for right in range(len(fruits)):
    if fruits[right] in d:
        d[fruits[right]]=d[fruits[right]]+1
    else:
        d[fruits[right]]=1
    while len(d)>2:
        d[fruits[left]]-=1
        if d[fruits[left]]==0:
            del d[fruits[left]]
        left+=1
    curren_len=right-left+1
    if curren_len>max_len:
        max_len=curren_len
        start=left
print(max_len)
print(fruits[start:start+max_len])
    




