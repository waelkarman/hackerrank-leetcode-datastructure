
def howsum(target,array):

    if target < 0 :
        return None
    if target == 0:
        return []
    
    for a in array:
        ans = howsum(target-a,array)
        if ans is not None:
            ans.append(a)
            return ans

    return None

print(howsum(5,[1,2]))
print(howsum(5,[2,1]))
print(howsum(5,[2]))
print(howsum(7,[2,3]))
print(howsum(7,[5,3,4,7]))
print(howsum(7,[2,4]))
print(howsum(8,[2,3,5]))
print(howsum(300,[7,14])) #critical