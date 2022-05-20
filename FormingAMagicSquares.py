
    
    cost = 0
    mapkey = {}
    magix = {}
    
    mapkey[1] = 9
    mapkey[2] = 8
    mapkey[3] = 7
    mapkey[4] = 6
    mapkey[9] = 1
    mapkey[8] = 2
    mapkey[7] = 3
    mapkey[6] = 4
    
    magix[s[0][0]] = s[2][2] 
    magix[s[1][0]] = s[1][2] 
    magix[s[2][0]] = s[0][2] 
    magix[s[0][1]] = s[2][1] 
    
    to_del=[]
    
    for x in mapkey.keys():
        if x in magix.keys() and mapkey[x] == magix[x]:
            del magix[x]
            to_del.append(mapkey[x])
            to_del.append(x)
    
    for x in to_del:
        del mapkey[x]
        
    print(s)    
    print(magix)
    print(mapkey)
    
    # COMPUTE ON MAGIX AND MAPKEY MINIMUM DISTANCE
    # TO DO: 17/23 failed - 21
    #    - Consider matrix with duplicated couple - TO CHECK
    #    - Consider minimum for all permutation - SOLVED
    
    if s[1][1]!=5:
        cost += abs(s[1][1]-5)
        s[1][1] = 5
    
    ky = 0
    magix_k = magix.keys()
    exit_cost=200
    
    perm = permutations(magix_k, len(magix_k))
    for i in list(perm):
        print(f"permutation : {i}")
        magix_key=i
        partial_cost=0
        mapkey_copy = mapkey.copy()
        for k in magix_key:
            mapkey_key = mapkey_copy.keys()
            print(f"bind with : {mapkey_key} ---- magix = {k}")
            min_cost = 100
            for x in mapkey_key:
                if min_cost > abs(k-x)+abs(magix[k]-mapkey_copy[x]):
                    min_cost = abs(k-x)+abs(magix[k]-mapkey_copy[x])
                    ky = x
                if min_cost > abs(k-mapkey_copy[x])+abs(magix[k]-x):
                    min_cost = abs(k-mapkey_copy[x])+abs(magix[k]-x)
                    ky = x
            if len(mapkey_copy)>0:
                partial_cost+=min_cost
                del mapkey_copy[mapkey_copy[ky]]
                del mapkey_copy[ky]
        print(f"min cost is : {partial_cost}" )
        if exit_cost > partial_cost:
            exit_cost=partial_cost 
        
    return cost+exit_cost


