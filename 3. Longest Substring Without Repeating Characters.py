def lengthOfLongestSubstring(s: str) -> int:

    hashmap = {}
    res = i = 0

    while i < len(s):
        if s[i] in hashmap:
            if res < len(hashmap):
                res = len(hashmap)
            i = hashmap[s[i]] + 1
            hashmap.clear()
        else:
            hashmap[s[i]] = i
            i += 1

    if res < len(hashmap):
        res = len(hashmap)

    return res

print(lengthOfLongestSubstring('abcabcbb'))

print(lengthOfLongestSubstring('bbbbb'))

print(lengthOfLongestSubstring('pwwkew'))

print(lengthOfLongestSubstring(' '))