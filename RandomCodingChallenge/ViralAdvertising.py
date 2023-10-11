
def viralAdvertising(n):
    # Write your code here
    cumulative = 0
    shared = 5
    bu = True
    for a in range(1,n+1):

        if bu == True:
            cumulative=int(shared/2)
            bu = False
        else:
            cumulative=cumulative+int(shared/2)
        
        shared = int(shared/2)*3
       
        
    return int(cumulative)


