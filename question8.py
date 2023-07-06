def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    
    if s == goal:
        # Check if there are at least two repeated characters in s
        char_count = {}
        for char in s:
            if char in char_count:
                return True
            char_count[char] = 1
        return False
    
    indices = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            indices.append(i)
    
    if len(indices) != 2:
        return False
    
    i, j = indices
    return s[i] == goal[j] and s[j] == goal[i]

# Test the example input
s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)  # Output: True
