
def birthdayCakeCandles(candles):
    # Write your code here
    wmax=0
    nmax=1
    for a in candles:
        if a>wmax:
            wmax=a
            nmax=0
        if a==wmax:
            nmax+=1    
        
    return nmax


