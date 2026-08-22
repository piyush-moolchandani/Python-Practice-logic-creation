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
