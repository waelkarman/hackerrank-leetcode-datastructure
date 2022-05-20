
def angryProfessor(k, a):
    # Write your code here
    x=0
    for t in a :
        if t<=0:
            x+=1
    if x<k:
        return "YES"
    else:
        return "NO"


