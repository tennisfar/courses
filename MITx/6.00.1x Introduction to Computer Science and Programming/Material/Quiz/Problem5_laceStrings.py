def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    # Your Code Here
    laced = ''
    loops = min(len(s1), len(s2))
    i = 0
    for i in range(loops):
        laced += s1[i:i+1]
        laced += s2[i:i+1]

    if len(s1) > len(s2):
        laced += s1[i+1:]
        return laced
    elif len(s1) < len(s2):
        laced += s2[i+1:]
        return laced
    else:
        return laced


print(laceStrings('abcd', 'efghi')) # should return aebfcgdhi
