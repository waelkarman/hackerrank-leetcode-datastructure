
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    tot_fee=0
    if y2<y1 :
        return 10000
    elif y2>y1:
        return 0
    
    if m2<m1:
        return abs(m1-m2)*500
    elif m2 > m1 :
        return 0

    if d2<d1:
        tot_fee+=abs(d1-d2)*15
        

    return tot_fee

