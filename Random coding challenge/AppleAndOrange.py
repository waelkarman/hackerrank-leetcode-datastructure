
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    n_apples=0
    for d in apples:
        if (a+d)>=s and (a+d)<=t:
            n_apples +=1
    
    n_oranges=0
    for d in oranges:
        if (b+d)>=s and (b+d)<=t:
            n_oranges +=1
            
    print(n_apples)
    print(n_oranges)
            
