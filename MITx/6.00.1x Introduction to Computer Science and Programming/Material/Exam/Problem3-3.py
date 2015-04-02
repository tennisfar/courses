def sort3(lst):
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions below refer to this line
        print('L: ' + str(L))
    return out

lst = [0,2,1,4,3,6,5,8,7,9,8]
lst = [0,1,2,3,4,9,8,7,6,5]
print(sort3(lst))
