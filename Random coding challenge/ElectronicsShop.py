
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max_val = -1
    for a in keyboards:
        for x in drives:
            if (a+x) <= b:
                if (a+x) > max_val:
                    max_val = a+x
    return max_val


