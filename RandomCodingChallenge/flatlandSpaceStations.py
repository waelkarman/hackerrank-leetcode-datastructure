def flatlandSpaceStations(n, c):
    c.sort()
    l = {}
    min=0
    for i in range(len(c)-1):
        far_place=c[i]+c[i+1]
        min = c[i+1]-c[i]
        l[int(far_place/2)]=int(min/2)
      
    if c[0] != 0:  
        l[0]=c[0]
    if c[len(c)-1] != n-1:
        l[n-1]= n-1-c[len(c)-1]
     
    value0=0
    min0=0
    for k in l.keys():
        if l[k] > min0:
            min0 = l[k]
            value0 = k 

    return min0