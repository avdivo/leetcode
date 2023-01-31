def lengthOfLongestSubstring(s: str) -> int:

    hashmap = {}
    res = i = 0

    while i < len(s):
        if s[i] in hashmap:
            if res < len(hashmap):
                res = len(hashmap)

            j = hashmap[s[i]]
            d = []
            for k, v in hashmap.items():
                if v <= j:
                    d.append(k)
            [hashmap.pop(n) for n in d]
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