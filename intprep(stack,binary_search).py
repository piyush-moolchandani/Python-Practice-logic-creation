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

    

