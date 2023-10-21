

def cansum(target,array,sum=0,cache={}):
    if f"{target}" in cache:
        return cache[f"{target}"]

    if target < 0:
        return False
    
    if target == 0:
        return True

    
    for a in array:
        ans = cansum(target-a,array,cache)
        if ans:  
            cache[f"{target-a}"] = ans
            return True
    
    cache[f"{target}"] = False
    return False
    

print(cansum(5,[2]))
print(cansum(5,[2,1]))
print(cansum(7,[2,3]))
print(cansum(7,[5,3,4,7]))
print(cansum(7,[2,4]))
print(cansum(8,[2,3,5]))
print(cansum(300,[7,14])) # not critical anymore

