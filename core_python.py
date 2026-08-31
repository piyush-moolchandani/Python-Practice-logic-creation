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






