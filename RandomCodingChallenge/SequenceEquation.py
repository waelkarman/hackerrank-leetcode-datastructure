
def permutationEquation(p):
    # Write your code here
    res = []
    for x in range(1,len(p)+1):
        for y in range(1,len(p)+1):
            if x == p[p[y-1]-1]:
                res.append(y)
    
    return res
    

