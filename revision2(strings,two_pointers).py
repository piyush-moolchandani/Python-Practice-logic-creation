'''•	Reverse String '''
# n = "piyush"
# new=""
# for i in range(len(n)-1,-1,-1):
#     new=new+n[i]
# print(new)

'''optimized version '''
# n = "piyush"
# l = list(n)
# left = 0 
# right = len(n)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# n="".join(l)
# print(n)
# ---------------------------------------------------------------------------------------------------------

'''•	Reverse Words '''
# n = "python hates java"
# n = n.split()
# left = 0
# right = len(n)-1
# while left<right:
#     n[left],n[right]=n[right],n[left]
#     left+=1
#     right-=1
# n=" ".join(n)
# print(n)

'''•	Palindrome '''
# s = 'madam'
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# if rev==s:
#     print("pallindrome")

'''optimized version '''
# s = 'madam'
# left = 0
# right = len(s)-1
# is_pallindrome=True
# while left<right:
#     if s[left]!=s[right]:
#         is_pallindrome=False
#         break
#     left+=1
#     right-=1
# if is_pallindrome:
#     print("palindrome")
# else:
#     print('Not palindrome')
# ---------------------------------------------------------------------------------------------------
'''•	Valid Palindrome '''
# s = "A man, a plan, a canal: Panama"
# chars=[]
# for i in s:
#     if i.isalnum():
#         chars.append(i.lower())
# n="".join(chars)
# left=0
# right=len(n)-1
# is_palindrome=True
# while left<right:
#     if n[left]!=n[right]:
#         is_palindrome=False
#         break
#     left+=1
#     right-=1
# if is_palindrome:
#     print('palindrome')
# else:
#     print('Not palindrome')
# ------------------------------------------------------------------------------------------------------
'''•	Character Frequency '''
# s = 'programming'
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Remove Spaces '''
# s = "hello my name is python"
# n = ""
# for i in s:
#     if i!=" ":
#         n=n+i
# print(n)

'''•	Remove Duplicates '''
# s='programming'
# d={}
# ans=""
# for i in s:
#     if i not in d:
#         ans+=i
#         d[i]=1
# print(ans)

'''•	Count Vowels and consonents '''
# s = "piyush"
# vowel_count=0
# consonents_count=0
# for i in s:
#     if i in "aeiou":
#         vowel_count+=1
#     else:
#         consonents_count+=1
# print({"vowels":vowel_count,"consonents":consonents_count})



