
def squares(a, b):
    # Write your code here
    num=0
    for i in range(b+1):
        if (i*i)<=b and (i*i)>=a:
            num+=1
        if (i*i)>b:
            break
            
    return num


