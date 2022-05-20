
def migratoryBirds(arr):
    # Write your code here
    max_l={}
    max_val=0
    max_key=arr[0]
    for a in arr:
        max_l[a]=0
    for a in arr:
        max_l[a]+=1
    for a in max_l.keys():
        print(a,max_l[a])       
        if max_l[a] > max_val:
            max_val=max_l[a]
            max_key=a
        elif max_l[a] == max_val:    
            if max_key > a:
                max_key=a
            
    return max_key
        

