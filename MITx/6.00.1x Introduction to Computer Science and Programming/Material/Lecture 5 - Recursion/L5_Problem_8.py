def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    charsInStr = len(aStr)
    #for c in aStr:
    #    charsInStr += 1

    if charsInStr == 0:
        return False

    if charsInStr == 1:
        if char == aStr:
            return True
        else:
            return False

    middle = charsInStr/2
    aStrChar = aStr[middle-1:middle]

    if char == aStrChar:
        return True
    else:
        if char > aStrChar:
            return isIn(char, aStr[middle:])
        else:
            return isIn(char, aStr[:middle])

print(isIn('c','abcdefgh'))
