
def pickingNumbers(a):
    # Write your code here
    minarr = []
    maxarr = []
    first = True
    maxval=0
    
    for j in range(len(a)):
        for i in a[j:len(a)]:
            if first:
                minarr.append(i)    
                maxarr.append(i)
                first = False
            else:
                if(i == minarr[0]):
                    minarr.append(i)    
                    maxarr.append(i)
                
                if(minarr[0]-i)==-1:
                    minarr.append(i)
                
                if(minarr[0]-i)==1:
                    maxarr.append(i)

        if(len(minarr)>maxval):
            maxval= len(minarr)
        if(len(maxarr)>maxval):
            maxval= len(maxarr)
        minarr.clear()
        maxarr.clear()
        first=True
        
    return maxval
                


