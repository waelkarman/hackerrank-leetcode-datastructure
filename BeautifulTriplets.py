def beautifulTriplets(d, arr):
    # Write your code here
    
    count = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(j,len(arr)):
                if( ((arr[j]-arr[i]) == (arr[k]-arr[j])) and ((arr[k]-arr[j]) == d) ):
                    count += 1
                    
    return count
