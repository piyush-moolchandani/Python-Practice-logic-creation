'''•	Valid Parentheses '''
# s = "({[]})"
# stack = []
# is_valid = True
# for i in s:
#     if i in '({[':
#         stack.append(i)
#     else:
#         if not stack:
#             is_valid=False
#             break
#         else:
#             if i==')' and stack[-1] == '(':
#                 stack.pop()
#             elif i=='}' and stack[-1] == '{':
#                 stack.pop()
#             elif i == "]" and stack[-1] == "[":
#                 stack.pop()
#             else:
#                 is_valid = False
#                 break
# if not stack and is_valid:
#     print(True)
# else:
#     print(False)


'''•	Next Greater Element '''
# l = [4, 5, 2, 10, 8]
# ans=[]
# for i in range(len(l)):
#     found = -1
#     for j in range(i+1,len(l)):
#         if l[j]>l[i]:
#             found = l[j]
#             break
#     ans.append(found)
# print(ans)

'''optimized approach '''
# l = [4, 5, 2, 10, 8]
# ans=[]
# stack = []
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
# ans = []
# for i in range(len(l)):
#     found = -1
#     for j in range(i-1,-1,-1):
#         if l[j]<l[i]:
#             found=l[j]
#             break
#     ans.append(found)
# print(ans)

'''optimized approach'''
# l = [4, 5, 2, 10, 8]
# stack = []
# ans = []
# for i in range(len(l)):
#     while stack and stack[-1]>=l[i]:
#         stack.pop()
#     if not stack:
#         ans.append(-1)
#     else:
#         ans.append(stack[-1])
#     stack.append(l[i])
# print(ans)

