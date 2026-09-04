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


'''Replace Zero With One '''
# n = 2007
# new = 0
# while n>0:
#     digit = n%10
#     if digit == 0:
#         digit = 1
#     n=n//10
#     new = new*10+digit
# rev = 0
# while new>0:
#     digit=new%10
#     rev = rev*10+digit
#     new=new//10
# print(rev)


        
'''Count frequency of words in a sentence'''
# s = '"I am learning Python and I am learning Django"'
# l = s.split()
# d = {}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)


'''35. Convert two lists into a dictionary'''
# keys = ["a","b","c"]
# values = [1,2,3]
# d={}
# for i in range(len(keys)):
#     if keys[i] not in d:
#         d[keys[i]] = values[i]
# print(d)

'''2. Different length — shorter list tak'''
# keys = ["a", "b", "c", "d"]
# values = [1, 2, 3]
# d = {}
# for i in range(min(len(keys), len(values))):
#     d[keys[i]] = values[i]
# print(d)


'''Create list of squares using list comprehension'''
# l = [1,2,3,4,5,6,7,8]
# ans = [i**2 for i in l]
# print(ans)

'''Create list of even numbers using comprehension'''
# l = [1,2,3,4,5,6,7,8]
# ans = [i for i in l if i%2==0 ]
# print(ans)

'''Create list of odd numbers using comprehension'''
# l = [1,2,3,4,5,6,7,8]
# ans = [i for i in l if i%2!=0]
# print(ans)

'''Convert a list of strings to uppercase using comprehension'''
# l=["python", "django", "sql", "rest"]
# ans = [i.upper() for i in l]
# print(ans)

'''Extract numbers greater than 10'''
# l = [1,2,45,6,78,7,57,9,8]
# ans = [i for i in l if i>10]
# print(ans)

'''Create dictionary using dictionary comprehension'''
# l = [1, 2, 3, 4, 5]
# ans = {i:i**2 for i in l}
# print(ans)

'''Create a dictionary containing only even numbers and their squares.'''
# l = [1, 2, 3, 4, 5, 6]
# ans = {i:i**2 for  i in l if i%2==0}
# print(ans)

'''Using dictionary comprehension, create a dictionary containing only numbers greater than 5, 
where the number is the key and its cube is the value.'''
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ans = {i:i**3 for i in l if i>5}
# print(ans)
'''{ key : value  for item in iterable  if condition }
   ↓      ↓          ↓                   ↓
   i     i**3       i in l              i > 5'''


'''List ke numbers ko dictionary mein rakho. Agar number even hai toh value "Even" ho, warna "Odd"'''
# l = [1, 2, 3, 4]
# ans = {i:'even' if i%2==0 else 'odd' for i in l}
# print(ans)


'''Dictionary comprehension use karke dictionary banao jisme:
Sirf even numbers include hon.
Number key ho.
Uski square value ho.
Lekin agar square 200 se greater ho, toh us number ko dictionary mein include mat karo.'''
# l = [12, 5, 8, 21, 16, 7, 30, 11]
# ans = {i:i**2 for i in l if i%2==0 and i**2<=200}
# print(ans)


'''Dictionary comprehension use karke dictionary banao jisme:
Sirf odd numbers include hon.
Number key ho.
Uski cube value ho.
Lekin cube 3000 se greater ho toh exclude kar do.'''
# l = [5, 12, 7, 20, 15, 8, 25, 10]
# ans = {i:i**3 for i in l if i%2!=0 and i**3<=3000}
# print(ans)

'''Flatten a nested list using comprehension'''
# l = [ [1, 2], [3, 4], [5, 6] ]
# ans = [j for i in l for j in i]
# print(ans)
'''Normal loop:

for i in l:
    for j in i:
        print(j)'''

# comphernsion
'''[j      for i in l      for j in i]
 ↑           ↑               ↑
kya       outer loop      inner loop
store
karna'''

# =================================================================
'''FUNCTIONS'''
'''Write a function using default arguments'''
# def default(name,city='bhopal'):
#     return f'hello {name} welcome to {city}'
# ans1 = default('piyush')
# print(ans1)
# ans2 = default('piyush','indore')
# print(ans2)

'''Write a function using *args'''
# def test(name,*marks):
#     return f'{name}:{marks}'
# ans1 = ('piyush',67,89,34)
# print(ans1)

# def sum_all(*l):
#     total = 0
#     for i in l:
#         total+=i
#     return total
# x = sum_all(1,2,3,4,5)
# print(x)

'''Write a function using **kwargs'''
# def test(name,**kwargs):
#         print("UserName :", name)
#         for key,value in kwargs.items():
#                 print(key, ':' ,value)
# test('piyush',age=22,city="indore",role="django devloper")

'''Write a function that accepts both *args and **kwargs'''
def stu_details(name,*marks,**details):
    print("Student Name: ", name)
    print("--- Marks ---")
    for subject, score in marks:
        print(subject, ":", score)
    print("--- Details ---")
    for key,value in details.items():
        print(key , ':' ,value)
stu_details('Piyush',('Maths', 98), ('Physics', 92), ('Chemistry', 90), ('English', 86), ('CS', 77),
            age=22, city='bhopal', status='pass'
)


