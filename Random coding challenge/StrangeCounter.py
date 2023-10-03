def strangeCounter(t):
    # Write your code here
    n=0
    k=0
    i=0
    while(n<t):
        k+=pow(2,i)
        n=3*k
        i+=1
    
    return n-t+1
