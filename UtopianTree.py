
def utopianTree(n):
    # Write your code here
    trl=True
    val=1
    for a in range(n):
        if trl == True :
            val=val*2
            
        if trl == False :
            val=val+1
            
        if trl:
            trl=False    
        else:
            trl=True
    return val   

