
def appendAndDelete(s, t, k):
    # Write your code here
    len_st=0
    #MANCA IL CASO EQUAL
    if len(s)==len(t):
        len_st = len(s)
    elif len(s)<len(t):
        len_st = len(s)
    else:
        len_st = len(t)
    val=0
    for i in range(len_st):
        if s[i] != t[i]:
            break
        val=i+1
    print("val-",val)
    print("len s:",len(s))
    

    double_val=abs(len(s)-val+len(t)-val)

    print(k," == " ,double_val)
    if k >= double_val:
        if((k-double_val)%2 == 0):
            return "Yes"
        else:
            if k > 2*len(t):
                return "Yes"
            else:
                return "No"    
    else:    
        return "No"


