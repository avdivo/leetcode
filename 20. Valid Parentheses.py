def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    buf = []

    for i in s:
        if i in ['(', '[', '{']:
            i = i.replace('(', ')').replace('[', ']').replace('{', '}')
            buf.append(i)
        elif i in [')', ']', '}']:
            try:
                if i == buf.pop():
                    continue
                raise
            except:
                return False
        else:
            return False

    if not buf:
        return True
    return False




print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
