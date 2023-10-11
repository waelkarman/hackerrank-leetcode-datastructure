
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE
# INCOMPLETE

def howsum(target,array,sum=0,l=[]):

    if sum > target:
        return []
    if sum == target:
        return l
    
    for a in array:
        ans = howsum(target,array,sum+a,l)
        l.append(a)
        return ans
    


print(howsum(5,[1,2]))
print(howsum(5,[2,1]))