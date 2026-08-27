'''•	Valid Parentheses '''
s = "({[]})"
stack = []
is_valid = True
for i in s:
    if i in '({[':
        stack.append(i)
    else:
        if not stack:
            is_valid=False
            break
        else:
            if i==')' and stack[-1] == '(':
                stack.pop()
            elif i=='}' and stack[-1] == '{':
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            else:
                is_valid = False
                break
if not stack and is_valid:
    print(True)
else:
    print(False)