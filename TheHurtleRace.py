

def hurdleRace(k, height):
    # Write your code here
    m=0
    for a in height :
        if (a-k)>m :
            m=a-k
    return m

