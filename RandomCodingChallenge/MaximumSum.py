
# WORKING NON OPTIMIZED

def maximumSum(a, m):
    # Write your code here
    maxmod=0
    for i in range(len(a)+1): 
        subsum=0
        for j in range(len(a)):
            if j < i:
                subsum+=a[j]
                if i == j+1 :
                    if subsum%m > maxmod:
                        maxmod = subsum%m
            else:
                subsum-=a[j-i]
                subsum+=a[j]
                if subsum%m > maxmod:
                    maxmod = subsum%m


    #print(f"maxmod:{maxmod}")
    return maxmod