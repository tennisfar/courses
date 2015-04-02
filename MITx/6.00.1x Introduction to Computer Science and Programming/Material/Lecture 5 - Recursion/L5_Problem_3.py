def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1

    if exp % 2: # even
        return base*recurPowerNew(base*base, exp/2)
    else:
        return base * recurPowerNew(base, exp-1)



print(recurPowerNew(3, 3))
