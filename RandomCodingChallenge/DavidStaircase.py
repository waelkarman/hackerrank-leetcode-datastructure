def stepPerms(n,memo={}):
    # Write your code here
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 1
    if n < 0 :
        return 0   
    
    l = [1,2,3]
    su=0
    for i in l:
        su+=stepPerms(n-i)
    
    memo[n]=su
    return su