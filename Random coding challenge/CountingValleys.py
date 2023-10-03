
def countingValleys(steps, path):
    # Write your code here
    valley = False
    level = 0
    val_num = 0
    for a in path:
        
        if a == 'U' :
            level+=1
            
        if a == 'D' :
            level-=1        
                
        if level < 0 :
            valley = True
            
        if valley and level == 0:
            valley = False
            val_num+=1
            
    return val_num   



