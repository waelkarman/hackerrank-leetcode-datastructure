

def minimumDistances(a):
    # Write your code here
    min_dist=len(a)
    for i in range(len(a)):        
        for j in range(len(a)):
            if a[i] == a[j] and i != j: 
                dist = abs(i-j)
                if dist < min_dist:
                    min_dist=dist
    if (min_dist==len(a) and a[0] != a[len(a)-1]) or len(a)==1:
        return -1
    else:
        return min_dist

