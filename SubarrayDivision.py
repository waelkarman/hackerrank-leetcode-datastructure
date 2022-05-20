
def birthday(s, d, m):
    # Write your code here
    ways=0
    
    i=0
    while((m+i)<=len(s)):
        sum_s=0
        for x in s[i:m+i]:
            sum_s = sum_s+x
        if sum_s == d:
            ways+=1    
        i+=1

    return ways

