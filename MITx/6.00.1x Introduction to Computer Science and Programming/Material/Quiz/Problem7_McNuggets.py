def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    # 6a+9b+20c=n

    # max number of loops: 6*a=n => a=n/6
    myRange = n/6
    for i in range(myRange):
        for j in range(myRange):
            for k in range(myRange):
                if 6*i + 9*j + 20*k == n:
                    return True
    return False


print(McNuggets(400)) # should return True
