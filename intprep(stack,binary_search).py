# -----------------------------------------STACK-----------------------------------------------------
'''valid parenthesis'''
# s = "()]{}"
# stack =[]
# is_valid = True
# for i in s:
#     if i in "[{(":
#         stack.append(i)
#     else:
#         if not stack:
#             is_valid = False
#             break
#         else:
#             if i==')' and stack[-1]=='(':
#                 stack.pop()
#             elif i==']' and stack[-1]=='[':
#                 stack.pop()
#             elif i=='}' and stack[-1]=='{':
#                 stack.pop()
#             else:
#                 is_valid = False
#                 break
# if is_valid and  not stack:
#     print("valid")
# else:
#     print("invalid")
            
''' function approach '''
# def valid_parentheses(s):
#     stack = []
#     for i in s:
#         if i in "[{(":
#             stack.append(i)
#         else:
#             if not stack:
#                 return False
#             if i == ')' and stack[-1] == '(':
#                 stack.pop()
#             elif i == ']' and stack[-1] == '[':
#                 stack.pop()
#             elif i == '}' and stack[-1] == '{':
#                 stack.pop()
#             else:
#                 return False
#     return not stack

'''•	Next Greater Element '''
# l = [4, 5, 2, 10, 8]
# stack = []
# ans=[]
# for i in range(len(l)-1,-1,-1):
#     while stack and stack[-1]<=l[i]:
#         stack.pop()
#     if not stack:
#         ans.append(-1)
#     else:
#         ans.append(stack[-1])
#     stack.append(l[i])
# ans.reverse()
# print(ans)


'''•	Previous Smaller Element '''
# l = [4, 5, 2, 10, 8]
# stack = []
# ans = []
# for i in l:
#     while stack and stack[-1]>=i:
#         stack.pop()
#     if not stack:
#         ans.append(-1)
#     else:
#         ans.append(stack[-1])
#     stack.append(i)
# print(ans)


'''•	Stock Span '''
# l = [100, 80, 60, 70, 60, 75, 85]
# stack=[]
# ans=[]
# for i in range(len(l)):
#     while stack and l[stack[-1]]<=l[i]:
#         stack.pop()
#     if not stack:
#         ans.append(i+1)
#     else:
#         ans.append(i-stack[-1])
#     stack.append(i)
# print(ans)


'''•	Remove Adjacent Duplicates '''
# s = "abbaca"
# stack = []
# for i in s:
#     if stack and stack[-1]==i:
#         stack.pop()
#     else:
#         stack.append(i)
# result = "".join(stack)
# print(result)

# ---------------------------------------Binary Search------------------------------------------------

'''•	Binary Search ''' 
# l = [2, 4, 7, 10, 13, 18, 21]
# target = 13
# left = 0
# right = len(l)-1
# found = False
# while left<=right:
#     mid = (left+right)//2
#     if l[mid]==target:
#         print(mid)
#         found = True
#         break
#     elif l[mid]<target:
#         left = mid+1
#     else:
#         right = mid-1
# if not found:
#     print(-1)

# fuction approach
# def binary_search(l, target):
#     left = 0
#     right = len(l) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if l[mid] == target:
#             return mid
#         elif l[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# x = [2, 4, 7, 10, 13, 18, 21]
# t = 13
# print(binary_search(x,t))


'''•	First Occurrence '''
# def first_occurence(l,target):
#     left = 0
#     right = len(l)-1
#     ans = -1
#     while left<=right:
#         mid = (left+right)//2
#         if l[mid] == target:
#             ans = mid
#             right = mid -1
#         elif l[mid]<target:
#             left = mid +1
#         else:
#             right = mid -1
#     return ans
# x = [2, 4, 4, 4, 7, 10]
# t = 4
# print(first_occurence(x,t))






