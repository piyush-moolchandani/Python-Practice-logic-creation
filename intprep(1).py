# Radha
'''1.	Reverse a list '''
'''Time Complexity?
Loop runs n times.Each append() is O(1).
Total:O(n)
Space Complexity?You created a new list l2.
Extra space:O(n)'''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)-1,-1,-1):                               
#     l2.append(l[i])
# print(l2)

'''2.	Rotate list left by 1 '''
'''Why save first element?Without:fi=l[0]
After first operation:l[0]=l[1]the value 1 is permanently lost.
Time ComplexityLoop runs:n-1 times So:O(n)
Space ComplexityOnly one extra variable:fi So:O(1)'''
# l=[1,2,3,4,5]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)
'''optimized'''
# l=[1,2,3,4,5]
# l=l[1:]+l[:1]
# print(l)

'''3.	Rotate list right by 1 '''
# l=[1,2,3,4,5]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)
'''optimized'''
# l=[1,2,3,4,5]
# l=l[-1:]+l[:-1]
# print(l)

'''4.	Rotate list left by k positions '''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)
'''optimized solution'''
# l=[1,2,3,4,5]
# k=2
# k=k%len(l)
# l=l[k:]+l[:k]
# print(l)

'''5.	Rotate list right by k positions '''
'''optimized solution'''
# l=[1,2,3,4,5]
# k=2
# k=k%len(l)
# l=l[-k:]+l[:-k]
# print(l)
