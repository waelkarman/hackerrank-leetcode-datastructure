
def cansumTab(target,array):

    cs = [False for _ in range(target+1)]

    # initialization
    cs[0]=True
    for a in array:
        cs[a]=True

    for i in range(target+1):
        for k in range(i,target+1):
            if cs[k] == True and i+k <= target:
                cs[i+k] = True
            
    print(cs)
    return cs[len(cs)-1]

print(cansumTab(7,[3,4,5]))