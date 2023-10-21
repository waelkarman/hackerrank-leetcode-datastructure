
def howsum(target,array,cache={}):
    
    if target in cache:
        return cache[target]
    if target < 0 :
        return None
    if target == 0:
        return []
    
    for a in array:
        ans = howsum(target-a,array)
        if ans is not None:
            ansnew= ans+[a]
            cache[target]=ansnew
            return ansnew

    cache[target]=None
    return None


cache={}
print(howsum(5,[1,2],cache))
cache={}
print(howsum(5,[2,1],cache))
cache={}
print(howsum(5,[2],cache))
cache={}
print(howsum(7,[2,3],cache))
cache={}
print(howsum(7,[5,3,4,7],cache))
cache={}
print(howsum(7,[2,4],cache))
cache={}
print(howsum(8,[2,3,5],cache))
cache={}
print(howsum(300,[7,14],cache)) #not critical anymore