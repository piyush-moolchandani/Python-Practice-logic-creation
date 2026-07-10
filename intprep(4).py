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
# for i in range(len(l)):
#     for j in range(i+1,len(l)):        ---> tomorrow
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)



