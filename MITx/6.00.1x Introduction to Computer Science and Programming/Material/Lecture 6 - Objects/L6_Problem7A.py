def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

# return [5, -20, 40, -45]
# def timesFive(a):
#    return a * 5
# applyToEach(testList, timesFive)

# return [1, 4, 8, 9]
# applyToEach(testList, abs)

# return [2, -3, 9, -8]
#def addOne(a):
#    return a + 1
# applyToEach(testList, addOne)

# return [1, 16, 64, 81]
def power(a):
    return a*a
applyToEach(testList, power)

print testList
