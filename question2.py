def checkValidString(s):
    stack = []

    # First pass: Match '*' and '(' with corresponding ')'
    for char in s:
        if char in ['(', '*']:
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

    # Second pass: Match remaining '(' with '*'
    i = len(stack) - 1
    while stack and stack[i] == '(':
        stack.pop()
        i -= 1

    return len(stack) == 0
s = "()"
result = checkValidString(s)
print(result)  # Output: True
