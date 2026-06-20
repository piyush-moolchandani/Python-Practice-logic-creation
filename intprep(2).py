'''41.	Reverse string '''
# l='python'
# print(l[::-1])

# l='python'
# new=""
# for i in range(len(l)-1,-1,-1):
#     new=new+l[i]
# print(new)

'''42.	Check palindrome string '''
# l='madam'
# x=l
# if l[::-1]==x:
#     print('pallindrome string')

'''43.	Character frequency count '''
'''44.	Find first repeating character '''
# l='abccddee'
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count>1:
#         print(i)
#         break

'''45.	Find first non-repeating character '''
# l='aabbcde'
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq==1:
#         print(i)
#         break

'''47.	Reverse elements at prime indexes '''
# x="programming"
# new=""
# for i in range(len(x)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         new=new+x[i]
# rev=new[::-1]
# x=list(x)
# pos=0
# for i in range(len(x)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         x[i]=rev[pos]
#         pos+=1
# print("".join(x))

'''48.	Arrange digits inside number (even digits first) '''
# x=123456
# l=str(x)
# even=""
# odd=""
# for i in l:
#     if int(i)%2==0:
#         even+=i
#     else:
#         odd+=i
# print(even+odd)






        