
def divisibleSumPairs(n, k, ar):
    # Write your code here
    ways = 0
    for i in range(n):
        for j in range(i+1,n):
            x=ar[i]+ar[j]
            if x%k == 0:
                ways += 1
    return ways


