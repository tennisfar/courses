def myLog(x, b): # (16, 2) returns 4
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    res = 1
    while True:
        if b**res > x:
            res -= 1
            break
        elif b**res == x:
            break
        else:
            res += 1
    return res

print(myLog(15,3))
