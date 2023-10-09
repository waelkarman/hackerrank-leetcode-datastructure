

def gridwalker(n,m,cache={}):
    if (n,m) in cache:
        return cache[(n,m)] 

    if n == 0 or m == 0:
        return 0 
    if n == 1 and m == 1:
        return 1
    
    cache[(n,m)] = gridwalker(n-1,m) + gridwalker(n,m-1)
    return cache[(n,m)]


print(gridwalker(4,4))
print(gridwalker(4,1))
print(gridwalker(2,2))
print(gridwalker(3,2))
print(gridwalker(2,3))
print(gridwalker(18,18)) # Not critical anymore