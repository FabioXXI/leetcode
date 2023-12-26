def isValid(s):
    brackets = [
        "(", "[", "{", ")", "]", "}"
    ]

    if len(s) % 2 != 0:
        return False

    peding = []

    try:
        for word in s:
            if word == brackets[0]:
                peding.append(word)
            elif word == brackets[1]:
                peding.append(word)
            elif word == brackets[2]:
                peding.append(word)
            elif word == brackets[3] and peding[-1] == brackets[0]:
                peding.pop()
            elif word == brackets[4] and peding[-1] == brackets[1]:
                peding.pop()
            elif word == brackets[5] and peding[-1] == brackets[2]:
                peding.pop()
            else:
                return False
    except:
        return False

    if len(peding) != 0:
        return False

    return True

print(isValid("[({(())}[()])]"))