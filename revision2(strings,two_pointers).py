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
# s = "egg"
# t = "add"
# if len(s)!=len(t):
#     print(False)
# else:
#     s_to_t={}
#     t_to_s={}
#     valid = True
#     for i in range(len(s)):
#         a=s[i]
#         b=t[i]
#         if a in s_to_t and s_to_t[a]!=b:
#             valid=False
#             break
#         if b in t_to_s and t_to_s[b]!=a:
#             valid=False
#             break
#         s_to_t[a]=b
#         t_to_s[b]=a
# print(valid)
# print(s_to_t)
# print(t_to_s)

'''•	Reverse Vowels '''
# s = 'he3llo'
# l=list(s)
# seen = set('AEIOUaeiou')
# left = 0
# right = len(s)-1
# while left<right:
#     if l[left] not in seen:
#         left+=1
#     elif l[right] not in seen:
#         right-=1
#     else:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# s="".join(l)
# print(s)


'''Reverse Only Letters '''
# s = "a3bC-dEf-ghIj"
# l=list(s)
# left = 0
# right = len(s)-1
# while left<right:
#     if not l[left].isalpha():
#         left+=1
#     elif not l[right].isalpha():
#         right-=1
#     else:
#         l[left],l[right]=l[right],l[left]
#         left+=1
#         right-=1
# s="".join(l)
# print(s)


'''Valid Palindrome II (LeetCode 680)'''
s = "abca"
left=0
right=len(s)-1
is_valid=True
while left<right:
    if s[left]==s[right]:
        left+=1
        right-=1
    else:
        skip_left = s[left+1:right+1]
        skip_right = s[left:right]
        if skip_left!=skip_left[::-1] and skip_right!=skip_right[::-1]:
            is_valid=False
        break
print(is_valid)

        

# ======================================== TWO__POINTERS =====================================================

# l = ['P','Y','T','H','O','N']
# l2=[]
# target = 'T'
# for i in l:
#     if i!=target:
#         i='@'
#     l2.append(i)
# print(l2)

'''•	Reverse Array (done)'''
# l=[1,2,3,4,5]
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# print(l)

'''•	Move Zeroes (done)'''
# l=[1,0,3,0,4,0]
# left=0
# for right in range(len(l)):
#     if l[right]!=0:
#         l[left],l[right]=l[right],l[left]
#         left+=1
# print(l)


'''•	Remove Duplicates (done)'''
# l=[1,2,2,3,4]
# left=0
# for right in range(1,len(l)):
#     if l[right]!=l[left]:
#         left+=1
#         l[left]=l[right]
# print(l[:left+1])


'''•	Remove Element '''
# l=[0, 1, 2, 2, 3, 0, 4, 2]
# target=2
# i=0
# for j in l:
#     if j!=target:
#         l[i]=j
#         i+=1
# print(i)
# print(l[:i])

'''•	Sorted Two Sum '''
# l = [1, 2, 4, 6, 10]
# target = 8
# left=0
# right=len(l)-1
# while left<right:
#     current_sum=l[left]+l[right]
#     if current_sum==target:
#         print((l[left],l[right]))
#         break
#     elif current_sum<target:
#         left+=1
#     else:
#         right-=1


'''•	Merge Sorted Arrays(done) '''
# l1=[1,3,5]
# l2=[2,4,6]
# i=0
# j=0
# ans=[]
# while i<len(l1) and j<len(l2):
#     if l1[i]<l2[j]:
#         ans.append(l1[i])
#         i+=1
#     else:
#         ans.append(l2[j])
#         j+=1
# while i<len(l1):
#     ans.append(l1[i])
#     i+=1
# while j<len(l2):
#     ans.append(l2[j])
#     j+=1
# print(ans)

'''Squares of a Sorted Array'''
# l = [-4, -1, 0, 3, 10]
# left=0
# right=len(l)-1
# ans=[0]*len(l)
# pos=len(l)-1
# while left<=right:
#     if l[left]**2>l[right]**2:
#         ans[pos]=l[left]**2
#         left+=1
#     else:
#         ans[pos]=l[right]**2
#         right-=1
#     pos-=1
# print(ans)

''''''
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left=0











    


 
