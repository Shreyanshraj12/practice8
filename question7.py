def decodeString(s):
    stack = []

    for char in s:
        if char != ']':
            stack.append(char)
        else:
            decoded_str = ''
            while stack[-1] != '[':
                decoded_str += stack.pop()
            stack.pop()  # Pop the opening bracket '['
            
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            k = int(k)
            
            repeated_str = decoded_str * k
            stack.append(repeated_str)
    
    result = ''
    while stack:
        result += stack.pop()
    
    return result[::-1]

# Test the example input
s = "3[a]2[bc]"
result = decodeString(s)
print(result)  # Output: "aaabcbc"
