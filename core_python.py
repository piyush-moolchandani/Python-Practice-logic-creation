'''Reverse a string without using [::-1]'''
# s = 'python'
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# print(rev)

'''Check if a string is palindrome'''
# s = "madam"
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# if rev==s:
#     print('palindrome')
# else:
#     print(' not palindorem')

'''Count vowels and consonants in a string'''
# s = 'piyush'
# vowel_count=0
# consonants_count=0
# for i in s:
#     if i in 'aeiou':
#         vowel_count+=1
#     else:
#         consonants_count+=1
# print({'vowel_count':vowel_count,'consonants_count':consonants_count})

'''Count frequency of each character in a string'''
# s = 'banana'
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''Remove duplicate characters from a string while preserving order'''
# s = "programming" 
# d={}
# ans=""
# for i in s:
#     if i not in d:
#         ans+=i
#         d[i]=1
# print(ans)

'''Find the first non-repeating character'''
# s='abaccd'
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]==1:
#         print(i)
#         break

'''Find the first repeating character'''
# s='abaccd'
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>1:
#         print(i)
#         break

'''Count words in a sentence'''
# s = "I am learning Django"
# l = s.split()
# count = 0 
# for i in l:
#     count+=1
# print(count)

'''Find the longest word in a sentence'''
# s = "I am learning Django"
# l=s.split()
# max_count=0
# for i in l:
#     if len(i)>max_count:
#         max_count=len(i)
#         ans=i
# print(ans)

'''Reverse every word of a sentence'''
# s = "I am learning Django"
# l = s.split()
# rev = ""
# for i in l:
#     for j in range(len(i)-1,-1,-1):
#         rev = rev + i[j]
#     rev = rev+" "
# print(rev)

# ====================================== LIST =====================================================

'''Find duplicates in a list'''
# l=[1,2,2,3,4,4]
# d = {}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# for i in d:
#     if d[i]>1:
#         print(i)

'''Remove duplicates from a list without using set()'''
# l=[1,2,2,3,4,4]
# d={}
# ans = []
# for i in l:
#     if i not in d:
#         ans.append(i)
#         d[i]=1
# print(ans)
 
'''13. Remove duplicates while preserving order'''
# l=[1,2,2,3,4,4]
# d={}
# ans = []
# for i in l:
#     if i  not in d:
#         ans.append(i)
#         d[i]=1
# print(ans)

'''14. Find common elements between two lists'''
# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 4, 5, 6, 7]
# for i in l1:
#     if i in l2:
#         print(f"the common elements are {i}")

'''Find elements present in first list but not second'''
# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 4, 5, 6, 7]
# ans=[]
# for i in l1:
#     if i not in l2:
#         ans.append(i)
# print(ans)

'''Flatten a simple nested list'''
# l = [[1,2], [3,4], [5]] 
# ans=[]
# for i in l:
#     for j in i:
#         ans.append(j)
# print(ans)

'''Find maximum and minimum without max() / min()'''
# l=[5,3,5,86,4,6,6,645,6,52,3,3]
# max_ele = l[0]
# min_ele = l[0]
# for i in l:
#     if i>max_ele:
#         max_ele=i
#     elif i<min_ele:
#         min_ele=i
# print(f"max_element {max_ele}")
# print(f"min_element {min_ele}")


'''Find second largest element'''
# l=[5,3,5,86,4,6,6,645,6,52,3,3]
# largest = 0
# se_largest = 0
# for i in l:
#     if i>largest:
#         se_largest = largest
#         largest = i
#     elif i>se_largest and i!=largest:
#         se_largest=i
# print(se_largest)

'''19. Find second smallest element'''
# l=[5,3,5,86,4,6,6,645,6,52,3,3]
# small = l[0]
# se_small = l[0]
# for i in l:
#     if i<small:
#         se_small=small
#         small=i
#     elif i<se_small and i!=small:
#         se_small=i
# print(se_small)

'''Separate even and odd numbers'''
'''Two Pointer Approach'''
# l=[1,2,3,4,5,6,7,8,9,10]
# left = 0
# for right in range(len(l)):
#     if l[right]%2!=0:
#         l[left],l[right]=l[right],l[left]
#         left+=1
# print(l)

'''Core Python'''
# l=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd+even)


'''Count even and odd numbers'''
# l=[1,2,3,4,5,6,7,8,9]
# even_count = 0
# odd_count = 0
# for i in l:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print({'even_count':even_count,'odd_count':odd_count})

'''Move all zeroes to the end'''
# l=[1,0,2,0,3,0,4,0]
# zeroes = []
# non_zeroes = []
# for i in l:
#     if i==0:
#         zeroes.append(i)
#     else:
#         non_zeroes.append(i)
# print(non_zeroes+zeroes)

'''25. Rotate a list by K positions'''  '''{LEft}'''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi = l[0]
#     for i in range(len(l)-1):
#         l[i] = l[i+1]
#     l[-1] = fi
# print(l)

'''25. Rotate a list by K positions'''  '''{RIGht}'''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     lv = l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i] = l[i-1]
#     l[0] = lv
# print(l)

'''Create a frequency dictionary from a list'''
# l = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5]
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''27. Find the key having maximum value'''
# d = {
#     "A": 10,
#     "B": 25,
#     "C": 15,
#     "D": 30
# }
# max_value = 0
# for i in d:
#     if d[i]>max_value:
#         max_value=d[i]
#         ans=i
# print(ans)
# print(max_value)

