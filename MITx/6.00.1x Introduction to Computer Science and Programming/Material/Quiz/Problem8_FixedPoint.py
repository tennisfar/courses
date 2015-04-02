def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        print('guess: '+ str(guess) + ', f(guess): ' + str(f(guess)) + ', res: ' + str(guess - f(guess)))
        if abs(guess - f(guess)) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

#def f(a):
#    def tryit(x):
#        return 0.5 * (a/x + x)
#    return tryit

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)


#def sqrt(a):
#    def tryit(x):
#        return 0.5 * (a/x + x)
#    return fixedPoint(tryit(a), 0.0001)


print(str(sqrt(25)))
