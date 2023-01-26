from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    pref = ''
    strs = sorted(strs, key=len)

    for i, letter in enumerate(strs[0]):

        for j in range(1, len(strs)):
            if letter != strs[j][i]:
                con = False
                break
        else:
            pref += letter
            continue
        break

    return pref



strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))