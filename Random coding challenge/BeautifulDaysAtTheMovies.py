
def beautifulDays(i, j, k):
    # Write your code here
    tot = 0 
    for x in range(i,j+1):    
        s=str(x)
        r=''
        for a in s:
            r = a+r
        n_r=int(r)
        #print(x,'-',n_r,'->',abs(x-n_r),'_',abs(x-n_r)%k)
        if (abs(x-n_r)%k) == 0:
            tot += 1
    
    return tot

