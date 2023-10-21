
#cache={}
def bestSum(target,array,cache={}):
    print(f"target:{target}, cache:{cache}")
    #if f"{target}" in cache:
    #    return cache[f"{target}"]
    
    if target < 0:
        return None
    
    if target == 0:
        return []

    shortestlist = None

    for a in array:
        ans = bestSum(target-a,array,cache)
        if ans is not None:
            ans.append(a)
            if shortestlist is None or len(ans) < len(shortestlist):
                shortestlist = ans                
                

    cache[f"{target}"]=shortestlist
    return shortestlist



print(bestSum(4,[1,2]))
#print(bestSum(5,[2,1]))
#print(bestSum(5,[2]))
#print(bestSum(7,[2,3]))
#print(bestSum(7,[5,3,4,7]))
#print(bestSum(7,[2,4]))
#print(bestSum(8,[2,3,5]))
#print(bestSum(300,[7,14])) #critical
