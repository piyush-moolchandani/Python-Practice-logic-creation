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
    
