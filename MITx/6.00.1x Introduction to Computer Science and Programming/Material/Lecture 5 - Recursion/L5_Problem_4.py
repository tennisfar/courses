def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    c = min(a,b)

    while a%c !=0 or b%c !=0 :
        c -= 1

    return c

print(gcdIter(6, 12))
