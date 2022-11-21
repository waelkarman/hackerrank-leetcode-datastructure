def pickingNumbers(a):
    # Write your code here
    max_count = 0
    for k in range(len(a)):
        count1 = 1
        count2 = 1
        last_val = a[k]
        for i in range(k+1,len(a)): 
            
            if(last_val-a[i] == 1):
                print(f"{last_val}-{a[i]}",end="\n")
                count1+=1
                #last_val = a[i]
            if(last_val-a[i] == -1):
                print(f"{last_val}-{a[i]}",end="\n")
                count2+=1
            if(last_val-a[i] == 0):
                print(f"{last_val}-{a[i]}",end="\n")
                count2+=1
                count1+=1
        
        if (count1 > max_count):
            max_count = count1
        if (count2 > max_count):
            max_count = count2
    return max_count

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
                


