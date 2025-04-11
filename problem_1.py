def length_of_longest_substring(string_input):
    
    last_seen = {}
    max_len = 0
    start = 0
    
    for end, char in enumerate(string_input):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        
        last_seen[char] = end
        
        max_len = max(max_len, end - start + 1)
    
    return max_len



print(length_of_longest_substring(''))