
def howsum(target,array,sum=0):

    if sum > target:
        return None
    if sum == target:
        return []
    
    for a in array:
        ans = howsum(target,array,sum+a)
        if ans != None:
            ans.append(a)
            return ans



print(howsum(5,[1,2]))
print(howsum(5,[2,1]))