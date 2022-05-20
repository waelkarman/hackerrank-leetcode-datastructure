
def equalizeArray(arr):
    # Write your code here
    min_sum = len(arr)
    for a in arr:
        if (len(arr)-arr.count(a))<min_sum:
            min_sum=len(arr)-arr.count(a)
    return min_sum
            
