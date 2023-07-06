from collections import Counter

def findAnagrams(s, p):
    result = []
    target_dict = Counter(p)
    window_dict = Counter()

    left, right = 0, 0
    window_size = len(p)
    s_len = len(s)

    while right < s_len:
        window_dict[s[right]] += 1

        if right >= window_size:
            if window_dict[s[left]] == 1:
                del window_dict[s[left]]
            else:
                window_dict[s[left]] -= 1
            left += 1

        if window_dict == target_dict:
            result.append(left)

        right += 1

    return result

# Test the example input
s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)  # Output: [0, 6]
