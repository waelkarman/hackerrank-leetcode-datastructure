def compareTriplets(a, b):
    # Write your code here
    x1=0
    x2=0
    
    if a[0]>b[0]:
        x1+=1
    elif a[0]<b[0]:
        x2+=1
    
    if a[1]>b[1]:
        x1+=1
    elif a[1]<b[1]:
        x2+=1
    
    if a[2]>b[2]:
        x1+=1
    elif a[2]<b[2]:
        x2+=1
    
    return [x1,x2]