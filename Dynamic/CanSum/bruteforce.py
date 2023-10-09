

def cansum(target,array,sum=0):

    if sum > target:
        return False
    
    if sum == target:
        return True

    
    for a in array:
        if True and cansum(target,array,sum+a):
            return True
    
    return False
    

print(cansum(5,[2]))
print(cansum(5,[2,1]))
print(cansum(7,[2,3]))
print(cansum(7,[5,3,4,7]))
print(cansum(7,[2,4]))
print(cansum(8,[2,3,5]))
print(cansum(300,[7,14])) #critical

