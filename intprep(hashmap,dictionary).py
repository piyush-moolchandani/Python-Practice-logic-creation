'''•	Frequency Count '''
# l=[1,1,2,2,2,2,4,4,4,5,5,6,6]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Character Frequency '''
# word = "madam"
# d={}
# for i in word:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Word Frequency '''
# word = "hello hello how are you "
# l=word.split()
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Maximum Frequency '''
# l=[1,1,2,2,2,2,4,4,4,5,5,6,6]
# d={}
# max_freq=0
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>max_freq:
#         max_freq=d[i]
#         element=i
# print("the maximum frequency is",max_freq, "an the element is",element)

# '''•	First Non-Repeating '''
# l=[1,1,2,3,4,4]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]==1:
#         print(i)
#         break

# '''•	First Repeating '''
# l=[1,2,2,3,3,3]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>1:
#         print(i)
#         break

'''•	Count Duplicates '''
# l = [1, 1, 2, 3, 3, 3, 4, 5, 5]
# d = {}
# count = 0
# for i in l:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# for i in d:
#     if d[i] > 1:
#         count+=1
# print(count)

'''•	Remove Duplicates '''
# l=[1, 2, 2, 3, 1, 4, 3, 5]
# d={}
# ans=[]
# for i in l:
#     if i not in d:
#         ans.append(i)
#         d[i]=1
# print(ans)

'''•	Contains Duplicate '''
# l = [1, 2, 3, 4, 2]
# d = {}
# for i in l:
#     if i in d:
#         print(True)
#         break
#     else:
#         d[i]=1
    

'''•	Missing Number '''
# l=[3,0,1]
# n=len(l)
# expected_sum=n*(n+1)//2
# actual_sum=0
# for i in l:
#     actual_sum+=i
# missing_no = expected_sum-actual_sum
# print(missing_no)

'''•	Duplicate Number '''
# l = [1, 3, 4, 2, 2]
# d={}
# for i in l:
#     if i in d:
#         print(i)
#         break
#     else:
#         d[i]=1

'''•	Group By Frequency '''
# l=[1,1,2,2,2,3,3,4]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# group={}
# for element,freq in d.items():
#     if freq not in group:
#         group[freq]=[]
#     group[freq].append(element)
# print(group)
 

'''•	Check Anagram '''
# s1="silent"
# s2="listen"
# d1={}
# d2={}
# if len(s1)!=len(s2):
#     print(False)
# else:
#     for i in s1:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
#     for j in s2:
#         if j in d2:
#             d2[j]=d2[j]+1
#         else:
#             d2[j]=1
#     if d1==d2:
#         print(True)
#     else:
#         print(False)

'''•	Group Anagrams '''
# l = ["eat", "tea", "tan", "ate", "nat", "bat"]
# d={}
# for i in l:
#     key = "".join(sorted(i))
#     if key not in d:
#         d[key]=[]
#     d[key].append(i)
# print(d)

'''•	Intersection of Arrays '''
# l1 = [4, 9, 5]
# l2 = [9, 4, 9, 8, 4]
# d={}
# ans=[]
# for i in l1:
#     d[i]=1
# for j in l2:
#     if j in d and j not in ans:
#         ans.append(j)
# print(ans)

