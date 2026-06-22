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

'''49.	Sum of digits grouping '''
# num = 123456
# l=str(num)
# for i in range(0,len(l),2):
#     if i+1<len(l):
#         sum=int(l[i])+int(l[i+1])
#     else:
#         sum=int(l[i])
#     print(sum)
'''"I convert the number into a string, traverse digits in groups of two, 
sum each pair, and for odd-length numbers I treat the last remaining digit as 
a separate group to avoid index errors."'''

'''Sum of digits grouping odd and even digits'''
# num = 123456
# l=str(num)
# even_sum=0
# odd_sum=0
# for i in l:
#     if int(i)%2==0:
#         even_sum+=int(i)
#     else:
#         odd_sum+=int(i)
# print(even_sum)
# print(odd_sum)

'''50.	Binary 1-count prime replacement Replace by count of 1s'''
# l = [5, 6, 8] 
# l2=[]
# for i in l:
#     ch=bin(i)[2:]
#     bin_count=0
#     for j in ch:
#         if j=="1":
#             bin_count+=1
#     prime=0
#     for k in range(1,bin_count+1):
#         if bin_count%k==0:
#             prime+=1
#     if prime==2:
#         i=bin_count
#     l2.append(i)
# print(l2)



        



    
        





        