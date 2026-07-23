'''•	Reverse Array '''
# l=[1,2,3,4,5]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

# optimized approach
# l=[1,2,3,4,5]
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# print(l)
'''Real answer ye hai:
Reverse Array me hum actually kar kya rahe hain?
Hum opposite positions wale elements ko swap karte hain. 
Har swap ke baad un dono elements ki final position fix ho jaati hai. 
Isliye unhe dobara touch nahi karte. Phir pointers ko ek step andar le aate hain. 
Jab pointers mil jaate hain ya cross kar jaate hain, poora array reverse ho chuka hota hai.

Why do we use two pointers?
Answer:
Kyunki ek pointer first element ko represent karta hai aur doosra last element ko.
Reverse me opposite elements exchange hote hain, isliye dono ends se start karke 
beech ki taraf move karna sabse efficient approach hai.
time compexity:o(n)
space o(1)'''




'''•	Rotate Array right '''
# def revesre(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4,5,6,7]
# k=3
# k=k%len(l)
# revesre(l,0,len(l)-1)
# revesre(l,0,k-1)
# revesre(l,3,len(l)-1)
# print(l)

'''•	Rotate Array left '''
# def reverse(l,left,right):
#     while left<right:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# l=[1,2,3,4,5,6,7]
# k=3
# k=k%len(l)
# reverse(l,0,k-1)
# reverse(l,k,len(l)-1)
# reverse(l,0,len(l)-1)
# print(l)

'''•	Move Zeroes '''
# l=[1,0,2,0,3,0]
# l2=[]
# for i in l:
#     if i!=0:
#         l2.append(i)
# l3=[]
# for i in l:
#     if i==0:
#         l3.append(i)
# print(l2+l3)

# optimized version
# l=[1,0,2,0,3,0]
# i=0
# for j in range(len(l)):
#     if l[j]!=0:
#         if i!=j:
#             l[i],l[j]=l[j],l[i]
#         i+=1
# print(l)

'''•	Merge Two Sorted Arrays '''
# l1=[1,3,5]
# l2=[2,4,6]
# i=0
# j=0
# ans=[]
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


'''Pair Sum '''
# l = [2,7,11,15]
# target = 9
# d={}
# for index,i in enumerate(l):
#     need=target-i
#     if need in d:
#         print((need,i))
        # print(d[need],index)       --->indices
#     d[i]=index


'''•	Majority Element '''
# l=[2,2,1,1,1,2,2]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# majority = len(l)/2
# for key, value in d.items():
#     if value > majority:
#         print(key)

'''•	Leaders in Array '''
# l=[16,17,4,3,5,2]
# for i in range(len(l)):
#     leader=True
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             leader=False
#     if leader:
#         print(l[i])

'''optimized approach'''
# l=[16,17,4,3,5,2]
# max_right = l[-1]
# ans=[l[-1]]
# for i in range(len(l)-2,-1,-1):
#     if l[i]>max_right:
#         ans.append(l[i])
#         max_right=l[i]
# final_ans = ans[::-1]
# print(final_ans)

'''•	Equilibrium Index '''
# l=[1,3,5,2,2]
# for i in range(len(l)):
#     left_sum=0
#     right_sum=0
#     for j in range(0,i):
#         left_sum+=l[j]
#     for k in range(i+1,len(l)):
#         right_sum+=l[k]
#     if left_sum==right_sum:
#         print("equilibrium index is",i)

'''optimized approach'''
# l=[1,3,5,2,2]
# total_sum = sum(l)
# left_sum=0
# for i in range(len(l)):
#     right_sum = total_sum-left_sum-l[i]
#     if left_sum==right_sum:
#         print("equilibrium index is",i)
#     else:
#         left_sum+=l[i]


'''•	Stock Buy and Sell '''
# prices=[7,1,5,3,6,4]
# min_price = prices[0]
# max_profit = 0 
# for i in prices:
#     if i<min_price:
#         min_price=i
#     else:
#         profit = i-min_price
#         if profit>max_profit:
#             max_profit=profit
# print(max_profit)
    







