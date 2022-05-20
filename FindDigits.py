

def findDigits(n):
    # Write your code here
    if n==0:
        return 0
    num = 0
    s = str(n)
    for d in s:
        if int(d) != 0 and  n%int(d) == 0 :
            num += 1

    return num

