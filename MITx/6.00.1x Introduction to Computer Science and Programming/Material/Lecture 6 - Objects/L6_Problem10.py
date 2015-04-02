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

print(howMany(animals)) # 6

#print(animals)
