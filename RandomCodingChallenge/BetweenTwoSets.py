
def getTotalX(a, b):
    # Write your code here
    ans=True
    var=0
    for n in range(a[len(a)-1],b[0]+1):
        var+=1
        for v_a in a:
            if n%v_a != 0:
                ans = False    
                
        for v_b in b:
            if v_b%n != 0:
                ans = False    
        
        if not ans:
            ans = True
            var-=1
    
    return var


