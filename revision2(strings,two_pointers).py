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


'''•	String Compression '''
# s = "aaabbcccc"
# if not s:
#     print("")
# else:
#     count=1
#     ans=""
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             ans+=s[i]+str(count)
#             count=1
#     ans+=s[-1]+str(count)
#     print(ans)

'''•	Rotation Check'''
# s1 = "abcd"
# s2 = "cdab"
# if len(s1)==len(s2):
#     temp = s1+s2
#     if s2 in temp:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

'''•	Longest Common Prefix '''
# strs = ["flower", "flow", "flight"]
# commmon=""
# for i in range(len(strs[0])):
#     char=strs[0][i]
#     match=True
#     for j in range(1,len(strs)):
#         if i>=len(strs[j]) or strs[j][i]!=char:
#             match=False
#             break
#     if not match:
#         break
#     commmon+=char
# print(commmon)

'''•	Longest Substring Without Repeating Characters '''
# s='abcabcab'
# left = 0
# seen=set()
# max_len=0
# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left+=1
#     seen.add(s[right])
#     max_len = max(max_len, right - left + 1)
# print(max_len)

'''•	Valid Anagram (Revision)  '''
# s = "anagram"
# t = "nagaram"
# if len(s)!=len(t):
#     print(False)
# else:
#     d1={}
#     d2={}
#     for i in s:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
#     for j in t:
#         if j in d2:
#             d2[j]=d2[j]+1
#         else:
#             d2[j]=1
#     if d1==d2:
#         print('anagram')
#     else:
#         print('not anagram')


'''•	Isomorphic Strings '''
s = "egg"
t = "add"
if len(s)!=len(t):
    print(False)
else:
    s_to_t={}
    t_to_s={}
    valid = True
    for i in range(len(s)):
        a=s[i]
        b=t[i]
        if a in s_to_t and s_to_t[a]!=b:
            valid=False
            break
        if b in t_to_s and t_to_s[b]!=a:
            valid=False
            break
        s_to_t[a]=b
        t_to_s[b]=a
print(valid)
print(s_to_t)
print(t_to_s)
