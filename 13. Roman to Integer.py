def romanToInt(s: str) -> int:

    numbers = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
               'CM': 900, 'M': 1000}
    dec = i = 0

    while i < len(s):
        if s[i] in 'IXC' and i < len(s)-1:
            if s[i:i+2] in 'IV IX XL XC CD CM':
                dec += numbers[s[i:i+2]]
                i += 2
                continue
        dec += numbers[s[i]]
        i += 1

    return dec

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
