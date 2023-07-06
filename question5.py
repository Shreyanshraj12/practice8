def compress(chars):
    write = 0
    read = 0
    count = 1

    while read < len(chars):
        if read + 1 == len(chars) or chars[read] != chars[read + 1]:
            chars[write] = chars[read]
            write += 1
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1
            count = 1
        else:
            count += 1
        read += 1

    return write

# Test the example input
chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = compress(chars)
print(new_length)  # Output: 6
print(chars[:new_length])  # Output: ['a', '2', 'b', '2', 'c', '3']
