def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    number = 0
    for c in aStr:
        number += 1

    return number

print(lenIter('xxxcc'))
