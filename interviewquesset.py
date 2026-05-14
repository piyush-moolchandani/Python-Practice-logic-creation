'''41.	Reverse a list '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)
    
'''42.	Rotate list left by 1 '''
# l=[1,2,3,4]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)

'''43.	Rotate list right by 1 '''
# l=[1,2,3,4]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)

'''44.	Rotate list by k positions '''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)

'''Rotate list right by k8 positions'''
# l=[1,2,3,4,5]
# k=8
# k=k%len(l)
# for i in range(k):
#     lv=l[-1]
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=lv
# print(l)

'''45.	Move all zeros to end '''
# l=[1,0,2,0,3,0,4,0,5,0]
# pos=0
# for i in range(len(l)):
#     if l[i]!=0:
#         l[pos],l[i]=l[i],l[pos]
#         pos+=1
# print(l)


'''47.	Separate even and odd numbers '''
# l=[1,2,3,4,5,6,7,8]
# pos=0
# for i in range (len(l)):
#     if l[i]%2==0:
#         l[pos],l[i]=l[i],l[pos]
#         pos+=1
# print(l)



