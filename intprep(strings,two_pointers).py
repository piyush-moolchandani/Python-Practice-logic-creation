'''                                     STRINGS                                  '''
'''•	Reverse String '''
# n="python"
# new=""
# for i in range(len(n)-1,-1,-1):
#     new=new+n[i]
# print(new)
'''two pointers approach'''
# n="python"
# convert=list(n)
# i=0
# j=len(n)-1
# while i<j:
#     convert[i],convert[j]=convert[j],convert[i]
#     i+=1
#     j-=1
# n="".join(convert)
# print(n)

'''•	Reverse Words '''
# n="hello my name is python"
# l=n.split()
# i=0
# j=len(l)-1
# while i<j:
#     l[i],l[j]=l[j],l[i]
#     i+=1
#     j-=1
# n=" ".join(l)
# print(n)
'''🔥 Ek interview tip
Agar interviewer Reverse Words de aur tum turant bolo:
"I'll split the sentence into words and then reuse the same two-pointer reverse algorithm that we use for reversing arrays."
To interviewer ko ye signal milta hai ki tum algorithms ko memorize nahi karte, patterns identify karte ho.
Ye DSA interviews me bahut positive impression deta hai. 💯'''

'''•	Palindrome '''
# n="madam"
# i=0
# j=len(n)-1
# is_pallindrome=True
# while i<j:
#     if n[i]!=n[j]:
#         is_pallindrome=False
#         break
#     i+=1
#     j-=1
# if is_pallindrome:
#     print("pallindrome")
# else:
#     print("not pallindrome")

'''•	Valid Palindrome '''
# n = "A man, a plan, a canal: Panama"
# l=""
# for i in n:
#     if i.isalnum():
#         l=l+i.lower()
# i=0
# j=len(l)-1
# is_pallindrome = True
# while i<j:
#     if l[i]!=l[j]:
#         is_pallindrome = False
#         break
#     i+=1
#     j-=1
# if is_pallindrome:
#     print('palindrome')
# else:
#     print('not pallindrome')


'''•	Character Frequency '''
# s = "programming"
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

'''•	Remove Spaces '''
# n = "hello my name is python"
# ans=""
# for i in n:
#     if i!=" ":
#         ans=ans+i
# print(ans)       

'''•	•	Count Vowels ''' 
# n = "piyush"
# count_vowel = 0
# for i in n:
#     if i in "aeiou":
#         count_vowel+=1
# print(count_vowel)


'''•	Remove Duplicates '''
# n="programming"
# d={}
# ans=""
# for i in n:
#     if i not in d:
#         ans+=i
#         d[i]=1
# print(ans)

'''•	String Compression '''
# s = "aaabbcccc"
# if not s:
#     print("")
# else:
#     ans=""
#     count=1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             ans+=s[i]+str(count)
#             count=1
# ans+=s[-1]+str(count)
# print(ans)

'''•	Rotation Check '''
# s1 = "abcd"
# s2 = "cdab"
# temp = s1+s1
# if s2 in temp:
#     print(True)
# else:
#     print(False)

'''                                  TWO POINTERS                                 '''
'''•	Remove Element '''
# l = [0,1,2,2,3,0,4,2]
# val = 2
# i=0
# for j in range(len(l)):
#     if l[j]!=val:
#         l[i],l[j]=l[j],l[i]
#         i+=1
# print(l[:i])

'''•	Sorted Two Sum '''
# l = [1, 2, 4, 6, 10]
# target = 8
# left=0
# right=len(l)-1
# while left<right:
#     sum=l[left]+l[right]
#     if sum==target:
#         print((l[left],l[right]))
#         break
#     if sum<target:
#         left+=1
#     else:
#         right-=1



        

        









