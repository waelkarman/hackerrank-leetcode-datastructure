def diagonalDifference(arr):
    # Write your code here
    d1=0
    d2=0
    for i in range(len(arr[0])):
        d1+=arr[i][i]
        d2+=arr[len(arr[0])-1-i][i]
    return abs(d1-d2)
