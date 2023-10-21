

def bestSum(target,array,cache={}):
    
    if target in cache:
        return cache[target]

    if target < 0:
        return None
    
    if target == 0:
        return []
    
    shortestlist = None
    for a in array:

        ans = bestSum(target-a,array,cache)

        if ans is not None:
            ansnew= ans+[a]
            if shortestlist is None or len(ans) < len(shortestlist):
                shortestlist = ansnew

    cache[target]=shortestlist
    return shortestlist

# RUN ONE TEST CASES AT ONCE AND KEEP THE OTHERS COMMENTED
cache={}
print(bestSum(5,[1,2],cache))
cache={}
print(bestSum(5,[2,1],cache))
cache={}
print(bestSum(5,[2],cache))
cache={}
print(bestSum(7,[2,3],cache))
cache={}
print(bestSum(7,[5,3,4,7],cache))
cache={}
print(bestSum(7,[2,4],cache))
cache={}
print(bestSum(8,[2,3,5],cache))
cache={}
print(bestSum(300,[7,14],cache)) # not critical anymore