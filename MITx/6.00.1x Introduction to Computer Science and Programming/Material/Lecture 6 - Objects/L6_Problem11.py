animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def howMany(d):
    num = 0
    for i in d:
        #print(i)
        #print(d[i])
        for j in d[i]:
            #print(j)
            num += 1
        #numArr.append(d.keys)

    return num

# print(howMany(animals)) # 6

def biggest(aDict):
    char = None
    num = 0
    for i in aDict:
        print(len(aDict[i]))
        if len(aDict[i]) >= num:
            num = len(aDict[i])
            char = i
        #print(i)
        #print(d[i])
        #for j in d[i]:
            #print(j)
        #numArr.append(d.keys)

    return char

# print(biggest(animals)) # 'd'
# print(biggest({})) # None
# print(biggest({'z': []})) # 'z'
print(biggest({'a': [15, 20, 7, 0], 'c': [16, 14, 8, 15, 5], 'b': [14, 20, 6]})) #c
#print(animals)