'''Sort a dictionary by values ascending '''
# d = {"A": 40, "B": 10, "C": 30, "D": 20}
# l = list(d.items())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i][1]>l[j][1]:
#             l[i],l[j]=l[j],l[i]
# ans = dict(l)
# print(ans)
        
# ans = dict(sorted(d.items(), key=lambda x: x[1]))
# print(ans)

'''Sort a dictionary by values descending '''
# d = {"A": 40, "B": 10, "C": 30, "D": 20}
# l = list(d.items())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i][1]<l[j][1]:
#             l[i],l[j]=l[j],l[i]
# ans = dict(l)
# print(ans)

# ans = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
# print(ans)

'''Merge two dictionaries'''
# d1 = {"a": 10, "b": 20}
# d2 = {"c": 30, "d": 40}
# l1 = list(d1.items())
# l2 = list(d2.items())
# ans = l1+l2
# d = dict(ans)
# print(d)

# d1 = {"a": 10, "b": 20}
# d2 = {"c": 30, "d": 40}
# merge_dict = d1|d2
# print(merge_dict)

''' without built in method'''
# d1 = {"a": 10, "b": 20}
# d2 = {"c": 30, "d": 40}
# d={}
# for i in d1:
#     if i not in d:
#         d[i] = d1[i]
# for j in d2:
#     if j not in d:
#         d[j]=d2[j]
# print(d)

'''D1 priority:
if j not in d:
    d[j] = d2[j]
D2 priority:
d[j] = d2[j]'''


'''Find common keys between two dictionaries'''
# d1 = {"a": 10, "b": 20,'f':78}
# d2 = {"c": 30, "a": 40,'f':34}
# for i in d1:
#     if i in d2:
#         print(f"The common keys are {i}")


'''Find keys having duplicate values'''
# d1 = {"a": 10, "b": 30,'g':78}
# d2 = {"c": 30, "a": 40,'f':10}
# for i in d1:
#     for j in d2:
#         if d1[i] == d2[j]:
#             print((i,j))


'''Invert a dictionary'''
# d = {"a": 1, "b": 2}
# new_dict = {}
# for i in d:
#     new_dict[d[i]] = i
# print(new_dict)

'''33.Group words according to their length'''
# l = ["cat","dog","apple","bat"]
# d={}
# for i in l:
#     length = len(i)
#     if length not in d:
#         d[length] = []
#     d[length].append(i)
# print(d)          


        






